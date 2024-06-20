# Detección de Anomalías en Tráfico de Red - Script2

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

## Partes del Código Original Utilizadas
Del código original que utilicé en el Scrip1, tomé los siguientes elementos y los integré en el nuevo código:
1. Captura de paquetes: Utilicé la funcionalidad de Pyshark para capturar paquetes en tiempo real.
2. Almacenamiento de datos en CSV: Implementé la lógica para escribir los datos capturados en un nuevo archivo CSV.
3. Uso de multiprocessing: Utilicé multiprocessing para ejecutar la captura de paquetes en procesos separados, permitiendo el procesamiento paralelo.

## Almacenamiento de datos en un archivo CSV
El código original también incluía la lógica para almacenar los datos capturados en un archivo CSV. Esto es importante para persistir los datos de tráfico de red para análisis posteriores.

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

## Algoritmos de Machine Learning para Detección de Anomalías
Utilizaremos dos algoritmos de Machine Learning: Isolation Forest y One-Class SVM

### Insolation Forest
Este algoritmo se encarga de detectar anomalías construyendo árboles de aislamiento de las observaciones. Las observaciones que requieren menos particiones para ser aisladas son consideradas anomalías.

La idea principal detrás de Isolation Forest es que las anomalías son puntos de datos que son más fáciles de aislar que los puntos normales. El algoritmo construye varios árboles de aislamiento, y la profundidad en la que un punto es aislado se utiliza como medida de su grado de anomalía.

¿Para que sirve la construcción de estos árboles?

Insoltation forest genera de manera aleatoria la partición de datos mediante árboles de aislamiento. Las particiones aleatorias dividen los datos hasta que cada punto es aislado. Las anomalías tienden a ser aisladas con menos particiones debido a que están más alejadas de los puntos normales. Ademas Insolation Forest es eficiente tanto en tiempo como en memoria, ya que la construcción de árboles de aislamiento es un proceso relativamente rápido y los árboles no son profundos. 

¿A que nos referimos que Insolation Forest es esficiente?

Pues que nos permite manejar grandes volúmenes de datos rápidamente, lo cual es crucial para analísis de red en tiempor real. La robustez tambien esta presente en este algoritmo ya que no requiere de suposiciones sobre la distribución de datos, lo que permite detectar anomalías en datos de red que pueden tener distribuciones complejas (Fraude financiero). Por ultimo Insolation Forest es altamente escalable con datos grandes, esto es importante en entornos de red donde el volumén de datos es significativo (Ataques DDoS en recursos de AWS).

### One-Class SVM
Este algoritmo se encuentra en una frontera de desición que separa las observaciones normales de los anómalas en un espacio de caracterísiticas de alta dimensión.

One-Class SVM intenta encontrar una frontera de decisión que separe los datos normales de los datos anómalos en un espacio de alta dimensión.

One-Class SVM utiliza la función de kernel para proyectar los datos en un espacio de alta dimensión donde es más fácil separarlos. Comúnmente se utiliza el kernel RBF (Radial Basis Function). Ademas se entrena solo con datos de una clase (datos normales) y se trata de identificar puntos que no se ajustan a la distribución de estos datos como anomalías.

¿Para que nos sirve utilizar funciones de kernel en One-Class SVM?
Al utilizar funciones de kernel, One-Class SVM puede capturar relaciones no lineales en los datos, lo cual es útil en datos de red que pueden tener relaciones complejas. Y esto es muy efectivo para identificar anomalías durante una buna representación de datos normales.

## Métricas de Evaluación: Precisión, Recall y F1-Score

### Precisión 
La precisión es la proporción de verdaderos positivos (TP) entre todos los casos predichos como positivos (TP + FP). Es una medida de cuántas de las predicciones positivas del modelo son realmente correctas. En la detección de anomalías en tráfico de red, alta precisión significa que la mayoría de las alertas de anomalías son verdaderamente anómalas, reduciendo las falsas alarmas.
![image1](


### Recall
El recall, también conocido como sensibilidad o tasa de verdaderos positivos, es la proporción de verdaderos positivos entre todos los casos que son realmente positivos (TP + FN). Alto recall asegura que la mayoría de las anomalías reales son detectadas, lo cual es crucial para la seguridad de la red.

### F1-Score
El F1-Score es la media armónica de la precisión y el recall. Proporciona un balance entre ambos y es útil cuando se necesita un compromiso entre precisión y recall. Proporciona una métrica equilibrada que es útil cuando tanto la precisión como el recall son importantes para evaluar el rendimiento del modelo.









