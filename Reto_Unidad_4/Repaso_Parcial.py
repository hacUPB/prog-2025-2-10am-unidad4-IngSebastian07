'''
# REPASO TERCER PARCIAL - PROGRAMACIÓN 2025-2
# De la Unidad 4 se tiene:

# En Python todo es un objeto.
# En Python las variables son etiquetas que apuntan a objetos, no los contienen. 
# La MUTABILIDAD se refiere a objetos que pueden ser modificados después de creados. La INMUTABILIDAD se refiere a objetos que no pueden ser modificados después de creados.
# Algunos ejemplos de objetos mutables: listas, diccionarios, sets.
# Algunos ejemplos de objetos inmutables: números, strings, tuplas.
# Un iterable se refiere a los objetos que permiten recorrer sus elementos uno a uno. 
# Una iteración es el método usado para hacer dicho proceso. Generalmente se utiliza con bucles for, while, entre otros.

# ---LISTAS---
# Las listas son mutables. Tienen la siguiente sintaxis:

lista = [] # Lista vacía.
lista2 = ["B787", "A350", "AN225"] # Lista de aeronaves.

# En las listas, cada elemento tiene una posición asignada. En este caso, se comienza desde el número cero.
# Para acceder a los elementos de la lista, se usa la siguiente indexación:

print(lista2[0]) # Se imprime "B787"
print(lista2[-1]) # Indexación negativa, se imprime el valor anterior al cero.
print(lista[:2]) # Se imprimen los valores desde el cero hasta el dos, sin incluir el dos.
print (lista[0:2]) # Se imprimen desde la posición cero hasta la posición dos, sin incluir la última.


# EJERCICIO.

# Datos de vuelo para un avión comercial
tiempo = [0, 10, 20, 30, 40, 50, 60]  # segundos
altitud = [0, 100, 500, 1000, 1500, 2000, 2200]  # metros
velocidad = [0, 50, 100, 150, 200, 250, 300]  # km/h
estado = ["despegue", "ascenso inicial", "ascenso", "ascenso", "ascenso", "nivelación", "crucero"]

# Se pide realizar un informe general para cada estado de la aeronave. Se sugiere usar la función zip() para tener más de un iterable.

print("---INFORME GENERAL DE LA AERONAVE--- ")
for t, a, v, e in zip(tiempo, altitud, velocidad, estado):
    print(f"Tiempo transcurrido: {t} - Altitud de la aeronave: {a} - Velocidad de la aeronave: {v} - Estado: {e}")

'''
'''
# EJERCICIO 2:

# Lista de componentes con sus masas (kg) y posiciones (m)
componentes = ["motor izquierdo", "motor derecho", "fuselaje", "ala izquierda", "ala derecha", "cola"]
masas = [1200, 1200, 5000, 800, 800, 600]
posiciones_x = [2, 2, 0, -2, 2, -6]

# Se pide calcular el centro de gravedad de la aeronave, teniendo en cuenta el peso registrado para cada componente.
# Recordar: CD = Momento Total / Masa Total

# Calcular masa total.
masa_total = 0
momento_total = 0
for i in range (len(masas)):
    masa_total = masa_total + masas[i]
    momento_total = momento_total + (masas[i] * posiciones_x[i])
print(f"La masa total es {masa_total}")
print(f"El momento total es {momento_total}")

# Calcular centro de gravedad
CG = momento_total/masa_total
print (f"El centro de gravedad está ubicado a {momento_total:0.2f} posiciones en el eje x")
'''
'''
# Ejercicio: Selección de cajas para carga en una aeronave

#En una operación de carga aérea, se tiene una lista de cajas, cada una con un peso diferente. La aeronave tiene un límite máximo de peso que no debe ser superado por la suma de los pesos de las cajas seleccionadas. Debes escribir una función que recorra la lista de pesos de las cajas y agregue cada caja mientras no se exceda el peso máximo permitido. La función debe mostrar en pantalla los índices de las cajas seleccionadas y el peso total cargado.
#Completa el código a continuación utilizando únicamente listas y ciclos:
#Datos: pesos_cajas = [120, 400, 300, 180, 450, 200] - peso_max_avion = 1000

cajas = [120, 400, 300, 180, 450, 200]
peso_max = 1000
peso = 0

for caja in cajas:
    print(f"---VERIFICACIÓN DE PESO---")
    print (f"Peso actual = {peso} Kg.")
    print (f"Peso de la caja = {caja} Kg.")
    if peso + caja <= peso_max:
        print ("Se puede agregar.")
        peso = peso + caja
        print (f"El nuevo peso es {peso} Kg.")
    else:
        print (f"Se supera el peso máximo de {peso_max} Kg.")

# FUNCIONA BIEN :D
'''
'''
# ---TUPLAS--- 
# Tienen alta similitud con las listas. La gran diferencia entre ellas: las listas son mutables, las listas no.
# Otra diferencia es que para crear una lista se usa lista = []. Para una tupla, se usa tupla = ()
# Si la tupla contiene solo un dato, deberá finalizarse con una coma: tupla = (0,)
# Las tuplas se pueden desempaquetar. Primero se enumeran los elementos y luego se iguala al nombre de la tupla.

# Ejemplo de desempaquetado.

Airbus_A350 = ("A350", 410, 16100, 53, "Rolls-Royce Trent XWB", 97000 )
MDL, CTDPSJS, ACC, PCTJ, MTR, EPJ = Airbus_A350
print (f"El {MDL} tiene una capacidad para transportar {CTDPSJS} pasajeros, alcanzando hasta {ACC} Km en un solo viaje. Está hecho con {PCTJ}% de material compuesto y posee unos motores {MTR} que generan {EPJ} libras de empuje. Una obra de arte, sin duda. ")

'''

# ---DICCIONARIOS---
# Se dice que los diccionarios son colecciones no ordenadas porque, a diferencia de las tuplas y las listas, los diccionarios no asignan posiciones a sus elementos.
# Estos, en cambio, funcionan con una clave y un valor, ¡Tal como un diccionario real!

# Ejemplos de diccionarios:
# Diccionario vacío
aeronave = {}

# Diccionario con elementos
aeronave = {
    "modelo": "Boeing 787-9",
    "envergadura": 60.17,  # metros
    "longitud": 62.81,     # metros
    "mtow": 254000,        # kg
    "velocidad_max": 954   # km/h
}

#:D
