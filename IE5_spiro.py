
# importamos Libreria Tortuga 
import turtle
from turtle import Screen, Turtle

tt = turtle
# Definimos color de fondo.
# Definimos grosor de linia .
# Definimos velocidad.
bg = int(input("Define color de fondo: 1=Blanco, 2=Negro: "))
gr = int(input("Dedine grosor de línea entre 1 y 5: "))
vel = int(input ("Define velocidad: 10, 50 o 100: "))
fig = int(input("Elige figura: 1.Circulo o 2.Pentagono: "))
rad = int(input("Entra el valor del radio o del lado: "))

#dibujamos
if bg == 1:
    tt.bgcolor('white')
else:
    tt.bgcolor('black')

tt.pensize(gr)
tt.speed(vel)


if fig == 1:
    for i in range(6):
   
          # Patron de colores
        for color in ('red', 'magenta', 'blue',
                      'cyan', 'green', 'white',
                      'yellow'):
            tt.color(color)
         
            # Dibuja un circulo de radio escogido
            tt.circle(rad)
         
            # Desplazamos 10 pixels 
            tt.left(10)
     
        # Escondemos el cursor
        tt.hideturtle()

else:
    for i in range(6):
   
          #patron de colores
        for color in ('red', 'magenta', 'blue',
                      'cyan', 'green', 'white',
                      'yellow'):
            tt.color(color)
         
            # Draw a circle of chosen size, 100 here
            tt.right(126)

            # Empezamos a trazar el dibujo.
            tt.pendown()
            tt.forward(rad)
            tt.right(72)
            tt.forward(rad)
            tt.right(72)
            tt.forward(rad)
            tt.right(72)
            tt.forward(rad)
            tt.right(72)
            tt.forward(rad)
            # desplazamos 10 pixels
            tt.left(10)
        # Escondemos el cursor
        tt.hideturtle()


pantalla = Screen()
#definimos la ventana

pantalla.setup(500,500)
pantalla.screensize(475,475)
#finalizamos la ejecución de la aplicación haciendo clic
pantalla.exitonclick()

