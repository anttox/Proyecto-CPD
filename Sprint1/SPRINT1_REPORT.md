# Introducción

## Objetivos del Sprint:
El objetivo del Sprint 1 es desarrollar un sistema de captura y análisis de tráfico de red en tiempo real. Este sistema se enfocará en capturar tráfico HTTP y HTTPS, analizar los paquetes capturados y almacenarlos en una base de datos SQLite para su posterior análisis. Estos objetivos se alinean con el objetivo general del proyecto de desarrollar un sistema de detección de intrusos (IDS) para redes informáticas.

# Planificación

## Tareas planificadas:
* Captura de paquetes de red utilizando Scapy.
* Análisis de paquetes capturados utilizando PyShark.
* Almacenamiento de la información analizada en una base de datos SQLite.
* Documentación del diseño y arquitectura del sistema.

## Asignación de tareas:
* Captura de paquetes: Equipo de redes.
* Análisis de paquetes: Equipo de análisis de datos.
* Almacenamiento en base de datos: Equipo de backend.
* Documentación: Todos los miembros del equipo colaboran.

# Implementación
Durante este sprint, se desarrolló un sistema para capturar, analizar y almacenar paquetes de red. Se decidió utilizar Scapy para la captura de paquetes debido a su flexibilidad y capacidad de manejo de paquetes a bajo nivel. Para el análisis de los paquetes capturados, se utilizó PyShark, que permite extraer información detallada de los paquetes. Finalmente, los datos analizados se almacenaron en una base de datos SQLite.

## Métodos:
**Captura de paquetes: Se utilizó Scapy para capturar paquetes filtrando por puertos 80 y 443.**

**Código**:

