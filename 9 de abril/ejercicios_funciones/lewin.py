'''
Crear una función que reciba una cadena y reemplace todas las vocales por `*`.
pista: usar un bucle for y usar if
'''
def reemplazar_vocales(cadena):
    vocales = "aeiouAEIOU"
    nueva_cadena = ""
    for caracter in cadena:
        if caracter in vocales:
            nueva_cadena += '*'
        else:
            nueva_cadena += caracter
    return nueva_cadena

texto = input("ingrese un texto: ")
resultado = reemplazar_vocales(texto)
print(resultado) 
