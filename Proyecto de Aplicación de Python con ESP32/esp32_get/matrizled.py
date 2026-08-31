#Importa la libreria max7219 para poder comunicarse
import max7219
#Importa herramientas del ESP32, Pin(pines fisicos) y SPI(sistema de comunicacion con la matriz)
from machine import Pin, SPI
from time import sleep
#SPI(1) usa el bus 1 del ESP32 para comunicar, velocidad de envío 10MHz
#Polarity-phase es como se sincronizan los datos, sck es el reloj para leer cada bit, mosi donde viajan los bits 0 y 1

spi = SPI(1, baudrate=10000000, polarity=0, phase=0, sck=Pin(18), mosi=Pin(23))

# Chip select en el Pin 5 para comunicar con la matriz
cs = Pin(5, Pin.OUT)

#Union de todas las definiciones y 1 de cantidad de matrices
display = max7219.Matrix8x8(spi, cs, 1)

def small_heart():
    display.fill(0)
    display.show()

    display.brightness(5)
    #Lo que se mostrará(caracter, posicion, encendido)
    # Corazón pequeño (x,y,1)
    display.pixel(1,1,1)
    display.pixel(2,1,1)
    display.pixel(3,1,1)
            
    display.pixel(1,2,1)
    display.pixel(2,2,1)
    display.pixel(3,2,1)
    display.pixel(4,2,1)

    display.pixel(2,3,1)
    display.pixel(3,3,1)
    display.pixel(4,3,1)
    display.pixel(5,3,1)

    display.pixel(2,4,1)
    display.pixel(3,4,1)
    display.pixel(4,4,1)
    display.pixel(5,4,1)

    display.pixel(1,5,1)
    display.pixel(2,5,1)
    display.pixel(3,5,1)
    display.pixel(4,5,1)

    display.pixel(1,6,1)
    display.pixel(2,6,1)
    display.pixel(3,6,1)
                
    display.show()
                
def big_heart():        
    # Corazón grande(x,y,1)
    display.brightness(0)
        
    display.pixel(1,0,1)
    display.pixel(2,0,1)
    display.pixel(3,0,1)
    display.pixel(4,0,1)

        
    display.pixel(0,1,1)
    display.pixel(1,1,1)
    display.pixel(2,1,1)
    display.pixel(3,1,1)
    display.pixel(4,1,1)
    display.pixel(5,1,1)

        
    display.pixel(0,2,1)
    display.pixel(1,2,1)
    display.pixel(2,2,1)
    display.pixel(3,2,1)
    display.pixel(4,2,1)
    display.pixel(5,2,1)
    display.pixel(6,2,1)


    display.pixel(1,3,1)
    display.pixel(2,3,1)
    display.pixel(3,3,1)
    display.pixel(4,3,1)
    display.pixel(5,3,1)
    display.pixel(6,3,1)
    display.pixel(7,3,1)

        
    display.pixel(1,4,1)
    display.pixel(2,4,1)
    display.pixel(3,4,1)
    display.pixel(4,4,1)
    display.pixel(5,4,1)
    display.pixel(6,4,1)
    display.pixel(7,4,1)
        

    display.pixel(0,5,1)
    display.pixel(1,5,1)
    display.pixel(2,5,1)
    display.pixel(3,5,1)
    display.pixel(4,5,1)
    display.pixel(5,5,1)
    display.pixel(6,5,1)


    display.pixel(0,6,1)
    display.pixel(1,6,1)
    display.pixel(2,6,1)
    display.pixel(3,6,1)
    display.pixel(4,6,1)
    display.pixel(5,6,1)
        
    display.pixel(1,7,1)
    display.pixel(2,7,1)
    display.pixel(3,7,1)
    display.pixel(4,7,1)
            
    display.show()




def off_matriz():
    display.fill(0)
    display.show()