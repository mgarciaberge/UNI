#grafic.py
from turtle import Screen, Turtle

pantalla = Screen()

# Definimos tamaño y margen interior de la pantalla de visualización.
pantalla.setup(500,500)
pantalla.screensize(475,475)

tortuga = Turtle()

# Posicionamos el puntero de la tortuga en el punto inicial del dibujo
tortuga.left(90)
tortuga.penup()
tortuga.forward(100)

# Giramos el puntero con el angulo correcto para inciar el trazo y dejar el poligono centrado
# angulo interior del pengano 108º angulo exterior 72 - al primer giro de 90 le sumamos 36 (angulo de partida de 126º)
# para poder centrar el poligono en el centro de la pantalla
tortuga.right(126)

# Empezamos a trazar el dibujo.
tortuga.pendown()
tortuga.forward(100)
tortuga.right(72)
tortuga.forward(100)
tortuga.right(72)
tortuga.forward(100)
tortuga.right(72)
tortuga.forward(100)
tortuga.right(72)
tortuga.forward(100)

#finalizamos la ejecución de la aplicación haciendo clic
pantalla.exitonclick()


