# Realizado por: Rodrigo Gutiérrez Guadarrama
# Grupo: 1561 (2025-1)
# Asignatura: Diseño y Análisis de Algoritmos

# Definimos el arreglo
data = [-9, 3, 5, -2, 9, -7, 4, 8, 6]

#Definimos a la función recursiva para determinar el producto máximo de dos números en el arreglo establecido
def maximo_producto(arr):
    #Establecemos el caso base, en caso de que el arreglo tiene al menos de dos elementos, de lo contrario no es posible realizar un producto
    if len(arr) < 2:
        return float('-inf'), None, None

    #Dividimos el arreglo en dos mitades
    mitad = len(arr) // 2
    izq = arr[:mitad]   #Lado izquierdo
    der = arr[mitad:]   #Lado derecho

    #Definimos los objetos para poder determinar el producto máximo en cada mitad O(log n)
    max_izq, num1_izq, num2_izq = maximo_producto(izq)
    max_der, num1_der, num2_der = maximo_producto(der)

    #Determinamos el producto máximo entre los elementos que hay en los bordes de las dos mitades
    max_com = float('-inf')
    max_num1_com = max_num2_com = None
    for i in izq:                       #O(n^2)
        for j in der:
            producto = i * j
            if producto > max_com:      #Comparamos si el prducto sea superior al valor del maximo producto que se tiene registrado
                max_com = producto      #En caso de que lo sea, se almacena el nuevo valor del producto máximo
                max_num1_com = i        #Se actualizan y se almacenan los números que fueron la operación del producto mayor
                max_num2_com = j

    #Determinaremos el producto máximo entre las tres opciones
    if max_izq > max_der and max_izq > max_der:
        return max_izq, num1_izq, num2_izq
    elif max_der > max_izq and max_der > max_com:
        return max_der, num1_der, num2_der
    else:
        return max_com, max_num1_com, max_num2_com

#Llamaremos a la función y obtendremos el resultado de los numeros establecidos en el array
producto, num1, num2 = maximo_producto(data)

#Imprimimos el resultado
print(f"El producto máximo es {producto}, que en parte son los números {num1} y {num2}.")

# Complejidad Big O del código es O(log n)
