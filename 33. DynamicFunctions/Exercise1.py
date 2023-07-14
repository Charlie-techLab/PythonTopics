"""
Create a function (all_positives) that takes a list of numbers as a parameter,
and returns True if all the values in a list are positive, and False if at
least one of the values is negative. Creates a list called list_numbers with
positive and negative values.

Don't call the function, you just need to define it.

==============================================================================

Crea una función (todos_positivos) que reciba una lista de números como
parámetro, y devuelva True si todos los valores de una lista son positivos,
y False si al menos uno de los valores es negativo. Crea una lista llamada
lista_numeros con valores positivos y negativos.

No invoques la función, solo es necesario definirla.
"""

numbers_list = [1, -50, 502, -5000, 755, 600, 33, 61]

def all_positives(numbers_list):
    for n in numbers_list:
        if n < 0:
            return False
        else:
            pass
    return True

lista_numeros = [1, -50, 502, -5000, 755, 600, 33, 61]

def todos_positivos(lista_numeros):
    for n in lista_numeros:
        if n < 0:
            return False
        else:
            pass
    return True