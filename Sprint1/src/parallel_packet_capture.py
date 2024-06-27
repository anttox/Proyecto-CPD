from scapy.all import sniff, TCP, IP
from multiprocessing import Process

# Funcion para capturar paquetes de red
def capturar_paquetes(packet):
    # Verificamos si el paquete tiene capas IP y TCP
    if packet.haslayer(IP) and packet.haslayer(TCP):
        print(f"Paquete capturado: {packet[IP].src} -> {packet[IP].dst}")

# Funcion para iniciar la captura de paquetes
def iniciar_captura():
    # Iniciamos la captura de paquetes en tiempo real con un filtrado especifico
    sniff(filter="tcp port 80 or port 443", prn=capturar_paquetes, store=0)

if __name__ == '__main__':
    # Creamos un proceso para la captura de paquetes
    proceso_captura = Process(target=iniciar_captura)
    proceso_captura.start()
    proceso_captura.join()

