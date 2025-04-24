# realizar las importaciones de las funciones
# segun las 4 variables vistas
# hacer print a la ejecucion de las funciones importadas

import operaciones
print(operaciones.suma(2,3))
print(operaciones.resta(2,3))
print(operaciones.multiplicacion(2,3))
print(operaciones.division(2,3))
print(operaciones.division_piso(2,3))

from operaciones import suma
print(suma(5,7))

import operaciones as op
print(op.multiplicacion(8,9))

from operaciones import *
print(division(5,7))

from operaciones import numero_aleatorio
print(numero_aleatorio())

from operaciones import modulo
print(modulo(4,9))