#Realizado por: Rodrigo Gutiérrez Guadarrama
#Grupo: 1561 (2025-1)
#Asignatura: Diseño y Análisis de Algoritmos

# Definimos el arreglo (incluyendo los números enteros)
data = [-9, 3, 5, -2, 9, -7, 4, 8, 6]

#Definimos a las variables para poder almacenarlas en el producto máximo
max_producto = float('-inf')  # Se comienza primero con el valor más menor posible por defecto
num1 = None
num2 = None

#Crearemos dos ciclos for anidados para poder recorrer en el arrelglo, 
for i in range(len(data)): #Complejidad = O(n)
    for j in range(i + 1, len(data)):  # Evitamos de que el mismo número se compare consigo mismo. Complejidad = O(n-1)
        producto = data[i] * data[j]  #Realizamos el producto de los elementos del arreglo
        if producto > max_producto:    #Comparamos si el prducto sea superior al valor del maximo producto que se tiene registrado
            max_producto = producto  #En caso de que lo sea, se almacena el nuevo valor del producto máximo
            num1 = data[i]             #Se almacenan los números que fueron la operación del producto mayor
            num2 = data[j]

# Imprimimos el resultado
print(f"El producto máximo es {max_producto}, que en parte son los números {num1} y {num2}.")

#Complejidad Big O del código es O(n^2)
