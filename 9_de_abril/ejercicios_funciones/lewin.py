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

# Escribir una función que reciba una lista de palabras y retorne la longitud promedio de esas palabras

# # Escribir una función que reciba una lista de palabras y retorne la longitud promedio de esas palabras
def longitud_promedio_palabras(lista_palabras):
    if not lista_palabras:
        return 0
    total_caracteres = sum(len(palabra) for palabra in lista_palabras)
    promedio = total_caracteres / len(lista_palabras)
    return promedio

# Ejemplo de uso
entrada = input("Ingrese una lista de palabras separadas por comas: ")
palabras = [palabra.strip() for palabra in entrada.split(",") if palabra.strip()]  # Convierte la entrada en una lista de palabras
print("La longitud promedio de las palabras es:", longitud_promedio_palabras(palabras))

