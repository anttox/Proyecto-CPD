# Introducción

## Objetivos del Sprint
Desarrollar un sistema de detección de intrusos (IDS) para redes informáticas, capaz de capturar y analizar tráfico de red en tiempo real para identificar actividades sospechosas utilizando técnicas de machine learning.

# Planificación

## Tareas Planificadas
- Captura de paquetes de red utilizando Scapy.
- Análisis de los paquetes capturados con PyShark.
- Almacenamiento de los datos analizados en una base de datos SQLite.
- Preprocesamiento de los datos para su uso en modelos de aprendizaje automático.
- Entrenamiento y evaluación de modelos de Isolation Forest y One-Class SVM.
- Visualización y análisis de resultados.

# Implementación

## Descripción del Trabajo Realizado

### Captura y Análisis de Paquetes
Se utilizó Scapy para capturar paquetes de red en tiempo real y guardarlos en un archivo .pcap. Luego, se empleó PyShark para analizar estos paquetes y extraer características relevantes como protocolo, dirección IP de origen, puerto de origen, dirección IP de destino y puerto de destino.

### Almacenamiento en Base de Datos
Los datos analizados se almacenaron en una base de datos SQLite para facilitar su acceso y manipulación en etapas posteriores.

### Preprocesamiento de Datos
Los datos se preprocesaron convirtiendo las direcciones IP a formato entero, calculando el tamaño del paquete y normalizando las características numéricas.

### Entrenamiento y Evaluación de Modelos
Se entrenaron modelos de Isolation Forest y One-Class SVM utilizando una combinación de datos normales y anomalías sintéticas. Los modelos se evaluaron utilizando métricas de clasificación como precisión, recall y f1-score.

# Algoritmos y Métodos

## Isolation Forest
Se utilizó el algoritmo Isolation Forest para detectar anomalías en los datos de red. Este algoritmo es especialmente adecuado para detectar outliers en conjuntos de datos grandes y de alta dimensionalidad.

## One-Class SVM
El modelo One-Class SVM se entrenó para identificar anomalías en el tráfico de red. Este modelo es útil para problemas de detección de anomalías cuando solo se dispone de datos de una clase (normal).

# Desafíos Encontrados
- Captura de Paquetes: La configuración de permisos y la necesidad de ejecutar el código con privilegios de superusuario para la captura de paquetes en tiempo real.
- Preprocesamiento: Normalización y conversión de direcciones IP.
- Evaluación de Modelos: Ajuste de hiperparámetros y evaluación de rendimiento.

# Resultados

## Funcionalidades Desarrolladas
- Captura de paquetes de red en tiempo real.
- Análisis y almacenamiento de paquetes en una base de datos SQLite.
- Preprocesamiento de datos para modelos de aprendizaje automático.
- Entrenamiento y evaluación de modelos de Isolation Forest y One-Class SVM.

# Pruebas Realizadas
Se realizaron pruebas utilizando datos de prueba con anomalías sintéticas para evaluar el rendimiento de los modelos. Los resultados mostraron una buena capacidad de detección de anomalías, aunque se identificaron áreas para mejorar en términos de precisión y recall.

**Código**

![image](https://github.com/anttox/Proyecto-CPD/assets/118635410/399e126b-4e55-400c-b06b-610a607f432a)

De todas maneras el código se puede encontrar y ejecutar en el directorio src.

**Ejecución y Salida**

![image](https://github.com/anttox/Proyecto-CPD/assets/118635410/ec447c8d-243a-42df-8de7-3f60c27fedfd)

**Preprocesamiento de datos**

![image](https://github.com/anttox/Proyecto-CPD/assets/118635410/14459947-efa8-4deb-b8ee-7ec212ea5a7a)

Descripción: Limpiar y preprocesar los datos capturados para la preparación de los modelos de machine learning. Extraer características relevantes de los paquetes (por ejemplo, tamaño del paquete, tiempo entre paquetes, número de paquetes por segundo).

**Resultados:**

- Datos preprocesados y estructurados listos para el modelado.
- Implementación de funciones para convertir direcciones IP a enteros, calcular el tamaño de los paquetes y el intervalo de tiempo entre ellos.

**Entrenamiento de modelos de machine learning**

![image](https://github.com/anttox/Proyecto-CPD/assets/118635410/9982a3a6-d616-42e2-ac05-3e8ee613a4ac)

Descripción: Seleccionar algoritmos de detección de anomalías (por ejemplo, Isolation Forest, One-Class SVM). Entrenar los modelos utilizando scikit-learn y validar los resultados con un conjunto de datos etiquetados.

**Resultados:**

- Modelos de Isolation Forest y One-Class SVM entrenados.
- Ajuste de hiperparámetros utilizando GridSearchCV para optimizar el rendimiento de los modelos.

**Evaluación de modelos**

![image](https://github.com/anttox/Proyecto-CPD/assets/118635410/6c5f75b7-1808-41c3-bd2b-5805e409d92c)

Descripción: Evaluar la precisión y la tasa de falsos positivos/negativos de los modelos. Realizar ajustes necesarios para mejorar el rendimiento de los modelos.

**Resultados:**

- Métricas de evaluación de los modelos (Precision, Recall, F1 Score, Accuracy).
- Comparación del rendimiento entre Isolation Forest y One-Class SVM.
- Ajustes realizados para mejorar la precisión y reducir los falsos positivos.

# Entregables
- Modelos entrenados de detección de anomalías.
- Código para el entrenamiento y evaluación de los modelos.
- Informe sobre el rendimiento y la precisión de los modelos implementados.

# Conclusiones
Durante este sprint, se logró implementar y evaluar algoritmos de machine learning para la detección de anomalías en el tráfico de red. Los modelos entrenados demostraron una capacidad significativa para identificar actividades sospechosas con una buena precisión y una baja tasa de falsos positivos. Los resultados obtenidos sentaron las bases para la optimización y el análisis en tiempo real en el siguiente sprint.

# Próximos pasos
En el próximo Sprint 3, se optimizará el sistema para análisis en tiempo real utilizando técnicas de paralelismo y asincronía. Además, se preparará una presentación detallada de los hallazgos y se desarrollará una interfaz de usuario para la visualización de las detecciones de anomalías.




