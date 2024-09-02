#Realizado por: Rodrigo Gutiérrez Guadarrama
#Grupo: 1561 (2025-1)
#Asignatura: Diseño y Análisis de Algoritmos

def fibonacci(n):
    if n == 0: #cuando n sea equivalente a 0
        return 0
    else:
        if n == 1:
            return 1 #cuando n sea equivalente a 1
        else:
            return fibonacci(n-1)+fibonacci(n-2) #Se retorna empleando la formula de Fibonacci


#Se imprime la serie Fibonacci poniendo a n como limite
n = 7
print(f"La serie Fibonacci hasta {n} es:")

for i in range(n + 1):
    print(f"{fibonacci(i)}, ", end="")