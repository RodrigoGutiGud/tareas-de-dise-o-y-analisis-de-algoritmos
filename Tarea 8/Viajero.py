# Realizado por: Rodrigo Gutiérrez Guadarrama
# Grupo: 1561 (2025-1)
# Asignatura: Diseño y Análisis de Algoritmos

#Definimos la función que calcula la distancia total de un recorrido
def calcular_distancia(ruta, distancias):
    distancia_total = 0                                          #Será el objeto que acumulará la distancia total de la ruta
    for i in range(len(ruta) - 1):                               #O(n)
        distancia_total += distancias[ruta[i]][ruta[i+1]]        #Recorre cada par de ciudades consecutivas en la ruta
    
    #Regresa a la ciudad inicial
    distancia_total += distancias[ruta[-1]][ruta[0]]
    return distancia_total                                       #Retorna el valor de las sumas de las distancias

#Definimos la funcion que genera permutaciones de manera recursiva
def generar_permutaciones(ciudades):
    if len(ciudades) == 1:                                       #Si las ciudades presenta un elemento, se retorna unicamente la lista de esa ciudad
        return [ciudades]
    
    permutaciones = []                                           #Definimos el array permutaciones, en donde este almacenará todas las permutaciones generadas del proceso
    for i in range(len(ciudades)):                               #O(n!)
        
        # Separamos una ciudad
        ciudad_actual = ciudades[i]
        
        # Generamos permutaciones del subconjunto restante
        restantes = ciudades[:i] + ciudades[i+1:]
        for p in generar_permutaciones(restantes):
            permutaciones.append([ciudad_actual] + p)
    
    return permutaciones

#Definimos la funcion del viajero O(n!*n)
def viajero(ciudades, distancias):
    mejor_distancia = float('inf')
    mejor_ruta = None

    # Generar todas las permutaciones posibles de las ciudades (excepto la ciudad inicial 0)
    permutaciones = generar_permutaciones(ciudades[1:])  # Excluimos la ciudad inicial
    for perm in permutaciones:
        ruta = [0] + perm                                               #Comenzamos siempre en la ciudad 0
        distancia_actual = calcular_distancia(ruta, distancias)         #Calculamos la distancia total de la ruta actual      

        if distancia_actual < mejor_distancia:                          #Se actualiza y se almacena las variables de acuerdo con la mejor distancia y mejor ruta correspondiente 
            mejor_distancia = distancia_actual
            mejor_ruta = ruta

    return mejor_ruta, mejor_distancia                                  #Retormamos con la variable que contiene con la mejor distancia y mejor ruta correspondiente 


if __name__ == "__main__":
    #Establecemos una matriz en donde contenga distancias simetricas entre ciudades
    distancias = [
        [0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0]
    ]
    
    #Establecemos el conjunto de ciudades, en este caso son el: 0, 1, 2 y el 3
    ciudades = [0, 1, 2, 3]
    
    #Llamaremos a la función y se almacena el resultado
    ruta, distancia = viajero(ciudades, distancias)

    #Imprimimos el resultado correspondiente
    print(f"La mejor ruta es: {ruta} con una distancia de {distancia}")

    #Complejidad Big O del código es O(n!)
