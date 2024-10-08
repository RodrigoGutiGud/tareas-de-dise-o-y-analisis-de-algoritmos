# Realizado por: Rodrigo Gutiérrez Guadarrama
# Grupo: 1561 (2025-1)
# Asignatura: Diseño y Análisis de Algoritmo

from itertools import combinations                  #Importamos por parte del modulo itertools, la función combinations_with_replacement 
                                                    #para generar combinaciones con repetición

# Definimos los objetos de acuerdo con sus pesos y valores correspondidos del ejemplo
objetos = [
    {"peso": 2, "valor": 3},
    {"peso": 3, "valor": 4},
    {"peso": 4, "valor": 5},
    {"peso": 5, "valor": 8}
]

#Definimos la capacidad máxima de la mochila, que en este caso es 8
capacidad_maxima = 8

#Definimos la función mochila
def mochila(objetos, capacidad_maxima):
    n = len(objetos)                                #En n almacenaremos el número de objetos disponibles que pueden ocupar en la mochila
    mejor_valor = 0                                 #Almacenaremos el valor máximo que se puede ocupar en la mochila.    
    mejor_comb = []                                 #Almacena la mejor combinación de objetos que maximiza el valor sin que se exceda el peso en la mochila.
    
    #Creamos los ciclos for anidados para poder probar y generar todas las combinaciones posibles
    for r in range(1, n+1):                                                 #Complejidad: O(n)
        for comb in combinations(objetos, r):                               #Complejidad: O(2^n)
            peso_total = sum(objeto['peso'] for objeto in comb)             #Calcula la suma de los pesos de los objetos en la combinación actual
            valor_total = sum(objeto['valor'] for objeto in comb)           #Calcula la suma de los valores de los objetos en la combinación actual
            
            # Comprobamos si la combinación sea verdadera y incluyendo que no se excede la capacidad
            if peso_total <= capacidad_maxima and valor_total > mejor_valor:    #Si la combinación actual sea válida y tiene un valor mayor a comparación 
                mejor_valor = valor_total                                       #a la que se tiene registrada se actualizan e almacena el valor actual y el peso
                mejor_comb = comb
    
    return mejor_valor, mejor_comb      #Devolvemos la mejor solución

#Llamamos a la función y se almacena el resultado
valor_maximo, objetos_seleccionados = mochila(objetos, capacidad_maxima)

#Imprimimos el resultado correspondido
print(f"Valor máximo que se puede llevar: {valor_maximo}")
print("Objetos seleccionados:")
for obj in objetos_seleccionados:
    print(f"Peso: {obj['peso']}, Valor: {obj['valor']}")

    #Complejidad Big O del código es O(2^n)
