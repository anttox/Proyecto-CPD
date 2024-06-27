# Proyecto 2: Sistema de detección de intrusos en redes – Renzo Vilca

## Objetivo del proyecto
Desarrollar un sistema de detección de intrusos (IDS) para redes informáticas, capaz de capturar y analizar tráfico de red en tiempo real para identificar actividades sospechosas utilizando técnicas de machine learning.

## Estructura del Proyecto

### Sprint 1: Desarrollo de un sistema de captura de paquetes de red y análisis básico de tráfico
- **Objetivos:**
  - Capturar paquetes de red en tiempo real.
  - Realizar un análisis básico del tráfico de red.

- **Actividades:**
  - Configuración del entorno:
    - Instalar y configurar Scapy y PyShark para la captura y análisis de paquetes.
    - Asegurar permisos necesarios para la captura de paquetes (ejecutar como root/administrador).
  - Captura de paquetes:
    - Desarrollar un script para capturar paquetes de red en tiempo real utilizando Scapy.
    - Configurar filtros básicos para capturar solo el tráfico relevante (HTTP, HTTPS, TCP).
  - Análisis básico de tráfico:
    - Utilizar PyShark para analizar los paquetes capturados y extraer información relevante (direcciones IP, puertos, protocolos).
    - Almacenar los datos capturados y analizados en un formato estructurado (CSV o base de datos SQLite).

- **Entregables:**
  - Script de captura de paquetes de red.
  - Código de análisis básico de tráfico.
  - Informe sobre la configuración del entorno y los resultados iniciales del análisis de tráfico.

### Sprint 2: Implementación de algoritmos de detección de anomalías utilizando técnicas de machine learning
- **Objetivos:**
  - Implementar algoritmos de detección de anomalías.
  - Aplicar técnicas de machine learning para identificar tráfico anómalo.

- **Actividades:**
  - Preprocesamiento de datos:
    - Limpiar y preprocesar los datos capturados para la preparación de los modelos de machine learning.
    - Extraer características relevantes de los paquetes (tamaño del paquete, tiempo entre paquetes, número de paquetes por segundo).
  - Entrenamiento de modelos de machine learning:
    - Seleccionar algoritmos de detección de anomalías (Isolation Forest, One-Class SVM).
    - Entrenar los modelos utilizando scikit-learn y validar los resultados con un conjunto de datos etiquetados.
  - Evaluación de modelos:
    - Evaluar la precisión y la tasa de falsos positivos/negativos de los modelos.
    - Realizar ajustes necesarios para mejorar el rendimiento de los modelos.

- **Entregables:**
  - Modelos entrenados de detección de anomalías.
  - Código para el entrenamiento y evaluación de los modelos.
  - Informe sobre el rendimiento y la precisión de los modelos implementados.

### Sprint 3: Optimización para análisis en tiempo real utilizando multiprocessing y asyncio, y presentación de los hallazgos
- **Objetivos:**
  - Optimizar el sistema para análisis en tiempo real.
  - Exponer los resultados del proyecto en una presentación detallada.

- **Actividades:**
  - Optimización del sistema:
    - Implementar técnicas de paralelismo utilizando multiprocessing para capturar y analizar múltiples flujos de tráfico simultáneamente.
  - Implementación de análisis asíncrono:
    - Utilizar asyncio para realizar el análisis de paquetes de manera asíncrona, permitiendo el procesamiento en tiempo real sin bloqueos.
  - Despliegue del sistema:
    - Desarrollar una interfaz de usuario simple para la visualización en tiempo real de las detecciones de anomalías (utilizando Flask o Dash).
  - Preparación de la presentación:
    - Crear una presentación que detalle los objetivos, metodología, resultados y conclusiones del proyecto.
    - Incluir demostraciones en vivo del sistema funcionando y análisis de casos de uso específicos.

- **Entregables:**
  - Código optimizado del sistema de detección de intrusos en tiempo real.
  - Interfaz de usuario para la visualización de detecciones.
  - Presentación detallada con demostraciones y análisis de casos.
  - Informe final del proyecto con documentación completa del desarrollo y resultados obtenidos.
  - Repositorio de GitHub con toda la documentación, código y resultados del proyecto.

## Requisitos de Software
- Python 3.x
- Scapy
- PyShark
- scikit-learn
- Flask o Dash
- asyncio
- multiprocessing
- SQLite (opcional)
