import os
from math import pi, sqrt
import turtle
from turtle import Screen, Turtle

def main():
    #os.system ("clear")
    opcion = '0'
    while opcion == '0':
        print("Elige una opción de menú:")
        print("Elige 1 para Operaciones con Circulos")
        print("Elige 2 para Operaciones con Cuadrados")
        print("Elige 3 para Operaciones con Triangulos Equilateros")
              
        opcion = input ("Haz tu elección: ")

        if opcion == "1":
            print ("Escogistes Circulo")
            menu_circulo ()
        elif opcion == "2":
            print ("Escogiste Cuadrado")
            menu_cuadrado ()
        elif opcion == "3":
            print ("Escogiste Triangulo")
            menu_triangulo ()
        else:
            print("Selección no válida. Vuelve a intertarlo.")
            main()

def menu_circulo():
    #limpiamos pantalla
    os.system ("clear")
    #definición de funciones que calculan
    def area_circulo(radio):
        A = pi*radio**2
        return A
    def perimetro_circulo(radio):
        P = 2 * pi * radio
        return P
    def dibujar_circulo(radio):
          
        #configuramos tortuga
        tt=turtle
        tt.bgcolor('black')
        tt.speed(100)
        tt.pensize(1)
        tt.color('red')
        tt.circle(radio)
        tt.hideturtle()

        #creamos la pantalla 
        pantalla = Screen()
        #definimos la ventana
        pantalla.setup(500,500)
        pantalla.screensize(475,475)
        #finalizamos la ejecución de la aplicación haciendo clic
        pantalla.exitonclick()

        main()

    #estructura del menú para escoger la función a calcular
    opcion_circulo = '0'
    radio = float(input("Introduce el radio del circulo: "))
    while opcion_circulo == '0':
        print("Menú de operaciones con Circulos")
        print("Opcion 1. Calcula el Área")
        print("Opcion 2. Calcula el Perímetro")
        print("Opcion 3. Dibuja el Circulo")

        opcion_circulo = input ("Haz tu elección: ")

        if opcion_circulo == "1":
            os.system ("clear")
            print ("Escogiste Calcular el Area")
            area = float(area_circulo (radio))
            print (f"El área de un circulo de radio {radio} es {round(area,2)}")

        elif opcion_circulo == "2":
            os.system ("clear")
            print ("Escogiste Calcular el Perímetro")
            perimetro_circulo (radio)
            perimetro = float(perimetro_circulo(radio))
            print (f"El perímetro de un circulo de radio {radio} es {round(perimetro,2)} ")

        elif opcion_circulo == "3":
            os.system ("clear")
            print ("Dibujar un Circulo")
            dibujar_circulo (radio)

        else:
            print("Selección no válida. Vuelve a intertarlo.")
            

    #volvemos a la función principal
    main()

def menu_cuadrado():
    #limpiamos pantalla
    os.system ("clear")
    #definición de funciones que calculan
    def area_cuadrado(lado):
        A = lado*lado
        return A
    def perimetro_cuadrado(lado):
        P = lado * 4
        return P
    def dibujar_cuadrado(lado):
          
        #configuramos tortuga
        tt=turtle
        tt.bgcolor('black')
        tt.speed(100)
        tt.pensize(1)
        tt.color('red')
        tt.left(90)
        tt.forward(lado)
        tt.left(90)
        tt.forward(lado)
        tt.left(90)
        tt.forward(lado)
        tt.left(90)
        tt.forward(lado)
        tt.left(90)
        tt.hideturtle()

        #creamos la pantalla 
        pantalla = Screen()
        #definimos la ventana
        pantalla.setup(500,500)
        pantalla.screensize(475,475)
        #finalizamos la ejecución de la aplicación haciendo clic
        pantalla.exitonclick()

        main()
    
    #estructura del menú para escoger la función a calcular
    opcion_cuadrado = '0'
    lado = float(input("Introduce el lado del cuadrado: "))
    while opcion_cuadrado == '0':
        print("Menú de operaciones con Cuadrados")
        print("Opcion 1. Calcula el Área")
        print("Opcion 2. Calcula el Perímetro")
        print("Opcion 3. Dibuja el Cuadrado")

        opcion_cuadrado = input ("Haz tu elección: ")

        if opcion_cuadrado == "1":
            os.system ("clear")
            print ("Escogiste Calcular el Area")
            area = float(area_cuadrado (lado))
            print (f"El área de un cuadrado de lado {lado} es {round(area,2)}")

        elif opcion_cuadrado == "2":
            os.system ("clear")
            print ("Escogiste Calcular el Perímetro")
            perimetro_cuadrado (lado)
            perimetro = float(perimetro_cuadrado(lado))
            print (f"El perímetro de un cuadrado de lado {lado} es {round(perimetro,2)} ")

        elif opcion_cuadrado == "3":
            os.system ("clear")
            print ("Dibujar un Cuadrado")
            dibujar_cuadrado (lado)

        else:
            print("Selección no válida. Vuelve a intertarlo.")
            

    #volvemos a la función principal
    main()

  
def menu_triangulo():
    #limpiamos pantalla
    os.system ("clear")
    #definición de funciones que calculan
    def area_triangulo(base,altura):
        A = (base*altura)/2
        return A
    def perimetro_triangulo(base):
        P = 3 * base
        return P
    def dibujar_triangulo(base):
          
        #configuramos tortuga
        tt=turtle
        tt.bgcolor('black')
        tt.speed(100)
        tt.pensize(1)
        tt.color('red')
        tt.left(120)
        tt.forward(base)
        tt.left(120)
        tt.forward(base)
        tt.left(120)
        tt.forward(base)
        tt.hideturtle()

        #creamos la pantalla 
        pantalla = Screen()
        #definimos la ventana
        pantalla.setup(500,500)
        pantalla.screensize(475,475)
        #finalizamos la ejecución de la aplicación haciendo clic
        pantalla.exitonclick()

        main()

    #estructura del menú para escoger la función a calcular
    opcion_triangulo = '0'
    base = float(input("Introduce la base del triangunlo equilátero: "))
    altura = float(base *(sqrt(3)/2))
    while opcion_triangulo == '0':
        print("Menú de operaciones con Triangulos")
        print("Opcion 1. Calcula el Área")
        print("Opcion 2. Calcula el Perímetro")
        print("Opcion 3. Dibuja el triangulo")

        opcion_triangulo = input ("Haz tu elección: ")

        if opcion_triangulo == "1":
            os.system ("clear")
            print ("Escogiste Calcular el Area")
            area = float(area_triangulo (base,altura))
            print (f"El área de un triangulo de base {base} es {round(area,2)}")

        elif opcion_triangulo == "2":
            os.system ("clear")
            print ("Escogiste Calcular el Perímetro")
            #perimetro_triangulo (base)
            perimetro = float(perimetro_triangulo(base))
            print (f"El perímetro de un triangulo de base {base} es {round(perimetro,2)} ")

        elif opcion_triangulo == "3":
            os.system ("clear")
            print ("Dibujar un triangulo")
            dibujar_triangulo (base)

        else:
            print("Selección no válida. Vuelve a intertarlo.")
            

    #volvemos a la función principal
    main()

main()
