# Instalaciones necesarias para desarrollar el Proyecto 2: Sistema de detección de intrusos en redes

## Requisitos previos generales
- Ubuntu 18.04 o superior
- Acceso a un usuario con privilegios de sudo
- Conexión a Internet

## Sprint 1: Desarrollo de un sistema de captura de paquetes de red y análisis básico de tráfico

### Paso 1: Actualización del sistema
Actualiza la lista de paquetes e instala las últimas actualizaciones:

```sh
!apt update && apt upgrade -y
!apt install python3 python3-pip -y

