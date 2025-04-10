'''
Crear una función que reciba una cadena y reemplace todas las vocales por `*`.
pista: usar un bucle for y usar if
'''

# Creamos una función para reemplazar las vocales
def reemplazar_vocales(cadena):
    # Aquí vamos a guardar el nuevo texto sin vocales
    resultado = ""  
    # Recorremos cada letra de la cadena
    for letra in cadena:  
        if letra in 'aeiouAEIOU':  # verificamos si la letra es una vocal
            resultado = resultado + "*"  # si se identifica la vocal la cambiamos por un *
        else:
            resultado = resultado + letra  # validamos si no es vocal, de deja igual
    return resultado  # Devolvemos el texto con los cambios

# Pedimos  que escriba una frase
texto = input("Escribe un texto: ")

# Llamamos la función y guardamos el resultado
nuevo_texto = reemplazar_vocales(texto)

# Mostramos el resultado final
print("Texto con vocales reemplazadas:")
print(nuevo_texto)