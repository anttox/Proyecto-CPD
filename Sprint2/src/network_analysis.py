# Preprocesamiento de Datos
import pandas as pd
import sqlite3
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sklearn.ensemble import IsolationForest
from sklearn.svm import OneClassSVM
from sklearn.metrics import classification_report

# Cargar datos desde SQLite
def load_data_from_db(db_name='network_traffic.db', table_name='traffic'):
    conn = sqlite3.connect(db_name)
    df = pd.read_sql_query(f"SELECT * FROM {table_name}", conn)
    conn.close()
    return df

df_packets = load_data_from_db()

# Mostrar las primeras filas de los datos cargados
print(df_packets.head())

# Función para preprocesar los datos
def preprocess_data(df):
    # Convertir direcciones IP a enteros
    def ip_to_int(ip):
        try:
            return int(''.join(f'{int(i):08b}' for i in ip.split('.')), 2)
        except:
            return 0

    df['src_addr'] = df['src_addr'].apply(ip_to_int)
    df['dst_addr'] = df['dst_addr'].apply(ip_to_int)

    # Extraer características relevantes
    df['packet_size'] = df['src_port'] + df['dst_port']

    # Seleccionar solo las columnas numéricas
    numeric_columns = ['src_addr', 'dst_addr', 'src_port', 'dst_port', 'packet_size']

    # Llenar valores faltantes con la mediana
    df[numeric_columns] = df[numeric_columns].fillna(df[numeric_columns].median())

    # Normalizar los datos
    scaler = StandardScaler()
    df_scaled = scaler.fit_transform(df[numeric_columns])

    return df_scaled

df_preprocessed = preprocess_data(df_packets)

# Visualizar la distribución de los datos preprocesados
sns.pairplot(pd.DataFrame(df_preprocessed, columns=['src_addr', 'dst_addr', 'src_port', 'dst_port', 'packet_size']))
plt.savefig('pairplot.png')

# Aumentar la proporción de anomalías en los datos de entrenamiento
anomalies_train = np.random.uniform(low=-10, high=10, size=(100, df_preprocessed.shape[1]))  # Generar 100 ejemplos de anomalías
X_train_with_anomalies = np.vstack([df_preprocessed, anomalies_train])
y_train_with_anomalies = [0] * len(df_preprocessed) + [1] * 100

# Entrenamiento de Isolation Forest con diferentes parámetros de contaminación
def train_isolation_forest(X_train, contamination):
    model = IsolationForest(contamination=contamination)
    model.fit(X_train)
    return model

# Función para evaluar el modelo
def evaluate_model(model, X_test, y_test):
    y_pred = model.predict(X_test)
    y_pred = [1 if x == -1 else 0 for x in y_pred]
    print(classification_report(y_test, y_pred))

# Generar datos de prueba incluyendo anomalías sintéticas
X_test_normal = df_preprocessed
y_test_normal = [0] * len(X_test_normal)

# Crear anomalías sintéticas (por ejemplo, valores fuera del rango normal)
anomalies = np.random.uniform(low=-10, high=10, size=(10, X_test_normal.shape[1]))
X_test_anomalies = np.vstack([X_test_normal, anomalies])
y_test_anomalies = y_test_normal + [1] * 10

# Probar diferentes valores de contaminación
for contamination in [0.05, 0.1, 0.15]:
    print(f"Evaluación de Isolation Forest con contaminación={contamination}:")
    isolation_forest_model = train_isolation_forest(X_train_with_anomalies, contamination)
    evaluate_model(isolation_forest_model, X_test_anomalies, y_test_anomalies)

# Entrenamiento de One-Class SVM
def train_one_class_svm(X_train):
    model = OneClassSVM(nu=0.1)
    model.fit(X_train)
    return model

one_class_svm_model = train_one_class_svm(X_train_with_anomalies)

# Evaluación de Modelos
print("Evaluación de Isolation Forest con datos aumentados:")
evaluate_model(isolation_forest_model, X_test_anomalies, y_test_anomalies)

print("Evaluación de One-Class SVM con datos aumentados:")
evaluate_model(one_class_svm_model, X_test_anomalies, y_test_anomalies)

