# Detalles del Diseño y Arquitectura

## Introducción

El objetivo de este proyecto es desarrollar un sistema de detección de intrusos (IDS) para redes informáticas. El sistema está diseñado para capturar y analizar el tráfico de red en tiempo real para identificar actividades sospechosas utilizando técnicas de machine learning. Este documento describe la arquitectura y el diseño del sistema desarrollado en el Sprint 1.

## Arquitectura del Sistema

El sistema se compone de dos componentes principales:

1. **Captura de Paquetes de Red**: Un script que utiliza Scapy para capturar paquetes de red en tiempo real.
2. **Análisis de Tráfico**: Un script que utiliza PyShark para analizar los paquetes capturados y almacenar la información relevante en un archivo CSV.

### Captura de Paquetes de Red

El componente de captura de paquetes está implementado en el script `parallel_packet_capture.py`. Este script utiliza la biblioteca Scapy para capturar paquetes de red en tiempo real y multiprocesamiento para mejorar el rendimiento. Los paquetes capturados se filtran para incluir solo tráfico HTTP y HTTPS.

**Diagrama de Flujo de la Captura de Paquetes**:

```plaintext
Inicio -> Iniciar Captura -> Capturar Paquete -> Verificar Capas IP y TCP -> Imprimir Información del Paquete -> Fin
```
### Análisis de Tráfico

El componente de análisis de tráfico está implementado en el script parallel_traffic_analysis.py. Este script utiliza la biblioteca PyShark para analizar los paquetes capturados. La información relevante, como la IP de origen, la IP de destino y el protocolo, se extrae y almacena en un archivo CSV. El script utiliza multiprocesamiento para manejar la carga de trabajo de manera eficiente.

**Diagrama de Flujo del Análisis de Tráfico**:

```plaintext
Inicio -> Iniciar Análisis -> Capturar Paquete -> Extraer Información del Paquete -> Almacenar Información en CSV -> Fin
```
### Detalles Técnicos
`parallel_packet_capture.py`
* Bibliotecas Utilizadas: Scapy, multiprocessing
* Función Principal:
    * `capturar_paquetes(packet)`: Captura y procesa los paquetes de red.
    * `iniciar_captura()`: Inicia el proceso de captura de paquetes.
* Flujo de Ejecución:
    * Se crea un proceso para la captura de paquetes.
    * Se captura el tráfico de red en tiempo real, filtrando por puertos 80 y 443.
    * Se verifica si los paquetes tienen capas IP y TCP, y se imprime la información relevante.

`parallel_traffic_analysis.py`
* Bibliotecas Utilizadas: PyShark, csv, multiprocessing
* Función Principal:
   * `analizar_paquetes()`: Analiza los paquetes capturados y almacena la información en un archivo CSV.
* Flujo de Ejecución:
   * Se crea un proceso para el análisis de paquetes.
   * Se captura el tráfico de red utilizando PyShark.
   * Se extrae información relevante (IP de origen, IP de destino, protocolo) y se almacena en un archivo CSV.
