# Introducción

## Objetivos del Sprint:

- Optimizar el sistema de detección de intrusos en redes para análisis en tiempo real.
- Desarrollar una interfaz de usuario para la visualización de resultados.
- Preparar y presentar los resultados del proyecto.

# Planificación

## Tareas planificadas:

- Implementar técnicas de paralelismo utilizando multiprocessing para capturar y analizar múltiples flujos de tráfico simultáneamente.
- Utilizar asyncio para realizar el análisis de paquetes de manera asíncrona.
- Desarrollar una interfaz de usuario con Flask para la visualización en tiempo real de las detecciones de anomalías.
- Preparar la presentación final detallando los objetivos, metodología, resultados y conclusiones del proyecto.

# Implementación

## Descripción del trabajo realizado:

- Se implementaron técnicas de paralelismo utilizando multiprocessing para capturar y analizar múltiples flujos de tráfico simultáneamente, lo cual mejoró significativamente el rendimiento del sistema.
- Se utilizó asyncio para realizar el análisis de paquetes de manera asíncrona, permitiendo un procesamiento en tiempo real sin bloqueos.
- Se desarrolló una interfaz de usuario con Flask, proporcionando una visualización clara y en tiempo real de las detecciones de anomalías.
- Se preparó una presentación detallada que incluye demostraciones en vivo del sistema y análisis de casos de uso específicos.

# Funcionalidades

**1. Captura de paquetes**

![image](https://github.com/anttox/Proyecto-CPD/assets/118635410/85842a55-19d8-4007-9c4d-06d0977552a6)

- Función: capture_packets_live(queue, packet_count=100, iface='enp7s0')
- Descripción: Captura paquetes de red en vivo desde una interfaz de red especificada. Utiliza Scapy para capturar los paquetes y los almacena en una cola para su posterior procesamiento.

**2. Preprocesamiento de Paquetes:**

![image](https://github.com/anttox/Proyecto-CPD/assets/118635410/ef5cd6cb-5dbc-4f3c-8293-2b627def287e)

![image](https://github.com/anttox/Proyecto-CPD/assets/118635410/a20af2d8-03c4-4d69-ad3b-7c5fdb72a922)

- Función: preprocess_live_packets(packets)
- Descripción: Preprocesa los paquetes capturados para extraer características relevantes como las direcciones IP de origen y destino, los puertos, el protocolo y la marca de tiempo. Convierte estas características en un DataFrame adecuado para los modelos de aprendizaje automático.

**3. Detección de Anomalías:**

![image](https://github.com/anttox/Proyecto-CPD/assets/118635410/d210922f-342c-418d-88aa-298a690d1635)

- Función: detect_anomalies_live(df_scaled)
- Descripción: Utiliza los modelos Isolation Forest y One-Class SVM para detectar anomalías en los datos de paquetes preprocesados. Escala los datos y ajusta los modelos para identificar outliers.

**4. Captura y Procesamiento Asincrónicos de Paquetes:**

![image](https://github.com/anttox/Proyecto-CPD/assets/118635410/14ba8a2a-674a-4492-8c64-6954dd6d669c)

- Función: async_capture_packets(queue, packet_count=100, iface='enp7s0')
- Descripción: Captura paquetes de forma asincrónica utilizando asyncio para evitar bloquear el hilo principal. Esta función ayuda a capturar paquetes y procesarlos en tiempo real.
python

**5. Aplicación Web con Flask:**

![image](https://github.com/anttox/Proyecto-CPD/assets/118635410/4908ed27-eed8-445c-9bb7-1c70512bd938)

![image](https://github.com/anttox/Proyecto-CPD/assets/118635410/b53ad65d-5cca-45d8-973a-9d01753fd0d8)

![image](https://github.com/anttox/Proyecto-CPD/assets/118635410/3e722d1f-ea50-480b-83aa-8d4f0647938a)

- Función: Inicialización de la aplicación Flask y rutas (/ y /anomalies)
- Descripción: La aplicación Flask sirve una interfaz web para mostrar los resultados de la detección de anomalías en tiempo real. El endpoint /anomalies proporciona datos JSON de las anomalías detectadas, y el endpoint /plot.png sirve los gráficos de anomalías.

**6. Multithreading para Detección en Tiempo Real:**

![image](https://github.com/anttox/Proyecto-CPD/assets/118635410/e27e404c-ec4f-40ee-80f0-96fd0d5fa2d5)

- Descripción: Utiliza hilos para ejecutar la captura de paquetes y la detección de anomalías en paralelo con el servidor web Flask. Esto garantiza que el sistema pueda procesar paquetes y actualizar la interfaz web en tiempo real.

