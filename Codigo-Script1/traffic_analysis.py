import pyshark
import csv

# Funcion para analizar y almacenar paquetes en un archivo CSV
def analizar_paquetes():
    captura = pyshark.LiveCapture(interface='enp7s0')
    # Abre el archivo CSV para escritura
    with open('datos_paquetes.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        # Escribimos las cabeceras en el archivo CSV
        writer.writerow(['Origen', 'Destino', 'Protocolo'])
        # Capturamos y analizamos los paquetes continuamente
        for packet in captura.sniff_continuously(packet_count=100):
            if 'IP' in packet:
                src_ip = packet.ip.src
                dst_ip = packet.ip.dst
                protocolo = packet.transport_layer
                print(f"Origen: {src_ip}, Destino: {dst_ip}, Protocolo: {protocolo}")
                # Escribimos los datos en el archivo CSV
                writer.writerow([src_ip, dst_ip, protocolo])

analizar_paquetes()

