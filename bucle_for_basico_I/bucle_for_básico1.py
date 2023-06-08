#Básico: imprime todos los números enteros del 0 al 150.
for enteros_al_150 in range(0,151):
    print(enteros_al_150)

#Múltiplos de cinco: imprime todos los múltiplos de 5 entre 5 y 1,000.
print("__________________________________")
for multiplos_de_5 in range(5,1001):
    if multiplos_de_5 % 5 == 0:
        print(multiplos_de_5)

#Contar, a la manera del Dojo: imprime números enteros del 1 al 100. Si es divisible por 5, imprime "Coding” en su lugar. Si es divisible por 10, imprime "Coding Dojo".
print("__________________________________")
for c_d in range(1,101):
    if c_d % 10 == 0:
        print("Coding Dojo")
    elif c_d % 5 == 0:
        print("Coding")
    else:
        print(c_d)

#Whoa. Es un gran idiota: agrega los enteros impares del 0 al 500,000, e imprime la suma final.
print("__________________________________")
suma_impares_0_500k = 0
for i in range(1, 500001, 2):
    suma_impares_0_500k += i

print(suma_impares_0_500k)

#Cuenta regresiva de a 4: imprime números positivos comenzando desde el 2018, en cuenta regresiva de 4 en 4.
print("__________________________________")
for cada_4_reversa in range(2018,0,-4):
    print(cada_4_reversa)

"""Contador flexible: establece tres variables: lowNum, highNum, mult. Comenzando en lowNum y pasando por highNum, imprime solo 
los enteros que sean múltiplos de mult. Por ejemplo, si lowNum=2, highNum=9 y mult=3. El bucle debe imprimir 3, 6, 9 (en líneas sucesivas)."""
print("__________________________________")
lowNum=2
highNum=9
mult=3
for flexible in range(lowNum,highNum+1):
    if flexible % mult == 0:
        print(flexible)



