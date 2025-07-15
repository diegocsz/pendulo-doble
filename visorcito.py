import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from numpy import sin, cos, radians
import oporto
import time

# Parámetros físicos
L1 = 0.172     # Longitud primer brazo (m)
L2 = 0.145    # Longitud segundo brazo (m)
m1 = 0.7     # Masa primer péndulo (kg)
m2 = 0.3     # Masa segundo péndulo (kg)
g = 9.81     # Gravedad (m/s²)

# Estado inicial
th2 = 0.0               # Ángulo segundo péndulo (rad)
vel2 = 0.0              # Velocidad angular
x0, y0 = 0, 0

fig, ax = plt.subplots()
ax.set_xlim(-L1 - L2, L1 + L2)
ax.set_ylim(-L1 - L2, 0.1)
ax.set_aspect('equal')
ax.grid()

line, = ax.plot([], [], 'o-', lw=2)
trace, = ax.plot([], [], 'r-', lw=1)
histx, histy = [], []

print("⏳ Esperando primer dato...")
while oporto.dato_actual is None:
    time.sleep(0.1)
print("✅ Dato recibido, iniciando visualización.")

def animate(frame):
    global th2, vel2

    th1_deg = oporto.dato_actual
    if th1_deg is None:
        return line,

    # Primer péndulo
    th1 = radians(th1_deg)
    x1 = L1 * sin(th1)
    y1 = -L1 * cos(th1)

    # Segunda masa (modelo simplificado de dinámica)
    dt = 0.05  # paso de tiempo en segundos

    # Aceleración angular inducida al segundo péndulo
    torque = -m2 * g * L2 * sin(th2) + 0.3 * sin(th1 - th2)  # gravedad + arrastre
    inertia = m2 * L2**2
    acc2 = torque / inertia

    vel2 += acc2 * dt
    vel2 *= 0.95  # fricción leve
    th2 += vel2 * dt

    x2 = x1 + L2 * sin(th2)
    y2 = y1 - L2 * cos(th2)

    histx.append(x2)
    histy.append(y2)

    line.set_data([x0, x1, x2], [y0, y1, y2])
    trace.set_data(histx[-500:], histy[-500:])
    return line, trace

ani = FuncAnimation(fig, animate, interval=50, blit=True)
plt.title("🎯 Péndulo doble con gravedad y masa (visual)")
plt.show()
