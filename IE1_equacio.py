#importamos de la libreria math la funcion raiz cuadrada
from math import sqrt

print("Programa para el cálculo de ecuaciones de segundo grado (ax^2 + bx + c)")

a = float(input("Introduce el coeficiente de a: "))
b = float(input("Introduce el coeficiente de b: "))
c = float(input("Introduce el coeficiente de c: "))

#Realizamos los calculos y los asignamos a 2 variables con las soluciones.
sol1 = (-b + sqrt(b**2 - 4*a*c)) / (2*a)
sol2 = (-b - sqrt(b**2 - 4*a*c)) / (2*a)

#formateamos el float para que solo aparezca con 2 decimales y se pueda imprimir como string.
format_sol1 = "{:.2f}".format(sol1)
format_sol2 = "{:.2f}".format(sol2)

#printamos el resultado de las soluciones de dos forma possibles, como string formateado anteriormente:
print ("Las soluciones para la equación de segundo grado son: x1= " + format_sol1 + " i x2= " + format_sol2 )
