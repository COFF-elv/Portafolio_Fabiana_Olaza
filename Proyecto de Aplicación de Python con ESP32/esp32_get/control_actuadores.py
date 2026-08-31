from time import sleep
import time
import showled
import matrizled
import motor

def switch(estado, nivel, energia):
    motor.posicion(energia)
    if (estado == "chill") and (nivel <= 25):
        showled.estado_chill()
        sleep(0.4)
        showled.off_led()
        sleep(0.1)
        
        showled.estado_chill()
        matrizled.small_heart()
        sleep(0.4)
        
        
        matrizled.off_matriz()
        sleep(0.2)
        showled.off_led()
        
        matrizled.small_heart()
        sleep(0.4)
        showled.estado_chill()
        
        matrizled.off_matriz()
        sleep(0.2)
        showled.off_led()
        
        showled.estado_chill()
        matrizled.big_heart()
        sleep(0.2)
        
        
        matrizled.off_matriz()
        showled.off_led()
        
        showled.estado_chill()
        sleep(0.4)
        showled.off_led()
        
    elif (estado == "flow") and (25 < nivel <= 50):
        showled.estado_flow()
        sleep(0.3)
        showled.off_led()
        sleep(0.1)
        
        showled.estado_flow()
        matrizled.small_heart()
        sleep(0.3)
        
        
        matrizled.off_matriz()
        sleep(0.15)
        showled.off_led()
        
        matrizled.small_heart()
        sleep(0.3)
        showled.estado_flow()
        
        matrizled.off_matriz()
        sleep(0.15)
        showled.off_led()
        
        showled.estado_flow()
        matrizled.big_heart()
        sleep(0.15)
        
        
        matrizled.off_matriz()
        showled.off_led()
        
        showled.estado_flow()
        sleep(0.3)
        showled.off_led()

    elif (estado == "rush") and (50 < nivel <= 75):
        showled.estado_rush()
        sleep(0.2)
        showled.off_led()
        sleep(0.1)
        
        showled.estado_rush()
        matrizled.small_heart()
        sleep(0.2)
        
        
        matrizled.off_matriz()
        sleep(0.15)
        showled.off_led()
        
        matrizled.small_heart()
        sleep(0.2)
        showled.estado_rush()
        
        matrizled.off_matriz()
        sleep(0.1)
        showled.off_led()
        
        showled.estado_rush()
        matrizled.big_heart()
        sleep(0.1)
        
        
        matrizled.off_matriz()
        showled.off_led()
        
        showled.estado_rush()
        sleep(0.2)
        showled.off_led()

    elif (estado == "euphoria") and (75 < nivel <= 100):
        showled.estado_euphoria()
        sleep(0.15)
        showled.off_led()
        sleep(0.1)
        
        showled.estado_euphoria()
        matrizled.small_heart()
        sleep(0.15)
        
        
        matrizled.off_matriz()
        sleep(0.1)
        showled.off_led()
        
        matrizled.small_heart()
        sleep(0.15)
        showled.estado_euphoria()
        
        matrizled.off_matriz()
        sleep(0.1)
        showled.off_led()
        
        showled.estado_euphoria()
        matrizled.big_heart()
        sleep(0.1)
        
        
        matrizled.off_matriz()
        showled.off_led()
        
        showled.estado_euphoria()
        sleep(0.15)
        showled.off_led()
        
    else:
        if estado is None and nivel is None:
            showled.off_led()
            matrizled.off_matriz()
            print("Probemas con API")
     
    