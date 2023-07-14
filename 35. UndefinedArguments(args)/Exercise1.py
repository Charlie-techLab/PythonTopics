"""
Create a function called sum_squares that takes any number of numeric
arguments, and returns the sum of their squared values.

For example, for the arguments sum_squares(1,2,3) it must return 14 (1+4+9).

==============================================================================

Crea una función llamada suma_cuadrados que tome una cantidad indeterminada de
argumentos numéricos, y que retorne la suma de sus valores al cuadrado.

Por ejemplo para los argumentos suma_cuadrados(1,2,3) deberá retornar
14 (1+4+9).
"""

def sum_squares(*args):
    power = 0
    
    for arg in args:
        power += arg**2
    return power

def suma_cuadrados(*args):
    potencia = 0
    
    for arg in args:
        potencia += arg**2
    return potencia