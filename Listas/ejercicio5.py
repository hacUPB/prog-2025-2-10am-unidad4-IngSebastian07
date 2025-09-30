'''
Generar una lista con 100 números aleatorios entre 100 y 1000.
Calcular el promedio de los valores de la lista.
Calcular el mayor y el menor de los números.
'''

import random

#Lista numérica.

numeros = []
for i in range (100):
    aleatorio = random.randint(100,1000)
    numeros.append(aleatorio)

sumatoria = 0
promedio = 0

for i in range(len(numeros)):
    sumatoria += numeros[i]
    promedio += sumatoria / len(numeros)
print (f"La sumatoria de todos los números es de {sumatoria}. El promedio de esos números es de {promedio:0.3f}")

menor = min(numeros)
mayor = max(numeros)

print (f"El mayor de los números en la lista es {mayor}, el menor de los números es {menor}")