'''
Crear una función que reciba una cadena y reemplace todas las vocales por `*`.
pista: usar un bucle for y usar if
'''


def reemplazar_vocales(cadena):
    vocales="aeiouAEIOU"
    for letra in cadena:
        if letra in vocales:
            cadena = cadena.replace(letra,'*')
            return cadena

print(reemplazar_vocales("Hola Mundo"))


# Escribir una función que reciba una lista de palabras y retorne la longitud promedio de esas palabras

Lista=["japon","china","españa","francia"]

def longitud_de_las_palabras(palabras):
    if palabras == 0:
        return 0
    total = 0 
    for palabra in palabras:
        total += len(palabra)
        return total / len(palabras)


print(longitud_de_las_palabras(Lista))