"""1. Actualiza:
Cambia el valor 10 en x a 15. Una vez que hayas terminado, x ahora debería ser [ [5,2,3], [15,8,9] ].
Cambia el "apellido” del primer alumno de 'Jordan' a 'Bryant'.
En el directorio_deportes, cambia "Messi" por "Andrés".
Cambia el valor 20 en z a 30."""

x = [ [5,2,3], [15,8,9] ] 
estudiantes = [
    {'first_name':  'Michael', 'last_name' : 'Bryant'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
directorio_deportes = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'fútbol' : ['Andrés', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 30} ]

"""2. Iterar a través de una lista de diccionarios
Crea una función iterateDictionary(some_list)para que, dada una lista de diccionarios,
la función recorra cada diccionarios de la lista e imprima cada llave y el valor asociado. Por ejemplo, dada la siguiente lista:"""

estudiantes = [
    {'first_name': 'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'},
    {'first_name': 'Mark', 'last_name': 'Guillen'},
    {'first_name': 'KB', 'last_name': 'Tonel'}
]

def iterateDictionary(lista):
    for persona in lista:
        datos_persona = []
        for clave, valor in persona.items():
            datos_persona.append(f'{clave} - {valor}')
        print(', '.join(datos_persona))

iterateDictionary(estudiantes)

"""3. Obtener valores de una lista de diccionarios
Crea una función iterateDictionary2(key_name, some_list)que, dada una lista de diccionarios y un nombre de clave, 
la función imprima el valor almacenado en esa clave para cada diccionario. Por ejemplo, iterateDictionary2('name', estudiantes) debería generar:
Michael
John
Mark
KB
Y iterateDictionary2('last_name', estudiantes) debería generar:
Jordan
Rosales
Guillen
Tonel
"""
print("_________________________")
def iterateDictionary2(clave, lista):
    for diccionario in lista:
        if clave in diccionario:
            print(diccionario[clave])

iterateDictionary2('first_name', estudiantes)
iterateDictionary2('last_name', estudiantes)

"""Iterar a través de un diccionarios con valores de lista
Crea una función printInfo(some_dict)que, dado un diccionario cuyos valores son todos listas, imprima el nombre de cada clave junto con el tamaño de su lista,
y luego imprima los valores asociados dentro de la lista de cada clave. Por ejemplo:"""

print("______________")
dojo = {
    'ubicaciones': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructores': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
def iterateDictionary3(clave, dicc):
    lista = dicc[clave]
    longitud = len(lista)

    print(f'{longitud} {clave.upper()}')
    for valor in lista:
        print(valor)

iterateDictionary3('ubicaciones', dojo)
iterateDictionary3('instructores', dojo)


"""salida:
7 UBICACIONES
San Jose
Seattle
Dallas
Chicago
Tulsa
DC
Burbank
    
8 INSTRUCTORES
Michael
Amy
Eduardo
Josh
Graham
Patrick
Minh
Devon

"""

