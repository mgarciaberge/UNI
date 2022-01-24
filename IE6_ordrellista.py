A=['Manel','manel','Mateu','mmar','alvaro','Mariona','roman','alonso']

#pasamos el Array a minusculas para poder ordenar independientemente del codio Ascii
A=[element.lower() for element in A]

#ordenamos la lista.
for i in range(1,len(A)):
    for j in range(0,len(A)-i):
        if (A[j+1] < A[j]):
            aux=A[j];
            A[j]=A[j+1];
            A[j+1]=aux;

#contamos coincidencias y printamos al lado de cada palabra 
#número de coincidencias mediante la creación de un diccionario.
repeticiones = {}
for n in A:
    if n in repeticiones :
        repeticiones[n] += 1
    else:
        repeticiones[n] = 0
print (repeticiones)




