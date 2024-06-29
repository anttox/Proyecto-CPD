import pandas as pd
import sqlite3
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.ensemble import IsolationForest
from sklearn.metrics import precision_score, recall_score, f1_score, accuracy_score, make_scorer
from sklearn.model_selection import GridSearchCV
import numpy as np
from sklearn.svm import OneClassSVM

def load_data_from_db(db_name='network_traffic.db', table_name='traffic'):
    conn = sqlite3.connect(db_name)
    df = pd.read_sql_query(f"SELECT * FROM {table_name}", conn)
    conn.close()
    return df

def preprocess_data(df):
    def ip_to_int(ip):
        try:
            return int(''.join(f'{int(i):08b}' for i in ip.split('.')), 2)
        except:
            return 0

    df['src_addr'] = df['src_addr'].apply(ip_to_int)
    df['dst_addr'] = df['dst_addr'].apply(ip_to_int)
    df['packet_size'] = df['src_port'] + df['dst_port']
    df['time_interval'] = df['timestamp'].diff().fillna(pd.Timedelta(seconds=0)).dt.total_seconds()
    numeric_columns = ['src_addr', 'dst_addr', 'src_port', 'dst_port', 'packet_size', 'time_interval']
    df[numeric_columns] = df[numeric_columns].fillna(df[numeric_columns].median())
    scaler = StandardScaler()
    df_scaled = scaler.fit_transform(df[numeric_columns])
    return df_scaled

def evaluate_model(model, X_test, y_test):
    y_pred = model.predict(X_test)
    y_pred = [1 if x == -1 else 0 for x in y_pred]
    precision = precision_score(y_test, y_pred, average='macro', zero_division=1)
    recall = recall_score(y_test, y_pred, average='macro', zero_division=1)
    f1 = f1_score(y_test, y_pred, average='macro', zero_division=1)
    accuracy = accuracy_score(y_test, y_pred)
    return precision, recall, f1, accuracy

if __name__ == "__main__":
    df_packets = load_data_from_db()
    df_packets['timestamp'] = pd.date_range(start='2023-01-01', periods=len(df_packets), freq='s')
    print(df_packets.head())

    df_preprocessed = preprocess_data(df_packets)
    sns.pairplot(pd.DataFrame(df_preprocessed, columns=['src_addr', 'dst_addr', 'src_port', 'dst_port', 'packet_size', 'time_interval']))
    plt.show()

    anomalies_train = np.random.uniform(low=-10, high=10, size=(2000, df_preprocessed.shape[1]))
    X_train_with_anomalies = np.vstack([df_preprocessed, anomalies_train])
    y_train_with_anomalies = [0] * len(df_preprocessed) + [1] * 2000

    param_grid = {
        'n_estimators': [50, 100, 200],
        'max_samples': ['auto', 0.6, 0.8],
        'contamination': [0.02, 0.05, 0.1],
        'max_features': [1.0, 0.8, 0.6]
    }

    if_model = IsolationForest()
    scorer = make_scorer(f1_score, average='macro')
    gs = GridSearchCV(if_model, param_grid=param_grid, scoring=scorer, cv=3, verbose=1, n_jobs=-1)
    gs.fit(df_preprocessed, [0] * len(df_preprocessed))
    best_if_model = gs.best_estimator_

    X_test_normal = df_preprocessed
    y_test_normal = [0] * len(X_test_normal)
    anomalies = np.random.uniform(low=-10, high=10, size=(200, X_test_normal.shape[1]))
    X_test_anomalies = np.vstack([X_test_normal, anomalies])
    y_test_anomalies = y_test_normal + [1] * 200

    precision_if, recall_if, f1_if, accuracy_if = evaluate_model(best_if_model, X_test_anomalies, y_test_anomalies)

    results_if = pd.DataFrame({
        'Metric': ['Precision', 'Recall', 'F1 Score', 'Accuracy'],
        'Score': [precision_if, recall_if, f1_if, accuracy_if]
    })

    print("Resultados de Isolation Forest")
    print(results_if)
    results_if.set_index('Metric').plot(kind='bar', figsize=(10, 6), ylim=(0, 1), colormap='viridis')
    plt.title('Performance Metrics for Isolation Forest')
    plt.ylabel('Score')
    plt.xticks(rotation=0)
    plt.legend(loc='lower right')
    plt.show()

    param_grid_svm = {'nu': [0.05, 0.1, 0.15], 'kernel': ['rbf'], 'gamma': ['scale', 'auto']}
    grid_search_svm = GridSearchCV(OneClassSVM(), param_grid_svm, cv=5, scoring='accuracy')
    grid_search_svm.fit(X_train_with_anomalies, y_train_with_anomalies)
    best_svm_model = grid_search_svm.best_estimator_

    precision_svm, recall_svm, f1_svm, accuracy_svm = evaluate_model(best_svm_model, X_test_anomalies, y_test_anomalies)

    results_svm = pd.DataFrame({
        'Metric': ['Precision', 'Recall', 'F1 Score', 'Accuracy'],
        'Score': [precision_svm, recall_svm, f1_svm, accuracy_svm]
    })

    print("Resultados de One-Class SVM")
    print(results_svm)
    results_svm.set_index('Metric').plot(kind='bar', figsize=(10, 6), ylim=(0, 1), colormap='viridis')
    plt.title('Performance Metrics for One-Class SVM')
    plt.ylabel('Score')
    plt.xticks(rotation=0)
    plt.legend(loc='lower right')
    plt.show()

