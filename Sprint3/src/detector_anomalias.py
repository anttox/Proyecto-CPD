import asyncio
import multiprocessing
from scapy.all import sniff, get_if_list
import pandas as pd
import numpy as np
from sklearn.ensemble import IsolationForest
from sklearn.svm import OneClassSVM
from sklearn.preprocessing import StandardScaler
import nest_asyncio
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from flask import Flask, render_template_string, jsonify, send_file
import threading
import time
import os

# Configurar los modelos
isolation_forest = IsolationForest()
one_class_svm = OneClassSVM()

def capture_packets_live(queue, packet_count=100, iface='enp7s0'):
    print(get_if_list())  # Verifica las interfaces disponibles
    packets = sniff(filter="ip", count=packet_count, iface=iface)
    print(f"Capturados {len(packets)} paquetes en la interfaz {iface}")
    queue.put(packets)

def preprocess_live_packets(packets):
    packet_data = []
    for packet in packets:
        if 'IP' in packet:
            try:
                if packet.haslayer('TCP'):
                    protocol = 'TCP'
                    src_port = packet['TCP'].sport
                    dst_port = packet['TCP'].dport
                elif packet.haslayer('UDP'):
                    protocol = 'UDP'
                    src_port = packet['UDP'].sport
                    dst_port = packet['UDP'].dport
                else:
                    continue

                src_addr = int(''.join([f'{int(octet):08b}' for octet in packet['IP'].src.split('.')]), 2)
                dst_addr = int(''.join([f'{int(octet):08b}' for octet in packet['IP'].dst.split('.')]), 2)
                timestamp = packet.time

                packet_data.append({
                    'protocol': protocol,
                    'src_addr': src_addr,
                    'src_port': src_port,
                    'dst_addr': dst_addr,
                    'dst_port': dst_port,
                    'timestamp': timestamp
                })
            except Exception as e:
                print(f"Paquete ignorado debido a error: {e}")
        else:
            print("Paquete ignorado debido a falta de capa IP")

    df = pd.DataFrame(packet_data)
    print(f"Paquetes procesados: {len(df)}")
    if not df.empty:
        df['packet_size'] = df['src_port'] + df['dst_port']
        df['time_interval'] = df['timestamp'].diff().fillna(0)

        numeric_columns = ['src_addr', 'dst_addr', 'src_port', 'dst_port', 'packet_size', 'time_interval']
        df[numeric_columns] = df[numeric_columns].fillna(df[numeric_columns].median())
        scaler = StandardScaler()
        df_scaled = scaler.fit_transform(df[numeric_columns])
        return df, df_scaled
    else:
        return None, None

def detect_anomalies_live(df_scaled):
    if df_scaled is not None:
        anomalies_if = isolation_forest.fit_predict(df_scaled)
        anomalies_svm = one_class_svm.fit_predict(df_scaled)
        return anomalies_if, anomalies_svm
    else:
        return [], []

async def async_capture_packets(queue, packet_count=100, iface='enp7s0'):
    loop = asyncio.get_event_loop()
    packets = await loop.run_in_executor(None, lambda: sniff(filter="ip", count=packet_count, iface=iface))
    print(f"Capturados {len(packets)} paquetes en la interfaz {iface}")
    await queue.put(packets)

async def async_main_live_detection(packet_count=100, iface='enp7s0'):
    queue = asyncio.Queue()
    await async_capture_packets(queue, packet_count, iface)

    packets = await queue.get()
    print(f"Primeros 5 paquetes capturados: {packets[:5]}")
    df, df_scaled = preprocess_live_packets(packets)
    anomalies_if, anomalies_svm = detect_anomalies_live(df_scaled)
    return anomalies_if, anomalies_svm, df

def main_live_detection(packet_count=100, iface='enp7s0'):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    nest_asyncio.apply(loop)
    anomalies_if, anomalies_svm, df = loop.run_until_complete(async_main_live_detection(packet_count, iface))
    return anomalies_if, anomalies_svm, df

