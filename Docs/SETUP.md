# Instalación de Dependencias para el desarroolo del Proyecto 2: Sistema de Detección de Intrusos en Redes

Este documento proporciona las instrucciones detalladas para instalar todas las dependencias necesarias para el correcto desarrollo del proyecto "Sistema de detección de intrusos en redes" en un entorno virtual de Python en la terminal de Linux y en Jupyter Notebook.

## Requisitos Previos
- Ubuntu 18.04 o superior
- Acceso a un usuario con privilegios de sudo
- Conexión a Internet
- Python 3.6 o superior
- pip
- virtualenv (opcional pero recomendado)

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
### Paso 4: Instalar Dependencias
Dentro del entorno virtual, instala las bibliotecas necesarias.
```sh
pip install scapy pyshark nest_asyncio pandas jupyter
```
### Paso 5: Trabajar en Jupyter Notebook
Para ejecutar comandos que requieren permisos elevados dentro de un Jupyter Notebook en un entorno Linux, puedes usar el comando sudo dentro de las celdas del notebook. Sin embargo, ejecutar sudo directamente en las celdas no funcionará debido a que Jupyter Notebook no tiene una interfaz para solicitar contraseñas. En su lugar, puedes iniciar Jupyter Notebook con permisos de superusuario desde la terminal. (Importante: Usa la opción --allow-root)
```sh
sudo jupyter notebook --allow-root
```
### Paso 6: Acceder a Jupyter Notebook desde el navegador proporcionado al ejecutar el comando sudo jupyter notebook --allow-root
Copia y pega la URL en el navegador proporcionada por Jupyter Notebook en la terminal. Será algo como esto:
```sh
http://localhost:8888/?token=77e141ac4db96559d16dd3fc45c888099a1778ffad521588
```



