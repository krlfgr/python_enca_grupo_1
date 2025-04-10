'''
Crear una función que reciba una cadena y reemplace todas las vocales por `*`.
pista: usar un bucle for y usar if
'''
def remplazo_vocales(cadena):
    vocales = 'aeiouAEIOU'
    for letra in cadena:
        if letra in vocales: