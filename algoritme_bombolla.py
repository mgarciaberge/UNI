#programa algoritmo de la burbuja. 
#el programa recorre el array n-1 vez comparando entre pares de valores 
#y los ordena.

#orden de complejidad del algoritmo O(n²)

def bombolla(nums):
    #intercambio a True para entrar en el bucle 1 vez como mínimo
    intercambio = True
    while intercambio:
        intercambio = False
        for i in range(len(nums)-1):
            #comprovamos si se deben intercambiar los números
            if nums[i] > nums[i+1]:
                #si se cumple hay que intercambiar los números
                nums[i], nums[i+1] = nums[i+1], nums[i]
                #cambiamos el valor de intercambio a True ya que se ha producido cambio
                intercambio = True

listanumerosrandom = [9,5,3,4,6,2]
bombolla(listanumerosrandom)
print (listanumerosrandom)



