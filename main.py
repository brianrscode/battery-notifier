import time
import psutil
from plyer import notification


try:
    while True:
        # Obtenemos el porcentaje actual de la batería
        currentBattery = psutil.sensors_battery().percent
        # Obtenemos el porcentaje actual de la batería
        isCharging = psutil.sensors_battery().power_plugged

        # Si el porcentaje actual de batería es menor o igual a 20 y si el equipo no está cargando
        if currentBattery <= 20 and isCharging == False:
            title = "Nivel de batería bajo"
            message = f'El nivel de batería es {currentBattery}%'
            # Lanzamos la notificación, incluyendo un ícono personalizado de la batería
            notification.notify(title=title, message=message, app_icon="battery.ico")
        # Hacemos una pausa en la ejecución del programa por 10 segundos
        time.sleep(10)
# En caso de ocurrir una excepción, la ignoramos y terminamos la ejecución
except:
    pass