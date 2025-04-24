# crear las funciones suma, resta, multiplicacion, division, division piso (validar 0 denominador)
# crear una funcion que genere un numero aleatorio (import random)
# crear una funcion modulo (%)

import random

def suma(a,b):
    return a+b

def resta(a,b):
    return a-b

def multiplicacion(a,b):
    return a*b

def division(a,b):
    if b==0 or a==0:
        return "no puedo dividir por cero"
    return a/b

print(division(0,3))

def division_piso(a,b):
    return a//b

def numero_aleatorio():
    return random.random()

def modulo(a,b):
    return a%b