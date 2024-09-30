#Realizado por: Rodrigo Gutiérrez Guadarrama
#Grupo: 1561 (2025-1)
#Asignatura: Diseño y Análisis de Algoritmos

import random #Importamos la librería fake para generar datos ficticios y de allí mismo se permite realizar pruebas
from faker import Faker #Importamos el módulo random para así poder Generar los datos aleatorios para así podemos generar los nombres, los apellidos, la edad, los correos, el semestre que va cursando, etc...
from unidecode import unidecode #Importamos el módulo unicode, con el fin de poder eliminar carácteres especiales que no son necesarios al generar los datos de los 100 alumnos 

faker = Faker('es_MX') # Definimos una instancia de la librería Fake. Asimismo seleccionaremos la región y el idioma de México para así generar los datos de los alumnos

#En este apartado son el nombre de todas las asignaciones que se encuentran en ICO por parte de la FES Aragón, únicamente se agregó a las asignaturas que son necesarias cursarlas durante la trayecoria de la carrera
materias = [
    "Cálculo Diferencial e Integral", "Álgebra", "Geometría Analítica",
    "Introducción a la Ingeniería en Computación", "Computadoras y Programación", 
    "Cálculo Vectorial", "Álgebra Lineal", "Administración Contabilidad y Costos",
    "Comunicación Oral y Escrita", "Programación Orientada a Objetos", 
    "Ecuaciones Diferenciales", "Métodos Numéricos", "Electricidad y Magnetismo", 
    "Introducción a la Economía", "Estructura de Datos", "Probabilidad y Estadística", 
    "Investigación de Operaciones y Sistemas", "Estructuras Discretas", 
    "Ingeniería Económica", "Análisis de Circuitos Eléctricos (L)", 
    "Diseño y Análisis de Algoritmos", "Lenguajes Formales y Autómatas", 
    "Medición e Instrumentación (L)", "Programación de Sistemas", 
    "Dispositivos Electrónicos (L)", "Ingeniería de Software", 
    "Sistemas de Comunicaciones (L)", "Sistemas Operativos", 
    "Compiladores", "Diseño Lógico (L)", "Calidad", 
    "Redes de Computadoras I (L)", "Seguridad Informática", 
    "Dinámica de Sistemas Físicos", "Diseño de Sistemas Digitales (L)", 
    "Bases de Datos I", "Sistemas de Información", 
    "Organización y Administración de Centros de Computo", 
    "Sistemas de Control (L)", "Microprocesadores y Microcontroladores (L)", 
    "Gestión de Redes de Computadoras (L)", "Habilidades Directivas", 
    "Inteligencia Artificial"
]

#Creamos la clase estudiante, en la cual emplea los siguientes atributos: nombre, apellido, edad, semestre, materias, promedio, correo y número de cuenta.
class Estudiante:
    def __init__(self, nombre, apellido, edad, semestre, materias, promedio, correo, num_cuenta):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.semestre = semestre
        self.materias = materias
        self.promedio = promedio
        self.correo = correo
        self.num_cuenta = num_cuenta

# Creamos una clase Nodo que este representa el árbol binario de búsqueda. Por lo tanto, cada nodo contendrá un estudiante y dispondrá de punteros 
class Nodo:
    def __init__(self, estudiante):
        self.estudiante = estudiante
        self.left = None
        self.right = None

#Creamos la clase del árbol binario de búsqueda, su objetivo sería que organiza y busca los datos de los estudiantes de manera eficiente
class ArbolBinarioBusqueda:
    def __init__(self):
        self.root = None

    #Empleamos una función para insertar un nuevo estudiante que se desea agregar a la base de datos, por lo cual inserción se basa de comparar el número de cuenta si es mayor o menor, si es menor se irá a la izquierda, de lo contrario sería a la derecha
    def insertar(self, estudiante):
        if self.root is None:
            self.root = Nodo(estudiante)
        else:
            self._insertar(self.root, estudiante)

    #Emplearmos un proceso de llamado "_inserción", en donde este empleará la inserción recursiva
    def _insertar(self, nodo_actual, estudiante):
        if estudiante.num_cuenta < nodo_actual.estudiante.num_cuenta:
            if nodo_actual.left is None:
                nodo_actual.left = Nodo(estudiante)
            else:
                self._insertar(nodo_actual.left, estudiante)
        elif estudiante.num_cuenta > nodo_actual.estudiante.num_cuenta:
            if nodo_actual.right is None:
                nodo_actual.right = Nodo(estudiante)
            else:
                self._insertar(nodo_actual.right, estudiante)
        else:
            print("\nEl número de cuenta ya existe. No se puede insertar.")

    #Definimos una función llamado "bucar", en la cual; con el uso del arbol binario de busqueda, se realizará la búsqueda del estudiante empleando únicamente su número de cuenta, si lo encuentra devolverá los datos del estudiante, de lo contrario devolverá un none
    def buscar(self, num_cuenta):
        return self._buscar(self.root, num_cuenta)

    #Emplearmos un proceso de llamado "_bucar", en donde este realiza la búsqueda recursiva
    def _buscar(self, nodo_actual, num_cuenta):
        if nodo_actual is None:
            return None
        if num_cuenta == nodo_actual.estudiante.num_cuenta:
            return nodo_actual.estudiante
        elif num_cuenta < nodo_actual.estudiante.num_cuenta:
            return self._buscar(nodo_actual.left, num_cuenta)
        else:
            return self._buscar(nodo_actual.right, num_cuenta)

