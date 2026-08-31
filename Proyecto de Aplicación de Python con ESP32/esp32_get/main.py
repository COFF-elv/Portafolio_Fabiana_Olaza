# main_B.py — ESP32_B (GET & ACTUADORES)
from time import sleep
import time
from wifi import conectar_wifi
from api_get import obtener_estado
import control_actuadores
from machine import Pin,PWM
led =Pin(32,Pin.OUT)
# Llamar a la función para conectar el ESP32_B a la red        
conectar_wifi()
led.value(1)
# Por cada lectura recibida será enviada en un POST al API
while True:
    estado, nivel, energia = obtener_estado()
    if energia is None:
        energia = 0
    control_actuadores.switch(estado, nivel, energia)
    time.sleep(0.1)
    
    