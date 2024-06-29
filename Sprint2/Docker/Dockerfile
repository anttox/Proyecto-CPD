# Utilizar una imagen base con Python
FROM python:3.12-slim

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar los archivos necesarios al contenedor
COPY requirements.txt requirements.txt
COPY network_traffic_analysis.py network_traffic_analysis.py
COPY network_traffic.db network_traffic.db

# Instalar las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Ejecutar el script de Python
CMD ["python", "network_traffic_analysis.py"]

