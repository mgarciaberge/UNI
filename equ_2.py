#importamos de la libreria math la funcion raiz cuadrada
from curses.ascii import isdigit
from math import sqrt

print("Programa para el cálculo de ecuaciones de segundo grado (ax^2 + bx + c)")

a = float(input("Introduce el coeficiente de a: "))
#if type(a) not in (int, float):
#    print("a debe ser numérico")
b = float(input("Introduce el coeficiente de b: "))
#if type(b) not in (int, float):
#    print("b debe ser numérico")
c = float(input("Introduce el coeficiente de c: "))
#if type(c) not in (int, float):
#    print("c debe ser numérico")

if a != 0:
    disc = b**2 - 4*a*c
    print (disc)
    if disc >= 0:
        sol1 = (-b + sqrt(disc)/(2*a))
        sol2 = (-b - sqrt(disc)/(2*a))
        f_sol1 = "{:.2f}".format(sol1)
        f_sol2 = "{:.2f}".format(sol2)
        if sol1 == sol2:
            print ("La equación tiene una solución: x="+f_sol1)
        else:
            print ("Las soluciones son: x1="+f_sol1+" y x2=" +f_sol2)
    else:
        if b != 0:
            sol = -c/b
            f_sol = "{:.2f}".format(sol)
            print("La ecuación tiene una sola solucion: x="+f_sol)
else:
    if c != 0:
        print("La ecuación no tiene solución.")
    else:
        print("La ecuación tiene infinitas soluciones.")
