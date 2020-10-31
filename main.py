# Ej. 1:

print("---EJERCICIO 1:")

numero = int(input("Escribe un número entero: "))

print("La tabla de multiplicar es: ")
for i in range(1, 11):
    print(f'{i} * {numero} = {i * numero}')

# Ej. 2:

print("---EJERCICIO 2:")


def bucle():
    for j in range(10, 20):
        print(j)


bucle()

# Ej. 3:

print("---EJERCICIO 3:")


def ConvertirFaC(x):
    res = ((9 / 5) * x + 32)
    return res


def TablaF():
    for i in range(0, 130, 10):
        print(str(i) + " ºC = " + str(ConvertirFaC(i)) + " F")


TablaF()

# Ej. 4:

print("---EJERCICIO 4:")


def añoBisiesto(x):
    if x % 4 == 0 and (x % 400 == 0 or x % 100 != 0):
        return True
    return False


print(añoBisiesto(2020))  # Año Bisiesto. True
print(añoBisiesto(2019))  # Año común. False
print(añoBisiesto(1700))  # 1700 es divisible entre 4 pero no es divisible por 400. False
print(añoBisiesto(4000))  # 4000 es divisible entre 4 y 400. True

# Ej. 5:

print("---EJERCICIO 5:")


def diaDelMes(x):
    dias = {
        1: 31,
        2: 28,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31
    }
    if 1 <= x <= 12:
        return dias.get(x)
    return -1


print(diaDelMes(1))
print(diaDelMes(6))
print(diaDelMes(12))

# Ej. 6:

print("---EJERCICIO 6:")


def fechaValida(d, m, año):
    valido = False

    if diaDelMes(m) > 0:
        if 1 <= d <= diaDelMes(m):
            valido = True
        else:
            valido = False

        if m == 2 and añoBisiesto(año):
            if 1 <= d <= (diaDelMes(m) + 1):
                valido = True

    return valido


print(fechaValida(29, 2, 2020))
print(fechaValida(32, 6, 2020))
print(fechaValida(5, 4, 2020))

# Ej. 7:

print("---EJERCICIO 7:")

cadena = input("Escribe la cadena: ")


def primeraLetra(cadena):
    palabras = cadena.split()
    nueva_cadena = ""

    for palabra in palabras:
        nueva_cadena = nueva_cadena + str(palabra[0])

    print(nueva_cadena)


primeraLetra(cadena)

# Ej. 8:

print("---EJERCICIO 8:")

cadena = input("Escribe una palabra: ")


def devolverConso(cadena):
    nueva_cadena = ""
    list = ("a", "e", "i", "o", "u")
    cadena.lower()
    for letra in list:
        cadena = cadena.replace(letra, "")
    print(cadena)


devolverConso(cadena)

# Ej. 9:


print("---EJERCICIO 9:")

cadena1 = input("Introduce una palabra: ")
cadena2 = input("Introduce otra palabra: ")


def comprobarOrden():
    cadenas = [cadena1, cadena2]
    print("La cadena mas pequeña es: " + min(cadenas))


comprobarOrden()

# Ej. 10:

print("---EJERCICIO 10:")

tuplaNumeros = (1, 2, 3, 5, 6, 9, 10)


def ordenados(tuple1):
    tuple2 = tuple(sorted(tuple1))

    print(tuple1)
    print(tuple2)

    if tuple1 == tuple2:
        print("La tupla está ordenada. ")
    else:
        print("La tupla no está ordenada. ")


ordenados(tuplaNumeros)

# Ej. 11:

print("---EJERCICIO 11:")

tupla = (3, 4)
tupla1 = (5, 4)

if tupla[0] == tupla1[0] or tupla[0] == tupla1[1] or tupla[1] == tupla1[0] or tupla[1] == tupla1[0]:
    print("Las fichas no encajan. ")
else:
    print("Las fichas encajan. ")

# Ej. 12:

print("---EJERCICIO 12:")

listaNumeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def factorial(num):
    factorial = 1
    if num == 0:
        return 1
    else:
        for j in range(1, num + 1):
            factorial = factorial * j
        return factorial


for i in listaNumeros:
    print("El factorial de " + str(listaNumeros[i]) + " es: " + str(factorial(listaNumeros[i])))

# Ej. 13:

print("---EJERCICIO 13:")

listaDeNumeros = [12, 34, 55, 7, 10, 2, 21, 77, 0]
k = int(input("Introduce el valor de k: "))


def listas(lista, k):
    listaMayores = []
    listaMenores = []
    listaIguales = []

    for i in range(0, len(lista)):
        if lista[i] < k:
            listaMenores.append(lista[i])
        if lista[i] > k:
            listaMayores.append(lista[i])
        if lista[i] == k:
            listaIguales.append(lista[i])

    print("Lista de números menores: " + str(listaMenores))
    print("Lista de números mayores: " + str(listaMayores))
    print("Lista de números iguales: " + str(listaIguales))


listas(listaDeNumeros, k)

# Ej. 14:

print("---EJERCICIO 14:")

cadena = str(input("Escribe una cadena: "))
cadena = cadena.lower()


def cuentaPalabras(frase):
    diccionario = {}
    listapalbras = frase.split()
    for i in range(0, len(listapalbras)):
        if listapalbras[i] in diccionario:
            diccionario[listapalbras[i]] = diccionario[listapalbras[i]] + 1
        else:
            diccionario[listapalbras[i]] = 1

    print(str(diccionario))


cuentaPalabras(cadena)

# Ej. 15:
import random

print("---EJERCICIO 15:")

dado1 = []
dado2 = []


def hacerTirada(lista):
    lista.append(random.randrange(1, 7))


hacerTirada(dado1)
hacerTirada(dado2)
hacerTirada(dado1)
hacerTirada(dado2)
hacerTirada(dado1)
hacerTirada(dado2)
hacerTirada(dado1)
hacerTirada(dado2)

print("Tiradas del dado 1: " + str(dado1))
print("Tiradas del dado 2: " + str(dado2))


def cantidad(dado1, dado2):
    suma = []
    for i in range(0, len(dado1)):
        suma = dado1[i] + dado2[i]

    print(str(suma))


cantidad(dado1, dado2)
