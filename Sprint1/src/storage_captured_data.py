import pyshark
import pandas as pd
import sqlite3
from scapy.all import sniff, wrpcap

# Función para capturar paquetes en tiempo real y guardarlos en un archivo .pcap
def capture_and_save_packets(packet_count=10, filename='captured_packets.pcap'):
    packets = sniff(filter="tcp port 80 or tcp port 443", count=packet_count)
    wrpcap(filename, packets)
    print(f"Se han capturado y guardado {packet_count} paquetes en {filename}")

# Función para analizar paquetes capturados utilizando PyShark
def analyze_packets(pcap_file):
    capture = pyshark.FileCapture(pcap_file)
    packet_data = []
    for packet in capture:
        try:
            protocol = packet.transport_layer
            src_addr = packet.ip.src
            src_port = packet[packet.transport_layer].srcport
            dst_addr = packet.ip.dst
            dst_port = packet[packet.transport_layer].dstport
            packet_data.append({
                'protocol': protocol,
                'src_addr': src_addr,
                'src_port': src_port,
                'dst_addr': dst_addr,
                'dst_port': dst_port
            })
            print(f"{protocol} Paquete: {src_addr}:{src_port} -> {dst_addr}:{dst_port}")
        except AttributeError:
            # Ignorar paquetes sin capa de transporte
            pass
    return pd.DataFrame(packet_data)

# Función para almacenar datos en la base de datos SQLite
def store_packet(packet):
    try:
        protocol = packet['protocol']
        src_addr = packet['src_addr']
        src_port = packet['src_port']
        dst_addr = packet['dst_addr']
        dst_port = packet['dst_port']
        c.execute("INSERT INTO traffic (protocol, src_addr, src_port, dst_addr, dst_port) VALUES (?, ?, ?, ?, ?)",
                  (protocol, src_addr, src_port, dst_addr, dst_port))
        conn.commit()
        print(f"Stored packet: {protocol} {src_addr}:{src_port} -> {dst_addr}:{dst_port}")
    except AttributeError as e:
        print(f"Packet skipped: {e}")

# Paso 1: Capturar y guardar paquetes en un archivo .pcap
capture_and_save_packets(packet_count=10, filename='captured_packets.pcap')

# Paso 2: Analizar los paquetes capturados
pcap_file = 'captured_packets.pcap'  # Nombre del archivo pcap
df_packets = analyze_packets(pcap_file)

# Paso 3: Crear base de datos y tabla
conn = sqlite3.connect('network_traffic.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS traffic
             (protocol TEXT, src_addr TEXT, src_port INTEGER, dst_addr TEXT, dst_port INTEGER)''')

# Paso 4: Almacenar los datos analizados
for index, row in df_packets.iterrows():
    store_packet(row)

# Paso 5: Verificar los datos almacenados
df = pd.read_sql_query("SELECT * FROM traffic", conn)
print(df)

# Mostrar los datos en la terminal
print(df.head())

# Cerrar la conexión a la base de datos
conn.close()
