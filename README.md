# Spoiler
Este proyecto después de ser un trabajo presentado en un curso, lo estoy intentando tomar como un pasatiempo para que sea mucho mejor.
Preferentemente espere la siguiente versión para utilizar.
# Péndulo Doble Caótico - Simulación y Visualización
Simulación computacional en tiempo real de un péndulo doble con datos de sensores reales, enfocada en el estudio del movimiento caótico y sus posibles aplicaciones en ¿robótica?.
# Objetivos del proyecto
- Usar datos reales del sensour MPU6050 vía Arduino.
- Visualizar el comportamiento caótico de un péndulo doble.
- Explorar aplicaciones futuras en no sé que campos.
# Motivación
Simple curiosidad.
# Estructura del proyecto
# Instalación
## Usuario
Si quieres conectar tu microcontrolador con el sensor MPU6050 (supongo en una maqueta), debes hacer lo siguiente para ejecutar esto:
### 1. Colocar el sensor MPU6050 en el primer pédulo
### 2. Conectar el sensor a un microcontrolador Arduino UNO
### 3. Clonar este repositorio con git en la carpeta de su preferencia (o descargar el zip, forma no tan recomendable)
git clone https://github.com/diegocsz/pendulo-doble.git
cd pendulo-doble
### 3. Tener instalado python3
pip install .
### 4. Descargar Arduino IDE y abrir dentro del proyecto el archivo en /arduino/angulo/angulo.ino
Subir el código al microcontrolador y anotar el puerto USB (Por ejm en Windows "COM3" o en Linux "/dev/ttyACM0"), luego obligatoriamente cerrar Arduino IDE.
### 5. Abrir el archivo /src/oporto,py
Aquí cambiar la parte de "puerto='/dev/ttyACM0'", cambiar '/dev/ttyACM0' por su puerto (por ejm sería 'COM3' y otro COM en Windows) y guardar
### 6. Ejecutar
Entrar a src y con el comando "python3 visorcito.py" por fin podrá ejecutarlo.
## Colaboradores
Si usted desea colaborar al proyecto se tendrá que esperar a la siguiente versión
# Uso
# Fundamentos científicos
# Futuro
# Licencia
# Créditos
Grupo de Mecánica Clásica ciclo 3 de la Universidad Tecnológica del Perú.
Especialmente a la compañera que sugirió el tema y sin ella no habría sido posible nada del presente proyecto ni tendría las ganas de seguir mejorándolo.
# Tareas
- Documentar y mejorar.
- Cambiar de lugar el sensor al segundo péndulo para mayor eficiencia.
- Calcular las ecuaciones de movimiento.
- Crear una gráfica predictiva del movimiento en tiempo real.
