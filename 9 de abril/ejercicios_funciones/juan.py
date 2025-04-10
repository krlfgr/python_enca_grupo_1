'''
Crear una función que reciba una cadena y reemplace todas las vocales por `*`.
pista: usar un bucle for y usar if
'''

def reemplazar_vocales(cadena):
    vocales ="aeiouAEIOU"
    for letra in cadena:
        if letra in vocales:
            cadena = cadena.replace(letra, '*')
            return cadena

print(reemplazar_vocales("Hola Mundo"))