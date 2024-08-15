#Realizado por: Rodrigo Gutiérrez Guadarrama
#Grupo: 1561 (2025-1)
#Asignatura: Diseño y Análisis de Algoritmos

#Definimos la entrada que será el array de los numeros que vamos a combinar 
entrada = [1, 2, 3]

#total será la variable que se va contar por el número total de combinaciones     
total = 0

#imprimimos la entrada
print("Lista de numeros como entrada: ",entrada)

#n será la variable que contará la cantidad de números que hay en la entrada, en este caso serán 3
n = len(entrada)

for i in range(n): #Es el bucle externo quien hará el recorido de la lista de entrada, su complejidad es T(n)=n, ya que se recorren n elementos que hay en el bucle externo
    for j in range(n): #Es el bucle interno quien este recore a la lista de los números de entrada, para que estos sean combinados con el bucle externo. Por lo tanto  su complejidad es T(n)=n, ya que se recorren n elementos por cada interación que se emplea en el bucle externo
        print("\n[",entrada[i],",",entrada[j],"]") #Imprime la combinación de cada numero de acuerdo con la lista de entrada
        total+=1 #Por cada combinación realizada, la variable total se sumará a 1

print("\nNumero total de combinaciones: ",total,) #Se imprime el número total de combinaciones que se hayan realizado en los bucles

#Una vez de analizar la complejidad de T(n), consideramos que:
#Por el bucle externo resultó ser T(n)=n
#Mientras que en el bucle interno que igual resultó ser a T(n)=n
#Y como ambos bucles están anidados; entonces la complejidad sería siendo igual que: T(n)=n*n => T(n)=n^2
#Entonces la complejidad de este código es equivalente a: T(n)=n^2