# Uso de Scapy y Pyshark en un sistema de Deteccion de Intrusos (IDS) - Script1
## Introducción

El desarrollo de un sistema de deteccion de intrusos (IDS) en redes informáticas es fundamental para la ciberseguridad actual. Ya que permite capturar y analizar el tráfico de red en tiempo real, y se puede lograr identificar actividades sospechozas o maliciosas. Estos sistemas son esenciales para prevenir ataques, detectar intrusos y garantizar la seguridad informática en una red.
En este proyecto usaremos heramientas fundamentales como el uso de Scapy y Pyshark.
Ojo no son las únicas herramientas que Python nos ofrece, tenemos a Suricata y Bro/Zeek, pero su facilidad para trabajar con la obtención de paquetes de red es más simple ya que los usuarios pueden simular ataques o verificar la robustez de los sistemas contra ciertas amenazas usando Scapy o analizar tráfco de red en tiempo real con Pyshark, aunque siempre va a depender de las necesidades específicas del proyecto.

## Scapy
Scapy es una herramienta de Python que permte trabajar con paquetes de red muy flexibles. Para que Scapy pueda capturar paquetes en tiempo real usamos la función "sniff". Sniff filtra el tráfico HTTP y HTTPS, lo que permite inspeccionar los paquetes de manera detallada y rápida. Gracias a su simplicidad y flexibilidad, Scapy es ideal para la captura de paquetes de bajo nivel, integrándose fácilmente en sistemas personalizados de detección de intrusos.

- Flexibilidad: Nos referimos a la capacidad que tiene Scapy de adaptarse a una amplia gama de necesidades y situaciones (Crear y modificar paquetes, Capturar paquetes en tiempo real, Compatibilidad con múltiples protocolos como IP, TCP, ICMP, etc).
- Simmplicidad: En Scapy se puede realizar con facilidad tareas complejas debido a la manipulación de paquetes de red con pocas líneas de código. Scapy tiene una sintaxis intuituva y permite a los usuarios realizar operaciones avanzadas sin necesidad de una configuración extensa ni de una comprensión profunda de los protocolos de red subyacentes.

## Pyshark
Pyshark, por otro lado, es una interfaz de python para Wireshark (wrapper), conocido por analizar y capturar tráfico de red en tiempo real. Se utiliza para capturar paquetes en una interfaz específica, filtrando el tráfico TCP en los pertos que se asigne. Además, Pyshark facilita la extracción y registro de información relevante de los paquetes capturados en un arhivo CSV o una base de datos SQlite (use CSV ya que por el momento la tareas son mas faciles porque las tareas y los datos son pequeños), lo cual es muy útil para análisis posteriores y para identificar patrones sospechozos.

- Wrapper: Pieza de código que encapsula o envuelve otra pieza de código para proporcionar una interfaz más sencilla o más conveniente.
- Compatibilidad con Wireshark: Pyshark se basa en la funcionalidad de Wireshark, lo que le permite utilizar las potentes capacidades de análisis y filtrado de Wireshark. Esto incluye la capacidad de entender y decodificar una amplia variedad de protocolos de red.
- Flexibilidad: Ofrece capacidades avanzadas de filtrado utilizando Berkeley Packet Filter (BPF) y filtros de visualización de Wireshark, permitiendo capturar solo el tráfico relevante.
- Soporte: Pyshark puede decodificar y analizar una amplia gama de protocolos de red, lo que lo hace adecuado para diversas aplicaciones y entornos de red.

## Desafíos
Desarrollar un sistema IDS utilizando Scapy y Pyshark presenta varios desafíos. A continuación detallo los principales desafíos que enfrenté durante el desarrollo del proyecto:
1. Rendimiento: La captura y análisis en tiempo real pueden consumir muchos recursos, lo cual puede afectar el rendimiento del sistema si no se optimiza correctamente.
2. Escalabilidad: A medida que el tráfico aumenta, es crucial que el sistema pueda escalar para manejar grandes volúmenes de datos sin perder información.
3. Exactitud: Identificar amenazas con precisión es esencial para minimizar falsos positivos y negativos, requiriendo un equilibrio entre sensibilidad y especificidad en los filtros y algoritmos de detección.

## Posibles mejores futuras con paralelización
Para mejorar el rendimiento y la escalabilidad del sistema IDS, se puede implementar paralelización. Esto permite distribuir la carga de trabajo entre múltiples procesadores o núcleos, mejorando la eficiencia y capacidad del sistema. Durante el desarrollo del proyecto me di cuenta de la gran cantidad de tiempo que tenia que esperar para recibir los paquetes o cuando aumenta el volumen de tráfico en la red, el sistema de detección de intrusos debe ser capaz de capturar y analizar más datos sin perder rendimiento, entonces me di cuenta que la mejor forma de solucionar estos problemas potenciales es dividiendo el problemas en partes mas pequeñas que pueden ser ejecutadas simultáneamente en múltiples procesadores o nucleos de procesadores. Las posibles mejoras que tengo en mente son las siguientes:
1. Utilizar múltiples hilos o procesos para capturar y analizar paquetes simultáneamente, reduciendo el tiempo de procesamiento y mejorando la capacidad de respuesta del sistema.
2. Implementar una arquitectura distribuida donde varios servidores capturan y analizan el tráfico de red en diferentes segmentos, agregando los resultados en un nodo central para un análisis integral y unificado.

## Referencias
1. Documentación de Scapy, https://scapy.readthedocs.io/en/latest/introduction.html#about-scapy
2. Documentación de Pyshark, https://github.com/KimiNewt/pyshark
3. Idea de paralelización, https://cr0hn.gumroad.com/l/libro-scapy
