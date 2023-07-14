"""
Create a function (even_count) that counts the number of even numbers in a
list (numbers_list), and returns the result of that count.

==============================================================================

Crea una función (cantidad_pares) que cuente la cantidad de números pares que
existen en una lista (lista_numeros), y devuelva el resultado de dicha cuenta.
"""

numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18,
                19, 20]

def even_count(numbers_list):
    quantity_even_numbers = 0
    for number in numbers_list:
        if number %2 == 0:
            quantity_even_numbers +=1
    return quantity_even_numbers

lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18,
                 19, 20]

def cantidad_pares(lista_numeros):
    cantidad_numeros_pares = 0
    for numero in lista_numeros:
        if numero %2 == 0:
            cantidad_numeros_pares +=1
    return cantidad_numeros_pares