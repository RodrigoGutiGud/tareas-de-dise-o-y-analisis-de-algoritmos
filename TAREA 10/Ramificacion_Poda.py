# Realizado por: Rodrigo Gutiérrez Guadarrama
# Grupo: 1561 (2025-1)
# Asignatura: Diseño y Análisis de Algoritmos

# Establecemos el laberinto de acuerdo con el ejemplo
laberinto = [
    ["p", "p", "p", "p", "p", "p", "p", "p"],
    ["p", "p", "p", "p", "p", "p", "p", "p"],
    ["p", "p", "p", "p", "c", "p", "p", "p"],
    ["p", "c", "c", "c", "c", "c", "c", "p"],
    ["p", "c", "p", "c", "p", "p", "c", "p"],
    ["p", "c", "p", "c", "p", "p", "c", "p"],
    ["p", "c", "p", "c", "c", "c", "c", "p"],
    ["p", "c", "p", "c", "p", "p", "c", "p"],
    ["p", "c", "c", "c", "c", "p", "c", "p"],
    ["p", "p", "p", "p", "c", "p", "c", "s"],
    ["p", "p", "c", "p", "c", "p", "p", "p"],
    ["p", "c", "c", "c", "c", "c", "p", "p"],
    ["p", "p", "c", "p", "p", "c", "p", "p"],
    ["p", "p", "E", "p", "p", "p", "p", "p"]
]

#Definimos la funcion de distancia de manhattan 
def distancia_manhattan(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)      #Calcula la distancia de Manhattan entre dos puntos

#Definimos la funcón  del algoritmo de la Ramificación y Poda 
def laberinto_ramificacion_poda(laberinto):
    fila_inicial, columna_inicial = 13, 2  #Asignamos las coordenadas de la entrada
    fila_meta, columna_meta = 9, 7        #Asignamos las coordenadas de la salida 
    visitado = [[False for _ in range(len(laberinto[0]))] for _ in range(len(laberinto))]   #Complejidad O(n*m)

    #Definimos la lista para explorar el laberinto 
    exploracion = [(0, fila_inicial, columna_inicial, [])]  #Establecemos las prioridades al recorrer: (prioridad, fila, columna, camino). Complejidad O(1)

    while exploracion:
        #Se ordena la lista en la parte de prioridad
        exploracion.sort(key=lambda x: x[0])  #Se ordenará según por la distancia de Manhattan
        prioridad, fila, columna, camino = exploracion.pop(0)  #Extraemos el elemento que posee menor distancia. Complejidad O(log(𝑛*𝑚))

        #En caso de que se alcanza la meta, entonces se retorna el camino
        if (fila, columna) == (fila_meta, columna_meta):       #Complejidad O(1)
            camino.append((fila, columna))
            for r, c in camino:
                laberinto[r][c] = '-'   #Se traza el camino correcto con el simbolo "-"
            return camino, laberinto

        #Wn caso de que ya se ha visitado el camino, entonces se ignora. Complejidad O(1)
        if visitado[fila][columna]:
            continue
        visitado[fila][columna] = True

        #Se actualiza y se agrega la casilla actual al camino
        camino.append((fila, columna))

        #Definimos los movimientos posibles que podemos realizar en el laberito en las cuales son:  izquierda, arriba, derecha, abajo
        movimientos = [(0, -1), (-1, 0), (0, 1), (1, 0)]
        for movimiento in movimientos:
            nueva_fila, nueva_columna = fila + movimiento[0], columna + movimiento[1]
            if (0 <= nueva_fila < len(laberinto) and 0 <= nueva_columna < len(laberinto[0]) and
                not visitado[nueva_fila][nueva_columna] and laberinto[nueva_fila][nueva_columna] in ('c', 'E', 's')):
                distancia = distancia_manhattan(nueva_fila, nueva_columna, fila_meta, columna_meta)
                exploracion.append((distancia, nueva_fila, nueva_columna, camino.copy()))

    return None, laberinto  #En caso de que no exista al menos una solución para el laberinto

#Se ejecuta la función y se imprime el resultado correspondido 
solucion, laberinto_resultante = laberinto_ramificacion_poda(laberinto)
if solucion:
    print("\nStack (Pila) del camino recorrido:\n")
    print("----------------------------------\n")
    for i, paso in enumerate(solucion, start=1):
        print(f"{i}. {paso}")
    print("\n----------------------------------")
    print("\nLABERINTO RESUELTO:\n")
    for fila in laberinto_resultante:
        print(" ".join(fila))
    print("\nNota: - (el simbolo guion) = son los caminos recorridos.")
else:
    print("No se encontró una ruta.")

#La complejidad Big O del programa es equivalente a 𝑂( (𝑛*𝑚) log(𝑛*𝑚) )