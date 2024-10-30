# Realizado por: Rodrigo Gutiérrez Guadarrama
# Grupo: 1561 (2025-1)
# Asignatura: Diseño y Análisis de Algoritmos

#Establecemos el laberinto de acuerdo con el ejemplo
laberinto = [
    ["p", "p", "p", "p", "p", "p", "p", "p"],
    ["p", "p", "p", "p", "p", "p", "p", "p"],
    ["p", "p", "p", "p", "p", "p", "p", "p"],
    ["p", "p", "p", "p", "p", "p", "p", "p"],
    ["p", "p", "p", "p", "p", "p", "p", "p"],
    ["p", "p", "p", "p", "p", "p", "p", "p"],
    ["p", "p", "c", "c", "c", "c", "c", "p"],
    ["p", "p", "c", "p", "p", "p", "c", "p"],
    ["p", "p", "c", "c", "c", "p", "c", "p"],
    ["p", "p", "p", "p", "c", "p", "c", "s"],
    ["p", "p", "c", "p", "c", "p", "p", "p"],
    ["p", "c", "c", "c", "c", "c", "p", "p"],
    ["p", "p", "c", "p", "p", "p", "p", "p"],
    ["p", "p", "E", "p", "p", "p", "p", "p"]
]

#Definimos la función empleando por la tecnica del backtracking
def laberinto_backtracking(laberinto):
    fila_inicial, columna_inicial = 13, 2       #Asignamos las coordenadas de la entrada
    fila_meta, columna_meta = 9, 7              #Asignamos las coordenadas de la salida 
    camino = []
    visitado = [[False for _ in range(len(laberinto[0]))] for _ in range(len(laberinto))]   #Se crea una matriz que tendrá las mismas medidas que la matriz del laberinto, 
                                                                                            #por defecto está en false, debido que ninguna casilla se ha recorrido al principio

#Definimos la función de backtrack, por lo cual nos basaríamos en solucionarlo por la técnica del backtracking
    def backtrack(fila, columna):
        if fila == fila_meta and columna == columna_meta:   #Verificamos si la casilla actual sea igual a la salida
            camino.append((fila, columna))                  #Si la casilla fue cruzada, se marca como una ya recorrida, siendo así parte de las casillas que forman parte del camino 
            laberinto[fila][columna] = '-'                  #Se marcan con el simbolo "-" para las casillas que fueron recorridas y sean la ruta correcta
            return True

        #Se marcan las casillas que hayan sido recorridas en el laberinto
        visitado[fila][columna] = True
        camino.append((fila, columna))

        #Se maneja la prioridad de realizar el desplace de los movimientos por cada casilla que se encuentra: 
        #1er Izquierda, 2nda Arriba, 3ra Derecha y por último Abajo
        movimientos = [(0, -1), (-1, 0), (0, 1), (1, 0)]
        for movimiento in movimientos:
            nueva_fila, nueva_columna = fila + movimiento[0], columna + movimiento[1]
            if (0 <= nueva_fila < len(laberinto) and 0 <= nueva_columna < len(laberinto[0]) and
                not visitado[nueva_fila][nueva_columna] and laberinto[nueva_fila][nueva_columna] in ('c', 'E', 's')):       #Complejidad O(n)
                if backtrack(nueva_fila, nueva_columna):
                    laberinto[fila][columna] = '-'          #Se traza el camino correcto con el simbolo "-"
                    return True

        #En caso solamente hay presencia de puras paredes en el camino, entonces se retrocede a la previa casilla que se recorrió y se marca el camino con el
        #simbolo "X"
        camino.pop()
        laberinto[fila][columna] = 'X'              #Imprime los caminos que no tienen una ruta o salida
        return False

    if backtrack(fila_inicial, columna_inicial):    #Complejidad O(n)
        return camino, laberinto                    #Complejidad O(1)
    else:
        return None, laberinto                      #Complejidad O(1)

#Se ejecuta la función y se imprime el resultado correspondido 
#en cuanto una pila que registra los caminos recorridos y el laberinto una vez resuelto

solucion, laberinto_resultante = laberinto_backtracking(laberinto)
if solucion:
    print("\nStack (Pila) del camino recorrido:\n")
    print("----------------------------------\n")
    for i, paso in enumerate(solucion, start=1):                #Se imprime el pila que contiene los caminos una vez recorridos, Complejidad O(n)
        print(f"{i}. {paso}")
    print("\n----------------------------------")
    print("\nLABERINTO RESUELTO:\n")
    for fila in laberinto_resultante:                           #Complejidad O(m)
        print(" ".join(fila))                                   #Se imprime el laberinto resuelto, por lo cual está marcando los correctos e fallidos caminos
    print("\nNota: - (el simbolo guion) = son los caminos recorridos, mientras que X = son los caminos fallidos")
else:
    print("No se encontró una ruta.")                           #En caso de que no se encuentra alguna ruta que continuar en la travesía o si no hay una salida en el laberinto 

#La complejidad Big O del programa es equivalente a O(n*m)