'''
Crear una función que reciba una cadena y reemplace todas las vocales por `*`.
pista: usar un bucle for y usar if

def remplazo_vocales(cadena):
    vocales = 'aeiouAEIOU'
    for letra in cadena:
        if letra in vocales:
'''
'''
Pendiente
'''

# Escribir una función que reciba una lista de palabras y retorne la longitud promedio de esas palabras
lista_palabras = ["miku","kaito","gumi","rin","meiko"]
def longitud_de_palabras(palabras): 
    long_total = 0
    for palabra in palabras:
        long_total += len(palabra)

    return long_total / len(palabras)
# Llamar a la función y mostrar el resultado
print("La longitud promedio de las palabras es:", longitud_de_palabras(lista_palabras))