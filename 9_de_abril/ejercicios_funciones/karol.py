'''
Crear una función que reciba una cadena y reemplace todas las vocales por `*`.
pista: usar un bucle for y usar if
'''
def cadena(cadena_texto="hola"):
    vocales="aeiou"
    modificado=""
    for letra in cadena_texto:
        if letra in vocales:
            modificado+="*"
        else:
            modificado+=letra   
        #modificado=cadena_texto.replace(vocales,"*")
    return modificado
    
print(cadena("prueba"))