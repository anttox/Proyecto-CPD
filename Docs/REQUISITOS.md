# Instalación de Dependencias para el desarroolo del Proyecto 2: Sistema de Detección de Intrusos en Redes

Este documento proporciona las instrucciones detalladas para instalar todas las dependencias necesarias para el correcto desarrollo del proyecto "Sistema de detección de intrusos en redes" en un entorno virtual de Python.

## Requisitos Previos
- Ubuntu 18.04 o superior
- Acceso a un usuario con privilegios de sudo
- Conexión a Internet

## Paso 1: Actualización del Sistema
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
### Paso 4: Instalación de Scapy y PyShark
Instala Scapy y PyShark dentro del entorno virtual. Estas herramientas se utilizarán para la captura y el análisis de paquetes de red:
```sh
pip install scapy pyshark
```
### Paso 5: Configuración de Permisos para Captura de Paquetes
Configura los permisos necesarios para que Scapy pueda capturar paquetes de red:
```sh
sudo setcap cap_net_raw,cap_net_admin=eip $(readlink -f $(which python3))
```
