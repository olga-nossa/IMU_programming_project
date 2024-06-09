import serial
import numpy as np
import matplotlib as plt
from matplotlib.animation import FuncAnimation

# Configura el puerto serie
ser = serial.Serial('/dev/ttyACM0', 115200)
ser.flushInput()

fig, (ax1, ax2) = plt.subplots(2, 1)

data = {
    "ax": [],
    "ay": [],
    "az": [],
    "gx": [],
    "gy": [],
    "gz": []
}

def update(frame):
    line = ser.readline().decode('utf-8').rstrip()
    ax, ay, az, gx, gy, gz = map(int, line.split(','))
    data["ax"].append(ax)
    data["ay"].append(ay)
    data["az"].append(az)
    data["gx"].append(gx)
    data["gy"].append(gy)
    data["gz"].append(gz)
    
    # Mantén solo los últimos 100 datos para un gráfico en tiempoo real
    if len(data["ax"]) > 100:
        for key in data:
            data[key].pop(0)
    
    # Limpiar y actualizar las gráficas
    ax1.cla()
    ax2.cla()
    
    ax1.plot(data["ax"], label="ax")
    ax1.plot(data["ay"], label="ay")
    ax1.plot(data["az"], label="az")
    
    ax2.plot(data["gx"], label="gx")
    ax2.plot(data["gy"], label="gy")
    ax2.plot(data["gz"], label="gz")
    
    ax1.legend(loc='upper left')
    ax2.legend(loc='upper left')
    

#
# try:
#     while True:
#         if ser.in_waiting > 0:
#             line = ser.readline().decode('utf-8').rstrip()
#             #Yaw, Pitch, Roll, ax, ay, az, gx, gy, gz
#             print(line)  # Imprime la cadena recibida
# except KeyboardInterrupt:
#     print("Interrupción del usuario. Cerrando.")
# finally:
#     ser.close()
