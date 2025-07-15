# visorcito.py
import matplotlib
matplotlib.use('TkAgg')  # Forzar backend interactivo

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from numpy import sin, cos, radians
import oporto
import time

L = 0.2  # Longitud del péndulo
x0, y0 = 0, 0

fig, ax = plt.subplots()
ax.set_xlim(-L, L)
ax.set_ylim(-L, 0.1)
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

def animate(frame):
    th = oporto.dato_actual
    if th is None:
        return line,

    angle = radians(th)
    x = L * sin(angle)
    y = -L * cos(angle)

    histx.append(x)
    histy.append(y)

    line.set_data([x0, x], [y0, y])
    trace.set_data(histx[-500:], histy[-500:])
    return line, trace

ani = FuncAnimation(fig, animate, interval=50, blit=True)
plt.title("🎯 Péndulo en tiempo real (1 solo brazo)")
plt.show()

