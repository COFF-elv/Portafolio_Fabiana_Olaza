import network
from time import sleep
import time


#Conexion a red WIFI
def conectar_wifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('connecting to network...')
        wlan.connect('XFJK', 'hollymybaby')
        while not wlan.isconnected():
            print('loading...')
            print(wlan.status())
            time.sleep(1)
    print('WIFI OK -> network config:', wlan.ifconfig())