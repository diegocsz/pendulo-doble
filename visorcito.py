# visorcito.py
import matplotlib
matplotlib.use('TkAgg')  # Forzar backend interactivo

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from numpy import sin, cos, radians
import oporto
import time

L1 = 0.2   # Longitud del primer brazo
L2 = 0.15  # Longitud del segundo brazo
x0, y0 = 0, 0

fig, ax = plt.subplots()
ax.set_xlim(-L1 - L2, L1 + L2)
ax.set_ylim(-L1 - L2, 0.1)
ax.set_aspect('equal')
ax.grid()

line, = ax.plot([], [], 'o-', lw=2)
trace, = ax.plot([], [], 'r-', lw=1)
histx, histy = [], []

# Esperar primer dato
print("⏳ Esperando primer dato...")
while oporto.dato_actual is None:
    time.sleep(0.1)
print("✅ Dato recibido, iniciando visualización.")

# Estado para animar ligeramente el segundo péndulo
angulo2 = 0
velocidad2 = 0

def animate(frame):
    global angulo2, velocidad2

    th1 = oporto.dato_actual
    if th1 is None:
        return line,

    # Primer péndulo
    angle1 = radians(th1)
    x1 = L1 * sin(angle1)
    y1 = -L1 * cos(angle1)

    # Simular oscilación inducida del segundo péndulo
    # Simple dinámica: el segundo péndulo se "arrastra" con retardo
    objetivo = angle1  # dirección hacia donde quiere ir
    velocidad2 += 0.05 * (objetivo - angulo2)  # aceleración proporcional
    velocidad2 *= 0.95  # fricción
    angulo2 += velocidad2

    x2 = x1 + L2 * sin(angulo2)
    y2 = y1 - L2 * cos(angulo2)

    histx.append(x2)
    histy.append(y2)

    line.set_data([x0, x1, x2], [y0, y1, y2])
    trace.set_data(histx[-500:], histy[-500:])
    return line, trace

ani = FuncAnimation(fig, animate, interval=50, blit=True)
plt.title("🎯 Péndulo doble en tiempo real (con oscilación dependiente)")
plt.show()