#En este caso se generan los 100 estudiantes por defecto
def generar_estudiantes(n):
    estudiantes = []
    for _ in range(n):
        nombre = faker.first_name()
        apellido = faker.last_name()
        edad = random.randint(18, 35)
        semestre = random.randint(1, 9)
        asignaturas = random.sample(materias, 5)
        promedio = round(random.uniform(5.0, 10.0), 2)
        correo = unidecode(f"{nombre.lower()}.{apellido.lower()}@aragon.unam.mx")
        num_cuenta = random.randint(400000000, 499999999)
        estudiante = Estudiante(nombre, apellido, edad, semestre, asignaturas, promedio, correo, num_cuenta)
        estudiantes.append(estudiante)
    return estudiantes

# #En esta función, se encarga de imprimir la información del estudiante
def mostrar_informacion_estudiante(estudiante):
    if estudiante:
        print(f"\nNombre completo: {estudiante.nombre} {estudiante.apellido}")
        print(f"Materias: {', '.join(estudiante.materias)}")
        print(f"Promedio general: {estudiante.promedio}")
        print(f"Semestre: {estudiante.semestre}")
        print(f"Correo electrónico: {estudiante.correo}")
        print(f"Número de cuenta: {estudiante.num_cuenta}")
    else:
        print("Estudiante no encontrado.")


#En esta función se encarga de imprimir todos los estudiantes quienes se encuentran registrados en la base de datos
def mostrar_todos_estudiantes(nodo):
    if nodo is not None:
        mostrar_todos_estudiantes(nodo.left)  # Recorrer subárbol izquierdo
        mostrar_informacion_estudiante(nodo.estudiante)  # Mostrar información del estudiante
        mostrar_todos_estudiantes(nodo.right)  # Recorrer subárbol derecho


#Por aquí creamos un función en donde sería un menu de opciones interactivo, al momento de que ejecutamos el programa 
def menu():
    arbol = ArbolBinarioBusqueda()
    
    #Por allí se genera y se almacena los 100 estudiantes 
    estudiantes = generar_estudiantes(100)
    for estudiante in estudiantes:
        arbol.insertar(estudiante)

    while True:

        print("---------------------------------------------------------")
        print("\n1. Insertar nuevo alumno")
        print("2. Consultar alumno por número de cuenta")
        print("3. Mostrar todos los estudiantes")
        print("4. Salir")
        opcion = input("Elige una opción: ")

        if opcion == "1": #En la primera opción alli se encarga de registrar un estudiante nuevo para la base de datos
            nombre = input("\nNombre: ")
            apellido = input("Apellido: ")
            edad = int(input("Edad: "))
            semestre = int(input("Semestre: "))
            asignaturas = random.sample(materias, 5)
            promedio = round(random.uniform(5.0, 10.0), 2)
            correo = unidecode(f"{nombre.lower()}.{apellido.lower()}@aragon.unam.mx")
            num_cuenta = int(input("Número de cuenta: "))

            nuevo_estudiante = Estudiante(nombre, apellido, edad, semestre, asignaturas, promedio, correo, num_cuenta)
            arbol.insertar(nuevo_estudiante)
            print("Alumno insertado exitosamente.")

        elif opcion == "2": #En la segunda opción alli se encarga de consultar el número de cuenta de un estudiante en específico
            num_cuenta = int(input("\nNúmero de cuenta: "))
            estudiante = arbol.buscar(num_cuenta)
            mostrar_informacion_estudiante(estudiante)

        elif opcion == "3": #En esta opción se imprime todos los alumnos quienes se encuentran registrados en la base de datos
            print("\nMostrando todos los estudiantes:")
            mostrar_todos_estudiantes(arbol.root)  

        elif opcion == "4": #En la opción 4 salimo del programa
            break

        else: #Si un número no coincide de acuerdo a las anteriores opciones, entonces se arroja un mensaje de una operación no válida
            print("Opción no válida. Inténtalo de nuevo.")


#Ejecucción del menú, al momento de iniciar con el programa
menu()
