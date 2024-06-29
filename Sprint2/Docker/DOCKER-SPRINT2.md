**1. Construir la imagen de Docker:**

Navega hasta el directorio donde se encuentra el Dockerfile y ejecuta el siguiente comando:

```sh
docker build -t network_traffic_analyzer .
```
![image](https://github.com/anttox/Proyecto-CPD/assets/118635410/fc7f2d39-4df3-49cf-a85a-107a926558b9)

**2. Ejecutar el contenedor de Docker:**

Una vez construida la imagen, puedes ejecutar el contenedor utilizando el siguiente comando:

```sh
docker run --rm -v $(pwd):/app network_traffic_analyzer
```
![image](https://github.com/anttox/Proyecto-CPD/assets/118635410/b5bb3b12-966e-4408-823d-e92e5deeb43d)
