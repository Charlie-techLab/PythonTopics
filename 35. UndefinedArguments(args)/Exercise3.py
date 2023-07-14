"""
Create a function named person_numbers that receives a name as its first
argument, followed by an indefinite quantity of numbers.

The function should return the following message:

"{name}, the sum of your numbers is {sum_numbers}"

===========================================================================

Crea una función llamada numeros_persona que reciba, como primer argumento,
un nombre, y a continuación, una cantidad indefinida de números.

La función debe devolver el siguiente mensaje:

"{nombre}, la suma de tus números es {suma_numeros}"
"""

def person_numbers(name, *args):
    numbers_sum = sum(args)
    return f"{name}, the sum of your numbers is {numbers_sum}"

def numeros_persona(nombre, *args):
    suma_numeros = sum(args)
    return f"{nombre}, la suma de tus números es {suma_numeros}"  