

'''
Crear una función que reciba una cadena y reemplace todas las vocales por `*`.
pista: usar un bucle for y usar if
'''

def reemplazar_vocales(cadena):
    #definimos las vocales
    vocales = "aeiouAEIOU"
    nueva_cadena = ""

# Iteramos sobre cada caracter en la cadena
    for caracter in cadena:
        # Verificamos si el caracter es una vocal
        if caracter in vocales:
            nueva_cadena += "*"
        else:
            nueva_cadena += caracter

    return nueva_cadena

texto = input("Ingrese una cadena: ")
resultado = reemplazar_vocales(texto)
print("Cadena modificada:", resultado)



def longitud_promedio (palabras):
    # verificamos si la lista esta vacia
    if not palabras:
        return 0 # retornamos 0 si no hay palabras

    #calculamos la suma de las longitudes de las palabras
    total_longitud = sum(len(palabra) for palabra in palabras)

    # calculamos la longitud promedio
    promedio = total_longitud / len(palabras)

    return promedio

lista_palabras = ["programacion", "tecnologia", "sistemas", "portatil"]
resultado = longitud_promedio(lista_palabras)
print ("la longitud promedio de las palabras es:", resultado)