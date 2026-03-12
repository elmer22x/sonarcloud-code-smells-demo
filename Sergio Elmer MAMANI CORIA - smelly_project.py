
# Mini proyecto con múltiples Code Smells para análisis con SonarQube

import math
import random

# 1: nombre de variable poco claro
a = 0

# 2: función demasiado larga
def procesar(lista):
    total = 0
    for i in lista:
        total = total + i
    for i in lista:
        total = total + i  # duplicación de código
    for i in lista:
        total = total + i
    print("Resultado:", total)
    if total > 100:
        print("Grande")
    else:
        print("Pequeño")
    for i in range(10):
        print(i)
    return total

# 3: función con demasiados parámetros
def calcular(a,b,c,d,e,f,g):
    return a+b+c+d+e+f+g

# 4: código duplicado
def area_circulo(r):
    return math.pi*r*r

def area_circulo2(r):
    return math.pi*r*r

# 5: variable global innecesaria
contador_global = 0

# 6: función que modifica variable global
def incrementar():
    global contador_global
    contador_global = contador_global + 1

# 7: uso innecesario de else
def es_par(n):
    if n % 2 == 0:
        return True
    else:
        return False

# 8: complejidad innecesaria
def decision(x):
    if x > 0:
        if x > 10:
            if x > 20:
                print("muy grande")

# 9: números mágicos
def descuento(precio):
    return precio * 0.873

# 10: función que no se usa
def funcion_inutil():
    print("Nunca se usa")

# 11: print para debugging
def debug(valor):
    print("DEBUG:", valor)

# 12: lista creada manualmente innecesariamente
lista = []
lista.append(1)
lista.append(2)
lista.append(3)

# 13: comparación redundante
def es_cero(x):
    if x == 0:
        return True
    else:
        return False

# 14: variable redefinida
def ejemplo():
    x = 5
    x = 7
    return x

# 15: función que hace demasiadas cosas
def sistema():
    datos = [1,2,3,4,5]
    r = procesar(datos)
    incrementar()
    debug(r)
    print("contador:", contador_global)
    if es_par(r):
        print("es par")
    else:
        print("no es par")

if __name__ == "__main__":
    sistema()


# 16: Función sin docstring (documentación)
def calcular_promedio(numeros):
    suma = 0
    for num in numeros:
        suma += num
    return suma / len(numeros)

# 17: Variable no utilizada
def calcular_suma(a, b):
    resultado = a + b
    x = 100  # Esta variable no se usa nunca
    return resultado

# 18: Comparación de tipos incorrecta
def comparar_tipos(valor):
    if type(valor) == int:  # Mala práctica, debería ser isinstance()
        return "Es entero"
    return "No es entero"

# 19: Uso de '== True' innecesario
def verificar_activo(activo):
    if activo == True:  # Debería ser 'if activo:'
        return "Activo"
    return "Inactivo"
