import pyshark
import pandas as pd
import nest_asyncio

# Permitir que el bucle de eventos de asyncio funcione en Jupyter Notebook
nest_asyncio.apply()

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

# Análisis de paquetes capturados
pcap_file = 'sprint1/data/captured_packets.pcap'  # Nombre del archivo pcap
df_packets = analyze_packets(pcap_file)

# Mostrar los datos analizados en Jupyter Notebook
display(df_packets.head())
