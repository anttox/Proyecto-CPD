# Introducción
Para implementar el proyecto en Docker, necesitas seguir algunos pasos para crear las imágenes Docker y configurar los archivos necesarios

## 1. Crear el Dockerfile
Primero, vamos a crear un Dockerfile que definirá cómo construir la imagen Docker para el proyecto.

![imagen](https://github.com/anttox/Proyecto-CPD/assets/118635410/068662ed-ce18-4acd-94f2-ce0b2a0bea97)

## 2. Crear el archivo de requisitos
Creamos un archivo requirements.txt con las dependencias necesarias:

![imagen](https://github.com/anttox/Proyecto-CPD/assets/118635410/a1544239-ffc6-4a36-b69f-9fe157478e29)

## 3. Construir y ejecutar la imagen Docker
Ejecutamos los siguientes comandos en nuestra terminal para construir y ejecutar la imagen Docker.
```sh
# Construimos la imagen Docker
docker build -t network-intrusion-detection-system .
```
![imagen](https://github.com/anttox/Proyecto-CPD/assets/118635410/e0eaf81d-921b-48c2-86e1-51fc492978f8)

```sh
# Ejecutamos el contenedor Docker
docker run -p 8888:8888 -v $(pwd):/app network-intrusion-detection-system
```
![imagen](https://github.com/anttox/Proyecto-CPD/assets/118635410/dedf8a6e-6162-408d-8c8b-50b29d040c06)

**Descripción del Comando**
v $(pwd):/app:
- -v es la opción para montar un volumen.
- $(pwd) es una expresión de shell que se evalúa como el directorio actual en el que estás trabajando.
- :/app es el punto de montaje dentro del contenedor Docker.
