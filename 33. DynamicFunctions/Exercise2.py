"""
Create a function (sum_minors) that adds the numbers of a list (stored in the
variable numbers_list) as long as they are greater than 0 and less than 1000,
and returns the result of said sum.

=============================================================================

Crea una función (suma_menores) que sume los números de una lista (almacenada
en la variable lista_numeros) siempre y cuando sean mayores a 0 y menores a
1000, y devuelva el resultado de dicha suma.
"""

numbers_list = [1, 50, 500, 5000, 750]

def sum_minors(numbers_list):
    numbers_sum = 0
    for number in numbers_list:
        if number > 0 and number < 1000:
            numbers_sum += number
            
    return numbers_sum

lista_numeros = [1, 50, 500, 5000, 750]

def suma_menores(lista_numeros):
    suma_numeros = 0
    for numero in lista_numeros:
        if numero > 0 and numero < 1000:
            suma_numeros += numero
            
    return suma_numeros