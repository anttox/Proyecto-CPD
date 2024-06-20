# Detección de Anomalías en Tráfico de Red

## Objetivos

1. Implementar algoritmos de detección de anomalías.
2. Aplicar técnicas de machine learning para identificar tráfico anómalo.

## Actividades

### Preprocesamiento de Datos

1. Limpiar y preprocesar los datos capturados para la preparación de los modelos de machine learning.
2. Extraer características relevantes de los paquetes (por ejemplo, tamaño del paquete, tiempo entre paquetes, número de paquetes por segundo).

### Entrenamiento de Modelos de Machine Learning

1. Seleccionar algoritmos de detección de anomalías (por ejemplo, Isolation Forest, One-Class SVM).
2. Entrenar los modelos utilizando scikit-learn y validar los resultados con un conjunto de datos etiquetados.

### Evaluación de Modelos

1. Evaluar la precisión y la tasa de falsos positivos/negativos de los modelos.
2. Realizar ajustes necesarios para mejorar el rendimiento de los modelos.

## Conceptos clave

### Computación Paralela
La computación paralela implica ejecutar múltiples procesos simultáneamente para acelerar el procesamiento. En el código, se utiliza el módulo multiprocessing para capturar y analizar paquetes de red en paralelo.

### Computación Distribuida
La computación distribuida consiste en distribuir tareas a través de múltiples nodos de computación que trabajan juntos. Aunque el código se ejecuta en un solo sistema, los conceptos de computación distribuida son aplicables si se implementara en un entorno distribuido.

### Machine Learning
Subcampo de la inteligencia artificial que permite a las máquinas aprender de los datos y hacer predicciones. Se utilizan modelos de machine learning como Isolation Forest y One-Class SVM para detectar anomalías en el tráfico de red.

### Detección de Anomalías
Técnica utilizada para identificar datos inusuales o anómalos que no se ajustan a un patrón esperado. Se utilizan modelos de machine learning para identificar patrones anómalos en los datos de tráfico de red.

## Relevancia en Computación Paralela y Distribuida

### Procesamiento Concurrente
La capacidad de ejecutar múltiples procesos simultáneamente. En el código, se utiliza el módulo multiprocessing para capturar y analizar paquetes de red en paralelo, lo que permite una captura más rápida y eficiente de grandes volúmenes de datos.

### Escalabilidad Horizontal
Aumentar el rendimiento mediante la adición de más nodos de computación. Si el código se implementara en un entorno distribuido, la escalabilidad horizontal permitiría procesar grandes volúmenes de datos de tráfico de red de manera eficiente.

### Sincronización y Comunicación
En sistemas distribuidos, la sincronización entre procesos y la comunicación eficiente son cruciales. En el código, los procesos de captura de paquetes y análisis de datos deben sincronizarse correctamente para evitar condiciones de carrera.



