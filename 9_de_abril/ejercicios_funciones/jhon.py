'''
Crear una función que reciba una cadena y reemplace todas las vocales por `*`.
pista: usar un bucle for y usar if
'''

# Creamos una funcion para reemplazar las vocales
# def reemplazar_vocales(cadena):
#     # Aqui vamos a guardar el nuevo texto sin vocales
#     resultado = ""  
#     # Recorremos cada letra de la cadena
#     for letra in cadena:  
#         if letra in 'aeiouAEIOU':  # verificamos si la letra es una vocal
#             resultado = resultado + "*"  # si se identifica la vocal la cambiamos por un *
#         else:
#             resultado = resultado + letra  # validamos si no es vocal, de deja igual
#     return resultado  # Devolvemos el texto con los cambios

# # Pedimos  que escriba una frase
# texto = input("Escribe un texto: ")

# # Llamamos la funcion y guardamos el resultado
# nuevo_texto = reemplazar_vocales(texto)
# # Mostramos el resultado final
# print("Texto con vocales reemplazadas:")
# print(nuevo_texto)


# Escribir una funcion que reciba una lista de palabras y retorne la longitud promedio de esas palabras

# Creamos una funcion que recibe una lista de palabras

def longitud_promedio(lista_palabras):
    
# guardamos la suma de las longitudes de todas las palabras
    
    suma = 0  
    
# Hacemos un for para recorer cada palabra en la lista
    
    for palabra in lista_palabras:
        
        suma = suma + len(palabra)  # con len() tenemos la longitud de cada palabra y luego la sumamos 

# Calculamos el promedio: sumamos el total dividido entre la cantidad de palabras agregadas
    
    promedio = suma / len(lista_palabras)
    
    return promedio  # Devolvemos el promedio

# Creamos la lista de palabras

mis_palabras = ["python", "me", "gusta","es" "genial"]

# Llamamos la función y guardamos el resultado

resultado = longitud_promedio(mis_palabras)

# Tiramos el resultado

print("La longitud promedio es:", resultado)




