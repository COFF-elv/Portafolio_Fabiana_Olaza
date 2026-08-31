import urequests
import ujson
import time
from time import sleep


#Parte de API
API_URL = "http://10.123.65.1:8080/sensor/data"
#               ↑ IP del ordenador a la red wifi

# Composición del envío del POST 
def enviar_lectura(nivel):
    cos = {
        "sensor":     "microfon",
        "valor":      nivel,
        "unitat":     "amplitud_adc",
        "dispositiu": "esp32_A"
    }
    try:
        resp = urequests.post(
            API_URL,
            data    = ujson.dumps(cos),
            headers = {"Content-Type": "application/json"}
        )
        if resp.status_code == 200:
            dada = ujson.loads(resp.text)
            print("INSERT OK — id:", dada["id"])
        else:
            print("Error HTTP:", resp.status_code)
        resp.close()
    except Exception as err:
        print("Error:", err)
        
        