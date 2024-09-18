#Realizado por: Rodrigo Gutiérrez Guadarrama
#Grupo: 1561 (2025-1)
#Asignatura: Diseño y Análisis de Algoritmos


# Definimos la búsqueda lineal
def busqueda_lineal(data, x):
    n = len(data)
    for i in range(n):
        for j in range(0, n-i-1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j] 

    print("Arreglo ordenado para búsqueda lineal:", data)

    for i in range(len(data)):
        if data[i] == x:
            return i
    return -1

#La complejidad de la búsqueda lineal es O(n^2)

# Definimos la búsqueda lineal con centinela
def busqueda_lineal_con_centinela(data, x):
    n = len(data)
    for i in range(n):
        for j in range(0, n-i-1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]  

    print("Arreglo ordenado para búsqueda lineal con centinela:", data)

    ultimo = data[n-1]
    data[n-1] = x
    i = 0
    while data[i] != x:
        i += 1
    data[n-1] = ultimo  

    if i < n-1 or data[n-1] == x:
        return i
    return -1

#La complejidad de la búsqueda lineal con centinela es de O(n^2)


#Definimos la búsqueda binaria
def busqueda_binaria(data, x, bajo, alto):
   
    if bajo > alto:
        return -1
    
    medio = (bajo + alto) // 2
    if data[medio] == x:
        return medio
    elif data[medio] > x:
        return busqueda_binaria(data, x, bajo, medio - 1)
    else:
        return busqueda_binaria(data, x, medio + 1, alto)
    
#La complejidad de la búsqueda binaria es de O(log n)

# Definimos la función main
def main():
    # Arreglo por defecto
    data = [3, 6, 8, 10, 15, 20, 30, 35, 40, 50]
    
    # Elemento a buscar 
    elemento_buscar = 20  

    # Imprimimos la búsqueda lineal
    print("\n--- Búsqueda Lineal ---")
    resultado_lineal = busqueda_lineal(data.copy(), elemento_buscar)  
    
    # Imprimimos la búsqueda lineal con centinela
    print("\n--- Búsqueda Lineal con Centinela ---")
    resultado_centinela = busqueda_lineal_con_centinela(data.copy(), elemento_buscar)  
    
    #Imprimimos la búsqueda binaria
    n = len(data)
    for i in range(n):
        for j in range(0, n-i-1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]  

    print("\n--- Búsqueda Binaria ---")
    print("Arreglo ordenado para búsqueda binaria:", data)
    resultado_binaria = busqueda_binaria(data, elemento_buscar, 0, len(data) - 1)

# Ejecutamos el main
if __name__ == "__main__":
    main()
