# Introducción

- **Objetivos del Sprint**:

El objetivo del Sprint 1 es desarrollar un sistema de captura y análisis de tráfico de red en tiempo real. Este sistema se enfocará en capturar tráfico HTTP y HTTPS, analizar los paquetes capturados y almacenarlos en una base de datos SQLite para su posterior análisis. Estos objetivos se alinean con el objetivo general del proyecto de desarrollar un sistema de detección de intrusos (IDS) para redes informáticas.

# Planificación

## Tareas planificadas:
* Captura de paquetes de red utilizando Scapy.
* Análisis de paquetes capturados utilizando PyShark.
* Almacenamiento de la información analizada en una base de datos SQLite.
* Documentación del diseño y arquitectura del sistema.

## Asignación de tareas:
* Captura de paquetes: Equipo de redes.
* Análisis de paquetes: Equipo de análisis de datos.
* Almacenamiento en base de datos: Equipo de backend.
* Documentación: Todos los miembros del equipo colaboran.

# Implementación
Durante este sprint, se desarrolló un sistema para capturar, analizar y almacenar paquetes de red. Se decidió utilizar Scapy para la captura de paquetes debido a su flexibilidad y capacidad de manejo de paquetes a bajo nivel. Para el análisis de los paquetes capturados, se utilizó PyShark, que permite extraer información detallada de los paquetes. Finalmente, los datos analizados se almacenaron en una base de datos SQLite.

## Métodos:
* Captura de paquetes: Se utilizó Scapy para capturar paquetes filtrando por puertos 80 y 443.
* Análisis de paquetes: Se utilizó PyShark para extraer información relevante como la IP de origen, IP de destino y puertos.
* Almacenamiento: Se creó una tabla en SQLite para almacenar los datos analizados.

## Desafíos encontrados:
* Configuración de permisos para capturar paquetes en tiempo real.
* Manejo de diferentes formatos de paquetes y extracción de información.
* Asegurar la integridad y consistencia de los datos almacenados en la base de datos.

# Resultados

## Funcionalidades desarrolladas:
* Captura de paquetes HTTP y HTTPS.
* Análisis detallado de los paquetes capturados.
* Almacenamiento de datos en una base de datos SQLite.

## Pruebas realizadas:
* Pruebas de captura: Se verificó la correcta captura de paquetes de red.
* Pruebas de análisis: Se comprobó que la información extraída de los paquetes es precisa.
* Pruebas de almacenamiento: Se verificó que los datos se almacenan correctamente en la base de datos.

## Demostración de funcionalidades:
* Captura de pantalla del archivo .pcap generado.
* Ejemplos de análisis de paquetes en el Jupyter Notebook.
* Visualización de datos almacenados en SQLite.
