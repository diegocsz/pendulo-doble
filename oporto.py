# oporto.py
import serial
import threading
import time

dato_actual = None

def leer_serial(puerto='/dev/ttyACM0', baudios=57600):
    global dato_actual
    try:
        arduino = serial.Serial(puerto, baudios, timeout=1)
        print(f"📡 Conectado al puerto: {puerto}")
    except serial.SerialException as e:
        print(f"❌ No se pudo abrir el puerto: {e}")
        return

    while True:
        if arduino.in_waiting:
            try:
                linea = arduino.readline().decode('utf-8').strip()
                if linea:
                    dato_actual = float(linea)
            except (ValueError, UnicodeDecodeError):
                continue

threading.Thread(target=leer_serial, daemon=True).start()
