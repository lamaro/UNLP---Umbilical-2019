# Proyecto UNLP - Umbilical
Autor: Amaro García Leandro

Objetivo principal:
Detectar movimiento mediante la cámara en una Raspi y enviar mensajes OSC a otra computadora dentro de la red. Se configuró la aplicacion para enviar mensajes al Resolume Arena 4 el cual dispara videos según la captura de movimiento de la Raspi.

Hardware
- Raspberry Pi 3
- Picamera Rev 1.3
- Fuente 5v 3a
- Wifi (para ssh)

Computadora cliente
- Windows o Mac OS X
- Wifi (misma red que la raspi)

Software Adicional
- Detector de movimiento basado picam.py en http://thezanshow.com/electronics-tutorials/raspberry-pi/tutorial-17
- OSC python https://pypi.org/project/python-osc/
- Resolume arena (en otra PC o MAC en la misma red)

Instalación
- Habilitar la camara luego de conectarla desde raspi-config
- Copiar todos los archivos a un directorio
- Instalar OSC para python 3: pip3 install python-osc
- Editar las lineas 23 a 25 de uMainOSC.py con los datos del receptor (Processing / Resolume) de OSC y el mensaje a enviar. 
- Ejecutar python3 uMainOSC.py en un terminal.
- Utilizar testReciverOSC (sketch en Processing 2) para probar la recepción de mensajes desde la Raspi. Al recibir una detección de movimiento aparecerá un punto rojo, mientras que no detecte aparecera un punto pequeño blanco
