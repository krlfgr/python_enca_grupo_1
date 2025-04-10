

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