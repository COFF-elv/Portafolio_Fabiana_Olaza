# main_A.py — ESP32_A (POST & SENSOR)
import time
from time import sleep
from wifi import conectar_wifi
from api_post import enviar_lectura
from sensor_sonido import SensorAudio

sensor = SensorAudio()
# Llamar a la función para conectar el ESP32_A a la red        
conectar_wifi()
# Por cada lectura recibida será enviada en un POST al API
while True:
    nivel = sensor.leer_nivel()
    print("Nivel:", nivel)
    enviar_lectura(nivel)
    time.sleep(0.2)