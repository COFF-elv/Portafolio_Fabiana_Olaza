import urequests
import ujson
import time
from time import sleep


#Parte de API
API_URL = "http://10.123.65.1:8080/estado"
#               ↑ IP del ordenador a la red wifi

# Composición del método GET
def obtener_estado():
    try:
        # GET del endpoint del API
        response = urequests.get(API_URL)
        response_code = response.status_code # Estado de la peticion
        if response_code == 200:
            # Convierte la respuesta a un diccionario Python
            data = response.json()
            # Consulta el estado y el nivel de los datos recibidos
            estado = data["estado"]
            nivel = data["nivel"]
            energia = data["energia"]
            print("Estado:", estado)
            print("Nivel:", nivel)
            print("Energía:", energia)
            response.close()
            return estado, nivel, energia
        else:
            print("Error HTTP:", response_code) # Imprime el codigo del error
            response.close() # Cierra la conexion
            return None, None, None
    except Exception as err:
        print("Error:", err) # Si detecta un error lo printa
        return None, None, None
        