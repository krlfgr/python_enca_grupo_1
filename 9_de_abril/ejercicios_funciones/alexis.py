'''
Crear una función que reciba una cadena y reemplace todas las vocales por `*`.
pista: usar un bucle for y usar if
'''
def reemplazar_vocales(cadena=input("ingrese palabra:")):

    vocales="aeiouAEIOU"
    remplazo_cadena= ''
    for letra in cadena:
     if letra in vocales:
        remplazo_cadena += '*'
     else: 
        remplazo_cadena += letra
    return remplazo_cadena
print(reemplazar_vocales())


#Escribir una función que reciba una lista de palabras y 
# retorne la longitud promedio de esas palabras

def longitud_promedio(lista):
    longitudes = 0
    for palabra in lista:
        longitudes = longitudes + len(palabra)
    promedio = longitudes / len(lista)
    return promedio
lista = {"enca", "programador", "junior", "alexis"}
print(longitud_promedio(lista))
