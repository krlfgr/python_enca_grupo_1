


'''
Podemos implementar nuestras propias funciones en Python utilizando la palabra
reservada def
Cuando definimos una función podemos implementar el tratamiento de un parámetro

#definiendo funciones
def <nombre>():
    operaciones
    operaciones
    operaciones
    return respuesta
    
#invocando funciones
nombre()

input("Por favor ingrese un número")
aquello que entregamos a una función para que opere se llama argumentos
Nota: No todas las funciones requieren de argumentos para operar
'''
#1. Definición de la función suma

def suma():
    x=20
    y=8
    z=x+y
    return z


#2. Invocar o llamar a la función
print(suma())

#2 ejemplo

def suma_2(x,y):
    z=x+y
    
    return z

print(suma_2(5,15)) #Invoca a la función con dos argumentos

variable1=50
variable2=40

print(suma_2(variable1,variable2)) #90

#Una función que retorna múltiples cosas
def funcion_multiple(x,y,z,w):
    w+=3
    return x**2, y/2, z//3


#Llamado
print(funcion_multiple(4,20,8,5))


#Una función con parametros opcionales
def funcion_opcionales(dato1,dato2=20,dato3=100):
    dato1 + dato2
    return dato3

print(funcion_opcionales(20))
