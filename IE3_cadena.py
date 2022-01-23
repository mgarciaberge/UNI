#Pedimos al Usuario que introduzca la cadena 
cadena = input("Intruduce una cadena de 5 caracteres del alfabeto: ")

#passamos la cadena a mayusculas
cadena = cadena.upper()

#invertimos los primeros 5 caracteres de la cadena y los almacenamos en una nueva variable
cadena_inv= cadena[5::-1]

#printamos la cadena invertida (5 primeros caracteres) y en mayusculas.
print (cadena_inv)

