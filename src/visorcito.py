import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from numpy import sin, cos, radians, degrees
import oporto
import time

# -------------------- PARÁMETROS --------------------
L1 = 0.172
L2 = 0.145
m1 = 0.7
m2 = 0.3
g = 9.81

# -------------------- ESTADO INICIAL --------------------
th2 = 0.0
vel2 = 0.0
x0, y0 = 0, 0

# -------------------- FIGURA --------------------
fig, ax = plt.subplots()
ax.set_xlim(-L1 - L2, L1 + L2+0.20)
ax.set_ylim(-L1 - L2, 0.2)
ax.set_aspect('equal')
ax.grid()

line, = ax.plot([], [], 'o-', lw=2)
trace, = ax.plot([], [], 'r-', lw=1)
histx, histy = [], []

# -------------------- TEXTOS --------------------
text_template_energy = "T = {:.3f} J\nV = {:.3f} J"

text_energy = ax.text(0.01, 0.95, '', transform=ax.transAxes, fontsize=10,
                      verticalalignment='top', bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))

text_lagrange = ax.text(0.21, 0.95, '', transform=ax.transAxes, fontsize=8, verticalalignment='top',
                        bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))

lagrange_eq = (
    "Ecuaciones de Lagrange (no resueltas):\n"
    "θ̈₁ = ( -9.81·(2·0.7 + 0.3)·sin(θ₁) - 0.3·9.81·sin(θ₁ - 2θ₂)\n"
    "      - 2·sin(θ₁ - θ₂)·0.3·(θ̇₂²·0.145 + θ̇₁²·0.172·cos(θ₁ - θ₂)) )\n"
    "      / ( 0.172·(2·0.7 + 0.3 - 0.3·cos(2θ₁ - 2θ₂)) )\n"
    "\n"
    "θ̈₂ = ( 2·sin(θ₁ - θ₂)·(θ̇₁²·0.172·(0.7 + 0.3) + 9.81·(0.7 + 0.3)·cos(θ₁)\n"
    "      + θ̇₂²·0.145·0.3·cos(θ₁ - θ₂)) )\n"
    "      / ( 0.145·(2·0.7 + 0.3 - 0.3·cos(2θ₁ - 2θ₂)) )"
)

text_lagrange.set_text(lagrange_eq)

# -------------------- ESPERA PRIMER DATO --------------------
print("⏳ Esperando primer dato...")
while oporto.dato_actual is None:
    time.sleep(0.1)
print("✅ Dato recibido, iniciando visualización.")

# -------------------- ANIMACIÓN --------------------
def animate(frame):
    global th2, vel2

    th1_deg = oporto.dato_actual
    if th1_deg is None:
        return line, trace, text_energy, text_lagrange

    #Angulo en radianes para operar
    th1 = radians(th1_deg)

    #Posición en x,y del primer péndulo
    x1 = L1 * sin(th1)
    y1 = -L1 * cos(th1)
    
    #50ms para una animación de 20fps
    dt = 0.05

    #Torque
    torque = -m2 * g * L2 * sin(th2) + 0.3 * sin(th1 - th2)
    #Momento de Inercia
    inertia = m2 * L2**2
    #Segunda Ley de Newton
    acc2 = torque / inertia

    #Integrar la aceleración angular para obtener velocidad angular
    vel2 += acc2 * dt
    #Establecer la fricción 0.7 para que finalice como el modelo real
    vel2 *= 0.93
    #Integrar la velocidad angular para llamar el desplazamiento angular
    th2 += vel2 * dt
    
    #Calcular la posición en base a
    x2 = x1 + L2 * sin(th2)
    y2 = y1 - L2 * cos(th2)

    #Velocidades angulares
    vx1 = L1 * vel2 * cos(th1)
    vy1 = L1 * vel2 * sin(th1)
    vx2 = vx1 + L2 * vel2 * cos(th2)
    vy2 = vy1 + L2 * vel2 * sin(th2)
    
    #Energía cinética tota
    T = 0.5 * m1 * (vx1**2 + vy1**2) + 0.5 * m2 * (vx2**2 + vy2**2)
    #Energía potencial total
    V = m1 * g * y1 + m2 * g * y2

    text_energy.set_text(text_template_energy.format(T, V))

    histx.append(x2)
    histy.append(y2)
    line.set_data([x0, x1, x2], [y0, y1, y2])
    trace.set_data(histx[-500:], histy[-500:])

    return line, trace, text_energy, text_lagrange

ani = FuncAnimation(fig, animate, interval=50, blit=True)
plt.title("🎯 Péndulo doble con energía y Lagrange (visual)")
plt.show()

