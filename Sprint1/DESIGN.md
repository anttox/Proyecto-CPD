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
