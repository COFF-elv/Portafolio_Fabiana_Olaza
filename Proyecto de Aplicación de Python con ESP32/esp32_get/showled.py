from machine import Pin, PWM
from time import sleep
import random

# tipo de led RGB: catodo comun, definicion de PIN para los LEDs
r1 = PWM(Pin(27))
g1 = PWM(Pin(26))
b1 = PWM(Pin(25))

r2 = PWM(Pin(13))
g2 = PWM(Pin(12))
b2 = PWM(Pin(14))

#estado recibido a traves de GET desde el API
# CHILL, FLOW, RUSH, EUPHORIA
# Condicion de cambio de estados
# LED RGB catodo -> 1 encendido, 0 apagado

def off_led():
    r1.duty_u16(0)
    g1.duty_u16(0)
    b1.duty_u16(0)

    r2.duty_u16(0)
    g2.duty_u16(0)
    b2.duty_u16(0)
            
def estado_chill():
    r1.duty_u16(45000)
    g1.duty_u16(12000)
    b1.duty_u16(65535)

    r2.duty_u16(45000)
    g2.duty_u16(12000)
    b2.duty_u16(65535)

def estado_flow():
    r1.duty_u16(65535)
    g1.duty_u16(42000)
    b1.duty_u16(0)

    r2.duty_u16(65535)
    g2.duty_u16(42000)
    b2.duty_u16(0)
    
def estado_rush():
    r1.duty_u16(65535)
    g1.duty_u16(18000)
    b1.duty_u16(0)
    
    r2.duty_u16(65535)
    g2.duty_u16(18000)
    b2.duty_u16(0)


def estado_euphoria():
    valor_r1 = random.randint(0, 65535)
    valor_g1 = random.randint(0, 65535)
    valor_b1 = random.randint(0, 65535)

    valor_r2 = random.randint(0, 65535)
    valor_g2 = random.randint(0, 65535)
    valor_b2 = random.randint(0, 65535)
                     
    r1.duty_u16(valor_r1)
    g1.duty_u16(valor_g1)
    b1.duty_u16(valor_b1)

    r2.duty_u16(valor_r2)
    g2.duty_u16(valor_g2)
    b2.duty_u16(valor_b2)
