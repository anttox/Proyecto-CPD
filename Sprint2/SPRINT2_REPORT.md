# Introducción

## Objetivos del Sprint
El objetivo de este sprint fue mejorar la detección de anomalías en el tráfico de red mediante el uso de modelos de aprendizaje automático. En particular, se buscó entrenar y evaluar modelos de Isolation Forest y One-Class SVM utilizando datos capturados y analizados en tiempo real.

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

![image](https://github.com/anttox/Proyecto-CPD/assets/118635410/9d522427-8a1f-4f65-85a5-13a5ca8ba95e)

**Ejecución y Salida**

![image](https://github.com/anttox/Proyecto-CPD/assets/118635410/cdec75c6-aa9b-4d61-85d9-8d80af9e63c2)

![image](https://github.com/anttox/Proyecto-CPD/assets/118635410/f6d3f528-87ff-4394-9e38-4e127c0abb9f)

**Preprocesamiento de Datos**

**1. Cargar datos desde SQLite**:

- Se cargan los datos desde una base de datos SQLite utilizando la función load_data_from_db.
- La salida muestra los primeros cinco registros de los datos cargados, con las columnas protocol, src_addr, src_port, dst_addr, y dst_port.

**Entrenamiento de Modelos de Machine Learning**

**2. Aumentar la proporción de anomalías en los datos de entrenamiento**:

- Se generan 100 ejemplos de anomalías uniformemente distribuidas entre -10 y 10.
- Estas anomalías se agregan a los datos preprocesados para formar X_train_with_anomalies y y_train_with_anomalies.

**3.Entrenamiento de Isolation Forest con diferentes parámetros de contaminación**:

- Se entrena el modelo Isolation Forest con tres diferentes valores de contaminación: 0.05, 0.1, y 0.15.
- Se imprime un reporte de clasificación para cada valor de contaminación, el cual incluye métricas de precisión, recall y f1-score.

**Evaluación de Modelos**

**4. Generar datos de prueba incluyendo anomalías sintéticas**:

- Se generan datos de prueba normales (X_test_normal) y anomalías sintéticas.
- Estas anomalías se agregan a los datos de prueba normales para formar X_test_anomalies y y_test_anomalies.

**5. Evaluar Isolation Forest con diferentes valores de contaminación**:

- Para cada valor de contaminación (0.05, 0.1, 0.15), se muestra un reporte de clasificación que evalúa el rendimiento del modelo Isolation Forest.
- Las métricas de evaluación incluyen:
  - precision: Proporción de verdaderos positivos entre los elementos clasificados como positivos.
  - recall: Proporción de verdaderos positivos entre todos los elementos que son realmente positivos.
  - f1-score: La media armónica de precisión y recall.
  - support: El número de ocurrencias de cada clase en el conjunto de prueba.

**Evaluación de Isolation Forest con diferentes valores de contaminación**

**1. Evaluación de Isolation Forest con contaminación=0.05**:

Clase 0 (normal): precision 0.96, recall 1.00, f1-score 0.98.
Clase 1 (anomalía): precision 1.00, recall 0.20, f1-score 0.33.
Interpretación: El modelo tiene alta precisión para detectar tráfico normal pero baja recall para detectar anomalías, lo que significa que detecta pocas anomalías.
Evaluación de Isolation Forest con contaminación=0.1:

Clase 0 (normal): precision 0.96, recall 1.00, f1-score 0.98.
Clase 1 (anomalía): precision 1.00, recall 0.20, f1-score 0.33.
Interpretación: Resultados similares a la contaminación=0.05, indicando un comportamiento consistente.
Evaluación de Isolation Forest con contaminación=0.15:

Clase 0 (normal): precision 0.97, recall 1.00, f1-score 0.99.
Clase 1 (anomalía): precision 1.00, recall 0.40, f1-score 0.57.
Interpretación: Aumentar la contaminación mejora la recall para las anomalías, aunque sigue siendo baja. La precisión para detectar tráfico normal sigue siendo alta.
Evaluación de Isolation Forest con datos aumentados
Evaluación de Isolation Forest con datos aumentados:
Clase 0 (normal): precision 0.97, recall 1.00, f1-score 0.99.
Clase 1 (anomalía): precision 1.00, recall 0.40, f1-score 0.57.
Interpretación: Los resultados son consistentes con los obtenidos con una contaminación del 0.15, lo que sugiere que el modelo maneja bien los datos aumentados.
Evaluación de One-Class SVM con datos aumentados
Evaluación de One-Class SVM con datos aumentados:
Clase 0 (normal): precision 1.00, recall 1.00, f1-score 1.00.
Clase 1 (anomalía): precision 1.00, recall 0.95, f1-score 0.97.
Interpretación: One-Class SVM muestra un rendimiento superior en comparación con Isolation Forest, con una precisión y recall muy altas para ambas clases. Esto indica que el modelo SVM es capaz de detectar casi todas las anomalías con alta precisión.
