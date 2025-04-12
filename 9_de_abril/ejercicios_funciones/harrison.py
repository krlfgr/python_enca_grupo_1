'''
Crear una función que reciba una cadena y reemplace todas las vocales por `*`.
pista: usar un bucle for y usar if
'''



def reemplazar_vocales(cadena):
    text = ""
    for c in cadena:
        if c in "aeiouAEIOU":
            text += "*"
        else:
            text += c
    return text


print(reemplazar_vocales("Real Madrid"))


# Escribir una función que reciba una lista de palabras y retorne la longitud promedio de esas palabras


def longitd_promedio(palabras):
    suma = 0
    for palabra in palabras:
        suma += len(palabra)
    return suma / len(palabras) if palabras else 0

print(longitd_promedio(["Casa", "Muebles","Baño","Estudio"]))


    return

lista2 = ["Maria","Pedro","gabriel",]