# Nueva función para guardar el gráfico de anomalías
def save_anomaly_plot(df, anomalies_if, anomalies_svm):
    plt.figure(figsize=(10, 5))

    # Graficar los datos originales
    plt.scatter(df['timestamp'], df['packet_size'], color='blue', label='Normal')

    # Graficar las anomalías detectadas por Isolation Forest
    if anomalies_if is not None:
        plt.scatter(df['timestamp'][anomalies_if == -1], df['packet_size'][anomalies_if == -1], color='red', label='Isolation Forest Anomalies')

    # Graficar las anomalías detectadas por One-Class SVM
    if anomalies_svm is not None:
        plt.scatter(df['timestamp'][anomalies_svm == -1], df['packet_size'][anomalies_svm == -1], color='green', label='One-Class SVM Anomalies')

    plt.xlabel('Time')
    plt.ylabel('Packet Size')
    plt.title('Anomalies Over Time')
    plt.legend()
    plt.savefig('/tmp/anomalies_with_labels.png')
    plt.close()

# Configurar Flask
app = Flask(__name__)

# Variables globales para almacenar los resultados
anomalies_if = []
anomalies_svm = []
df_global = pd.DataFrame()

def run_detection():
    global anomalies_if, anomalies_svm, df_global
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    while True:
        try:
            anomalies_if, anomalies_svm, df = main_live_detection(100, iface='enp7s0')
            df_global = df
            save_anomaly_plot(df_global, anomalies_if, anomalies_svm)
            time.sleep(10)  # Esperar 10 segundos antes de la siguiente captura
        except Exception as e:
            print(f"Error en la detección: {e}")

@app.route('/')
def index():
    return render_template_string('''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Detección de Anomalías en Tiempo Real</title>
        <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
        <style>
            body {
                font-family: Arial, sans-serif;
            }
            h1 {
                text-align: center;
            }
            .anomalies {
                margin: 20px;
            }
            .anomaly-list {
                list-style-type: none;
                padding: 0;
            }
            .anomaly-item {
                padding: 10px;
                border: 1px solid #ddd;
                margin-bottom: 5px;
            }
            .plot {
                margin: 20px;
                text-align: center;
            }
        </style>
    </head>
    <body>
        <h1>Detección de Anomalías en Tiempo Real</h1>
        <div class="anomalies">
            <h2>Isolation Forest</h2>
            <ul id="if-anomalies" class="anomaly-list"></ul>
            <h2>One-Class SVM</h2>
            <ul id="svm-anomalies" class="anomaly-list"></ul>
        </div>
        <div class="plot">
            <h2>Gráficos de Anomalías</h2>
            <img src="/plot.png" alt="Anomalies Plot">
        </div>
        <script>
            function fetchAnomalies() {
                $.getJSON('/anomalies', function(data) {
                    $('#if-anomalies').empty();
                    $('#svm-anomalies').empty();

                    data.IsolationForest.forEach(function(anomaly, index) {
                        $('#if-anomalies').append('<li class="anomaly-item">' + anomaly + '</li>');
                    });

                    data.OneClassSVM.forEach(function(anomaly, index) {
                        $('#svm-anomalies').append('<li class="anomaly-item">' + anomaly + '</li>');
                    });
                });
            }

            setInterval(fetchAnomalies, 5000);  // Actualizar cada 5 segundos
            fetchAnomalies();
        </script>
    </body>
    </html>
    ''')

@app.route('/anomalies')
def get_anomalies():
    global anomalies_if, anomalies_svm
    return jsonify({
        'IsolationForest': np.array(anomalies_if).tolist(),
        'OneClassSVM': np.array(anomalies_svm).tolist()
    })

@app.route('/plot.png')
def plot_png():
    global df_global
    if isinstance(df_global, pd.DataFrame) and not df_global.empty:
        return send_file('/tmp/anomalies_with_labels.png', mimetype='image/png')
    else:
        return "No plot available", 404

if __name__ == "__main__":
    detection_thread = threading.Thread(target=run_detection)
    detection_thread.start()
    app.run(debug=False, host='0.0.0.0', port=8000)

