#Realizado por: Rodrigo Gutiérrez Guadarrama
#Grupo: 1561 (2025-1)
#Asignatura: Diseño y Análisis de Algoritmos

#Definimos la clase nodo, este sería la representación de cada nodo que hay en el arbol
class Nodo:
    def __init__(self, dato): #Utilizamos __init__ para casí construir los nodos
        self.dato = dato #Almacena el valor que contiene el nodo
        self.hijos = [] #Inicia siendo una lista vacía de nodos
        
        
#Definimos  la funcion de imprimir, este se encarga de encontrar el nodo en especifico que se va a buscar en el arbol.
def imprimir_nodo(raiz, valor): #La raiz define el comienzo de la busqueda del nodo; que por defecto sería el head, mientras que el valor define el valor del nodo que se esta buscando
    if raiz is None: #Si la raiz es none o nula, la busqueda se detiene y termina
        return
    if raiz.dato == valor: #Si el valor del nodo actual es qeuivalente al nodo que se esta buscando, entonces la busqueda se detiene y imprime el nodo encontrado
        print(f"Busqueda terminada, se encontro el nodo: {raiz.dato}")
        return
    for hijo in raiz.hijos: #Si el nodo actual no es el equivalente al nodo que se este buscando, entonces empleando un for hara que llame recursivamente para cada nodo hijo
        imprimir_nodo(hijo, valor)

#Se crean los nodos con cada valor que esta en especifico, de acuerdo con lo que describe la imagen 
head = Nodo(20)
nodo23 = Nodo(23)
nodo19 = Nodo(19)
nodo57 = Nodo(57)
nodo67 = Nodo(67)
nodo99 = Nodo(99)

#Se establece una jerarquía de relaciones que hay entre los nodos si son hijos de otros nodo, de acuerdo de lo que se basa en la imagen 
head.hijos = [nodo23, nodo19]
nodo23.hijos = [nodo57]
nodo19.hijos = [nodo67]
nodo67.hijos = [nodo99]

#Imprimimos  los nodos solicitados que en este caso son el 99 y el 57 usando por medio de la funcion que es imprimir_nodo
print("Comenzando con la busqueda para encontrar el nodo 99:")
imprimir_nodo(head, 99)

print("Comenzando con la busqueda para encontrar el nodo 57:")
imprimir_nodo(head, 57)
