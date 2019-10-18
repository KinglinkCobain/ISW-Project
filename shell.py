"""
Analisis de algoritmos

Fecha: Miercoles 25 de septiembre del 2019
Autores: Aguilar Morales marco, Torres Rosas Ricardo Erick
Email: marcoaguilarm8@gmail.com, rtorresr1500@alumno.ipn.mx
Descripcion: implementacion del algoritmo ShellSort

"""


from random import *

#nuestra variable global
tiempo=0

#Algoritmo ShellSort
def shellSort(arr,n): 
  
    # Empezamos dividiendo el tamano del arreglo entre 2
    global tiempo
    tiempo+=1

    distancia = n//2
    
    # El algoritmo empieza con la condicion de que el la distancia entre las comparaciones sea de 0
    tiempo+=1
    while distancia > 0: 
        tiempo+=1
        for i in range(distancia,n): 
  
            # Guardamos el valor de la posicion i del arreglo en una variable temporal
            tiempo+=1
            temp = arr[i] 
            tiempo+=1
            j = i 
            tiempo+=1

            while  j >= distancia and arr[j-distancia] >temp:
                tiempo+=1 
            
                arr[j] = arr[j-distancia]
                tiempo+=1
                j -= distancia 
            tiempo+=1
            arr[j] = temp
            tiempo+=1 
        distancia //= 2
  


arr = []

for i in range(0,10):
#    arr.append(randint(1,10)) #Aleatorio
#    arr.append(i) #MEJOR CASO
    arr.append(10-i) #PEOR CASO
print("Arreglo antes de ordenar")
print(arr[:])

n = len(arr) 
tiempo
shellSort(arr,n) 
  
print ("\nArreglo despues de ordenar") 
print(arr[:])
print("Tiempo de ejecucion: ", tiempo)

#Tiempos de ejecucion:
#Mejor caso: 2,2,8,13,29,39,44,54,90,105,115
#Peor caso: 2,2,10,19,37,47,62,68,114,121,141