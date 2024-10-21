# Realizado por: Rodrigo Gutiérrez Guadarrama
# Grupo: 1561 (2025-1)
# Asignatura: Diseño y Análisis de Algoritmos

# Definimos los objetos de acuerdo con sus pesos y valores correspondidos del ejemplo O(n)
objetos = [
    {"peso": 2, "valor": 3},
    {"peso": 3, "valor": 4},
    {"peso": 4, "valor": 5},
    {"peso": 5, "valor": 8}
]

# Definimos la capacidad máxima de la mochila, que en este caso es 8
capacidad_maxima = 8

# Definimos la función de la mochila empleando con la técnica de divide y vencerás
def mochila(objetos, capacidad_maxima):
    # Caso base: Cuando la capacidad sea igual a 0
    if not objetos or capacidad_maxima == 0:
        return 0, []

    # Si en dado caso el peso del ultimo objeto sea mayor a la capacidad de la mochila, si es así entonces lo excluimos. O(n)
    if objetos[-1]["peso"] > capacidad_maxima:          
        return mochila(objetos[:-1], capacidad_maxima)

    #Se manejaran dos casos que serían en: incluir o excluir el último objeto
    
    #Caso 1: Excluyendo al último objeto
    valor_excluido, combinacion_excluida = mochila(objetos[:-1], capacidad_maxima)

    #Caso 2: Incluimos el último objeto
    valor_incluido, combinacion_incluida = mochila(objetos[:-1], capacidad_maxima - objetos[-1]["peso"])
    valor_incluido += objetos[-1]["valor"]

    #Se determina cuál caso se debe de elegir
    if valor_incluido > valor_excluido:
        return valor_incluido, combinacion_incluida + [objetos[-1]]
    else:
        return valor_excluido, combinacion_excluida

#Llamaremos a la función y se almacena el resultado, O(2^n)
valor_maximo, objetos_seleccionados = mochila(objetos, capacidad_maxima)

#Imprimimos el resultado correspondiente
print(f"Valor máximo que se puede llevar: {valor_maximo}")
print("Objetos seleccionados:")
for obj in objetos_seleccionados:
    print(f"Peso: {obj['peso']}, Valor: {obj['valor']}")

#Complejidad Big O del código es O(2^n)
