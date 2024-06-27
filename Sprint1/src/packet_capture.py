from scapy.all import sniff, wrpcap

# Función para capturar paquetes en tiempo real y guardarlos en un archivo .pcap
def capture_and_save_packets(packet_count=10, filename='sprint1/data/captured_packets.pcap'):
    packets = sniff(filter="tcp port 80 or tcp port 443", count=packet_count)
    wrpcap(filename, packets)
    print(f"Se han capturado y guardado {packet_count} paquetes en {filename}")

# Capturar y guardar paquetes en un archivo .pcap
capture_and_save_packets(packet_count=10, filename='sprint1/data/captured_packets.pcap')

