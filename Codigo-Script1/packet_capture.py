from scapy.all import sniff, TCP, IP

# Funcion para capturar paquetes de red
def capturar_paquetes(packet):
    # Verifica si el paquete tiene capas IP y TCP
    if packet.haslayer(IP) and packet.haslayer(TCP):
        print(f"Paquete capturado: {packet[IP].src} -> {packet[IP].dst}")

# Iniciamos la captura de paquetes en tiempo real con un filtrado especifico
sniff(filter="tcp port 80 or port 443", prn=capturar_paquetes, store=0)

