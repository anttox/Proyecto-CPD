# Instalación de Dependencias para el desarroolo del Proyecto 2: Sistema de Detección de Intrusos en Redes

Este documento proporciona las instrucciones detalladas para instalar todas las dependencias necesarias para el correcto desarrollo del proyecto "Sistema de detección de intrusos en redes" en un entorno virtual de Python en la terminal de Linux y en Jupyter Notebook.

## Requisitos Previos
- Ubuntu 18.04 o superior
- Acceso a un usuario con privilegios de sudo
- Conexión a Internet

### Paso 1: Actualización del Sistema
Primero, actualiza tu lista de paquetes e instala las últimas actualizaciones:
```sh
sudo apt update && sudo apt upgrade -y
```
### Paso 2: Instalación de Python y pip
```sh
sudo apt install python3 python3-pip -y
```
### Paso 3: Crear y Activar un Entorno Virtual
Crea un entorno virtual para instalar las dependencias del proyecto de manera aislada:
```sh
python3 -m venv myenv
source myenv/bin/activate
```
### Paso 2: Instalar Dependencias
Dentro del entorno virtual, instala las bibliotecas necesarias.
```sh
pip install scapy pyshark nest_asyncio pandas jupyter
```