![imagen](https://github.com/anttox/Proyecto-CPD/assets/118635410/b82a033d-e35d-4dd5-a938-2bc4e7fadbee)

**Ejecución y Salida**:

![imagen](https://github.com/anttox/Proyecto-CPD/assets/118635410/a93434bd-446a-4147-82b7-e8368163fe69)

**captured_packets.pcap**:

![imagen](https://github.com/anttox/Proyecto-CPD/assets/118635410/8dd09125-6d08-4ae0-90b5-d93c701391b6)
Podemos observar 10 paquetes capturados, principalmente tráfico TCP y TLSv1.2 y sus respectivos paquetes.

**Paquete 1**:
- Time: 0.000000
- Source: 206.247.35.67
- Destination: 192.168.1.11
- Protocol: TCP
- Length: 66 bytes
- Info: Puerto de origen 443 (HTTPS), puerto de destino 47080, ACK

**Paquete 2**:
- Time: 0.000515
- Source: 206.247.35.67
- Destination: 192.168.1.11
- Protocol: TLSv1.2
- Length: 104 bytes
- Info: Datos de aplicación

**Detalles de los paquetes**

Al seleccionar un paquete, por ejemplo, el Paquete 1, los detalles del paquete mostrarán:
- Ethernet II: Información sobre las direcciones MAC involucradas en la transmisión.
- Internet Protocol Version 4: Detalles sobre las direcciones IP de origen (206.247.35.67) y destino (192.168.1.11).
- Transmission Control Protocol: Información sobre los puertos (443 -> 47080) y el estado del paquete (ACK).

**Lista de Paquetes Capturados**

![imagen](https://github.com/anttox/Proyecto-CPD/assets/118635410/83ebbc95-6e5a-4283-a916-7cb2245047c4)
- No.: Número de secuencia del paquete capturado. En este caso, hay 10 paquetes capturados.
- Time: Tiempo transcurrido desde el inicio de la captura hasta el momento en que se capturó este paquete.
- Source: Dirección IP de origen del paquete.
- Destination: Dirección IP de destino del paquete.
- Protocol: Protocolo utilizado en el paquete (por ejemplo, TCP, TLSv1.2).
- Length: Longitud del paquete en bytes.
- Info: Información adicional sobre el paquete, como los números de puerto de origen y destino, y el tipo de mensaje (por ejemplo, ACK, Application Data).

**Detalles del Paquete Seleccionado**

![imagen](https://github.com/anttox/Proyecto-CPD/assets/118635410/6b3a2482-2ae9-40f5-851d-1463a6ef2651)
- Frame 1: Información sobre el frame de nivel de enlace, como el tamaño en bytes.
- Ethernet II: Detalles sobre la capa de enlace de datos, como las direcciones MAC de origen y destino.
- Internet Protocol Version 4: Información sobre la capa de red, como las direcciones IP de origen y destino.
- Transmission Control Protocol: Información sobre la capa de transporte, como los números de puerto de origen y destino, y los flags TCP (por ejemplo, ACK).

**Datos en Hexadecimal**

![imagen](https://github.com/anttox/Proyecto-CPD/assets/118635410/2f071bd4-0e4c-4a85-9f54-e8dc977fa394)
- Muestra una representación hexadecimal de los datos del paquete seleccionado. Esto incluye el contenido real del paquete tal como se capturó en la red.

**Análisis de paquetes: Se utilizó PyShark para extraer información relevante como la IP de origen, IP de destino y puertos.**

**Código**:

![imagen](https://github.com/anttox/Proyecto-CPD/assets/118635410/8189cd19-bc2d-4d2f-b50e-ab2b7f1f035b)

**Ejecución y Salida**:

![imagen](https://github.com/anttox/Proyecto-CPD/assets/118635410/2a59ed31-506e-429e-9ce8-bdbd576b1862)

**Análisis de Paquetes**

![imagen](https://github.com/anttox/Proyecto-CPD/assets/118635410/b86ab022-2697-4003-815b-54ba40cd950e)

La primera parte de la salida muestra la captura de paquetes y su análisis utilizando PyShark
- Protocolo: En este caso, TCP.
- IP de origen: Dirección IP y puerto del dispositivo que envía el paquete.
- IP de destino: Dirección IP y puerto del dispositivo que recibe el paquete.

**Almacenamiento de Paquetes**

![imagen](https://github.com/anttox/Proyecto-CPD/assets/118635410/65f6af1d-279b-4746-82d7-cc250bb00858)

La segunda parte de la salida muestra los paquetes que se han almacenado en la base de datos SQLite
- Protocolo: En este caso, TCP.
- IP de origen: Dirección IP y puerto del dispositivo que envía el paquete.
- IP de destino: Dirección IP y puerto del dispositivo que recibe el paquete.

**Verificación de Datos Almacenados**

![imagen](https://github.com/anttox/Proyecto-CPD/assets/118635410/d76889e7-9d69-47c1-bde5-074d3ca9f0b8)

- protocol: Protocolo de la comunicación (TCP).
- src_addr: Dirección IP de origen.
- src_port: Puerto de origen.
- dst_addr: Dirección IP de destino.
- dst_port: Puerto de destino.

**Almacenamiento: Se creó una tabla en SQLite para almacenar los datos analizados.**

![imagen](https://github.com/anttox/Proyecto-CPD/assets/118635410/f4c67394-f8dd-4ce6-963b-58fc83a2fa8d)

Para poder visualizar los datos del archivo SQLite `network_traffic.db` que contiene la información de los paquetes de red capturados y analizados.
**Actualizamos e instalamos SQLite**
```sh
sudo apt-get update
sudo apt-get install sqlite3
```
**Iniciamos SQLite**
```sh
sqlite3 network_traffic.db
```
**Listamos las Tablas**
```sh
.tables
```
Este comando muestra todas las tablas existentes en la base de datos. En este caso, muestra que hay una tabla llamada traffic.
**Consultamos los Datos**
```sh
SELECT * FROM traffic;
```
La tabla traffic contiene la siguiente estructura:
- protocol: El protocolo utilizado, que es TCP en todos los casos mostrados.
- src_addr: La dirección IP de origen. Por ejemplo, 162.159.133.234, 192.168.1.11, etc.
- src_port: El puerto de origen. Por ejemplo, 443, 38048, 48930, etc.
- dst_addr: La dirección IP de destino. Por ejemplo, 192.168.1.11, 140.82.113.25, etc.
- dst_port: El puerto de destino. Por ejemplo, 443, 47080, etc.

## Desafíos encontrados:
* Configuración de permisos para capturar paquetes en tiempo real.
* Manejo de diferentes formatos de paquetes y extracción de información.
* Asegurar la integridad y consistencia de los datos almacenados en la base de datos.

# Resultados

## Funcionalidades desarrolladas:
* Captura de paquetes HTTP y HTTPS.
* Análisis detallado de los paquetes capturados.
* Almacenamiento de datos en una base de datos SQLite.

## Pruebas realizadas:
* Pruebas de captura: Se verificó la correcta captura de paquetes de red.
* Pruebas de análisis: Se comprobó que la información extraída de los paquetes es precisa.
* Pruebas de almacenamiento: Se verificó que los datos se almacenan correctamente en la base de datos.

## Demostración de funcionalidades:
* Captura de pantalla del archivo .pcap generado.
* Ejemplos de análisis de paquetes en el Jupyter Notebook.
* Visualización de datos almacenados en SQLite.

# Análisis y evaluación

## Comparación con los objetivos del Sprint:
Los objetivos del Sprint 1 se cumplieron satisfactoriamente. Se logró desarrollar un sistema funcional de captura, análisis y almacenamiento de paquetes de red.

## Lecciones aprendidas:
* La importancia de configurar correctamente los permisos de red para capturar paquetes.
* La utilidad de PyShark para analizar detalladamente los paquetes capturados.
* La necesidad de realizar un manejo adecuado de la base de datos para asegurar la integridad de los datos.

# Plan para el próximo Sprint

## Objetivos del próximo Sprint:
* Implementar técnicas de machine learning para detectar actividades sospechosas en los datos de tráfico de red.
* Desarrollar una interfaz de usuario para visualizar los resultados del análisis en tiempo real.

## Tareas planificadas:
* Integración de algoritmos de machine learning.
* Desarrollo de la interfaz de usuario.
* Pruebas y validación del sistema completo.

## Ajustes necesarios:
* Ajustar la estructura de la base de datos para almacenar resultados de análisis de machine learning.
* Mejorar el rendimiento del sistema para manejar grandes volúmenes de datos en tiempo real.
