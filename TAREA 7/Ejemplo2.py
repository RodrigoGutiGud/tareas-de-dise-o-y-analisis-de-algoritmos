# Realizado por: Rodrigo Gutiérrez Guadarrama
# Grupo: 1561 (2025-1)
# Asignatura: Diseño y Análisis de Algoritmo

from itertools import combinations_with_replacement     #Importamos por parte del modulo itertools, la función combinations_with_replacement 
                                                        #para generar combinaciones con repetición

#Definimos la funcion para poder determinar la menor combinación de monedas
def encontrar_minimas_monedas_fuerza_bruta(monedas, objetivo):
    
    #Definimos las variables
    minima_combinacion = None                   #Será la variable tomará registro en cuanto a la mejor menor combinación de monedas
    minimo_numero_monedas = float('inf')        #Será la variable que almacenará el mínimo número de monedas encontradas

    #Creamos los ciclos for anidados para poder determinar todas las combinaciones posibles de las menor cantidad de monedas 
    for r in range(1, objetivo + 1):                                        #Complejidad: O(objetivo+1)
        for combinacion in combinations_with_replacement(monedas, r):       #Complejidad: O(m^s)
            if sum(combinacion) == objetivo:                                #Se compara si la suma de la combinación actual es igual al valor del objetivo
                if len(combinacion) < minimo_numero_monedas:                #Si la cantidad de monedas es la combinación es menor, es la mínima encontrada por de momento
                    minima_combinacion = combinacion                        #Se actualiza y se almacena la mejor combinación y el número mínimo de monedas
                    minimo_numero_monedas = len(combinacion)

    if minima_combinacion:                                                   #En caso de que se encontró una combinación que cumple con el valor objetivo, se devuelve los valores
        return minima_combinacion
    else:                                                                    #De lo contrario, se devuelve con un mensaje de error
        return "No se puede alcanzar el objetivo con las monedas dadas."    

#Establecemos el valor de las monedas como ejemplo. Las monedas de 1, 2, 5, mientras que el objetivo sería el valor de 20 pesos
monedas = [1, 2, 5]
S = 20

#Llamamos a la función y se almacena el resultado
resultado = encontrar_minimas_monedas_fuerza_bruta(monedas, S)

#Imprimimos el resultado correspondido
print(f"La combinación menor de cantidad de monedas serían: {resultado}")

#Complejidad Big O del código es O(m^S)
