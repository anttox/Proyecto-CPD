import scapy.all as scapy
import pyshark
import csv
import os
import random
from multiprocessing import Process
from sklearn.preprocessing import StandardScaler
import pandas as pd
from sklearn.ensemble import IsolationForest
from sklearn.svm import OneClassSVM
from sklearn.metrics import classification_report

# Definir la ruta completa del archivo CSV
current_directory = os.path.dirname(os.path.realpath(__file__))
csv_file_path = os.path.join(current_directory, 'datos_paquetes.csv')
pcap_file_path = os.path.join(current_directory, 'captura_paquetes.pcap')

# Función para capturar paquetes con Scapy y guardar en un archivo pcap
def capturar_paquetes():
    paquetes = scapy.sniff(iface='enp7s0', count=100, prn=lambda x: x.summary())
    scapy.wrpcap(pcap_file_path, paquetes)

# Función para analizar paquetes capturados con Pyshark y guardar en CSV
def analizar_paquetes():
    captura = pyshark.FileCapture(pcap_file_path)
    with open(csv_file_path, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Origen', 'Destino', 'Protocolo', 'Longitud', 'label'])
        for packet in captura:
            if 'IP' in packet:
                src_ip = packet.ip.src
                dst_ip = packet.ip.dst
                protocolo = packet.transport_layer
                longitud = int(packet.length) if hasattr(packet, 'length') else 0
                label = random.choices([0, 1], weights=[0.5, 0.5], k=1)[0]
                print(f"Origen: {src_ip}, Destino: {dst_ip}, Protocolo: {protocolo}, Longitud: {longitud}, Label: {label}")
                writer.writerow([src_ip, dst_ip, protocolo, longitud, label])

# Función principal
if __name__ == '__main__':
    try:
        # Intentar eliminar el archivo existente para evitar problemas de permisos
        if os.path.exists(csv_file_path):
            os.remove(csv_file_path)
        
        # Capturar paquetes usando Scapy
        proceso_captura = Process(target=capturar_paquetes)
        proceso_captura.start()
        proceso_captura.join()
        
        # Analizar paquetes capturados usando Pyshark
        analizar_paquetes()
        
        # Verificar que el archivo CSV ha sido creado correctamente
        if os.path.exists(csv_file_path):
            # Preprocesamiento de datos
            data = pd.read_csv(csv_file_path)
            if 'Longitud' in data.columns and 'label' in data.columns:
                data['tamaño_paquete'] = data['Longitud']
                data['tiempo_entre_paquetes'] = data['Longitud'].shift(-1) - data['Longitud']
                data['numero_paquetes_por_segundo'] = data['Longitud'].expanding().count()
                data.fillna(0, inplace=True)

                # Estandarizar las características
                scaler = StandardScaler()
                data_scaled = scaler.fit_transform(data[['tamaño_paquete', 'tiempo_entre_paquetes', 'numero_paquetes_por_segundo']])

                # Entrenamiento de modelos
                model_if = IsolationForest(contamination=0.1, random_state=42)
                model_if.fit(data_scaled)
                # Convertir las predicciones a 0 y 1
                data['anomaly_if'] = model_if.predict(data_scaled)
                data['anomaly_if'] = data['anomaly_if'].apply(lambda x: 0 if x == 1 else 1)

                model_ocsvm = OneClassSVM(nu=0.1, kernel="rbf", gamma=0.1)
                model_ocsvm.fit(data_scaled)
                # Convertir las predicciones a 0 y 1
                data['anomaly_ocsvm'] = model_ocsvm.predict(data_scaled)
                data['anomaly_ocsvm'] = data['anomaly_ocsvm'].apply(lambda x: 0 if x == 1 else 1)

                # Evaluación de modelos
                print("Isolation Forest")
                print(classification_report(data['label'], data['anomaly_if'], zero_division=1))

                print("One-Class SVM")
                print(classification_report(data['label'], data['anomaly_ocsvm'], zero_division=1))
            else:
                print("Las columnas 'Longitud' o 'label' no están presentes en el archivo CSV.")
        else:
            print(f"El archivo {csv_file_path} no se ha creado.")
    except PermissionError as e:
        print(f"Permission error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

