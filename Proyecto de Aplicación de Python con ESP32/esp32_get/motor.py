from machine import Pin,PWM
import time
from time import sleep

# Se define el LED y el PIN
led = Pin(32, Pin.OUT)
# Se confira el PWM en el PIN donde se conectara el servo
servo = PWM(Pin(21))
servo.freq(50) # Se configura la frecuencia a la que trabaja normalmente el servo

#Funcion para que el servo se mueva de (0 a 180) grados
def posicion(energia):
    # Convierte los grados en señal PWM para que el servo entienda y se mueva
    # Se divide entre 180 como valor maximo usado y se convertira en porcentaje para el calculo de la señal PWM

    led.value(0)
    
    if energia < 25:
        angulo = 0
    elif energia <= 50:
        angulo = 50
    elif energia < 100 :
        angulo = 130
    else:
        if energia == 100:
            led.value(1)
            angulo = 180
            
    duty = int((angulo / 180) * 115 + 26) # rango minimo(26), rango maximo(115) ajustable de señal PWM
    servo.duty(duty) # Se envia la señal PWM al servo