"""Cuenta regresiva: crea una función que acepte un número como entrada. Devuelve una lista nueva que cuente de uno en uno, desde el número (como elemento 0) hasta 0 (como último elemento). 
Ejemplo: countdown(5) debería devolver [5,4,3,2,1,0]"""
print("___________________")
def cuenta_atras(num):
    lista = []
    for i in range(num,-1, -1):
        lista.append(i)
    return lista
print(cuenta_atras(5)) 

"""Imprimir y devolver: crea una función que reciba una lista con dos números. Imprime el primer valor y devuelve el segundo.
Ejemplo: imprimir_y_devolver([1,2]) debe imprimir 1 y devolver 2 """
print("___________________")
def imprimir_y_devolver(lista):
    print(lista[0])
    return lista[1]
nums = [1,2]
print(imprimir_y_devolver(nums))

"""Primero más longitud: crea una función que acepte una lista y devuelva la suma del primer valor de la lista, más la longitud de la lista.
Ejemplo: primero_mas_longitud([1,2,3,4,5]) debe devolver 6 (primer valor: 1 +length: 5)"""
print("___________________")
def sum(lista):
    return lista[0] + len(lista)
nums2 = [1,2,3,4,5]
print(sum(nums2))

"""Valores mayores que el segundo: escribe una función que acepte una lista y cree una nueva que contenga solo los valores de la lista original que sean mayores que su segundo valor.
Imprime cuántos valores son y luego devuelve la lista nueva. Si la lista tiene menos de 2 elementos, has que la función devuelva False
Ejemplo: valores_mayores_que_el_segundo([5,2,3,2,1,4]) debe imprimir 3 y devolver [5,3,4]
Ejemplo: valores_mayores_que_el_segundo([3]) debe devolver False"""
print("___________________")
def mayores_al_2do(lista):
    nueva =[]
    if len (lista) >= 2:
        for num in lista:
            if num > lista [1]:
                nueva.append(num)
    
    print (len(nueva))
    if len(nueva) < 2:
        return False
    else:
        return nueva

ejemplo1 = mayores_al_2do ([5,2,3,2,1,4])
print (ejemplo1)
ejemplo2 = mayores_al_2do ([3])
print (ejemplo2)

"""Esta longitud, ese valor: escribe una función que acepte dos enteros como parámetros: tamaño y valor. La función debe crear y devolver una lista cuya longitud sea igual al tamaño dado,
y cuyos valores sean todos el valor dado.
Ejemplo: length_and_value(4,7) debe devolver [7,7,7,7]
Ejemplo: length_and_value(6,2) debe devolver [2,2,2,2,2,2]"""
print("___________________")
def longitud_valor(longi,valor):
    lista = []
    for i in range (longi):
        lista.append( valor)
    return lista
print(longitud_valor(4,7))
print(longitud_valor(6,2))
