import time
from time import sleep
from machine import Pin, ADC


#Parte de lectura del sensor
#Lectura de datos con sensor
mic = ADC(Pin(34))
mic.atten(ADC.ATTN_11DB)       #Full range: 3.3v , range 0-4095 ADC
mic.width(ADC.WIDTH_12BIT)

class SensorAudio:
    
    def __init__(self):
        # Valor inicial del filtro
        self.nivel_filtrado = 0

        # Basado en lecturas crudas
        self.MIN = 200 # silencio aproximado/ruido bajo
        self.MAX = 3000 # música fuerte
        
    # Uso del EMA() para hacer las lecturas mas precisas sin saltos bruscos y mejorar la precision de la lectura
    # Calibración de la lectura para graduarla de 0-100 en 4 estados
    def leer_nivel(self, muestras=100):
        #Primeras 100 muestras para analizar el cambio del sonido
        valors = [mic.read() for _ in range(muestras)]
        amplitud = max(valors) - min(valors) # De la lista busca el max y min para calculalr la diferencia
        
        # Eliminar ruido base
        if amplitud < self.MIN:
            amplitud = 0
            
        #Convertir a escala 0-100
        nivel_actual = (amplitud - self.MIN) / (self.MAX - self.MIN) * 100

        #Limitar el rango
        if nivel_actual < 0:
            nivel_actual = 0
        elif nivel_actual > 100:
            nivel_actual = 100
        
        # Aplicacion del filtro EMA, se utiliza 0.7 y 0.3 para calibrar los cambios ente el anterior y el nuevo resultado
        self.nivel_filtrado = (nivel_actual * 0.7) + (self.nivel_filtrado * 0.3) 
        
        #Se convierte a int por si el resultado anterior es decimal
        nivel_final = int(self.nivel_filtrado)
        
        return nivel_final

