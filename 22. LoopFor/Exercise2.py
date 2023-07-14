"""
Given the following list of numbers, perform the sum of all the numbers using
for loops and store the result of the sum in a variable named number_sum:

list_numbers = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]

=============================================================================

Dada la siguiente lista de números, realiza la suma de todos los números
utilizando loops for y almacena el resultado de la suma en una variable
llamada suma_numeros:

lista_numeros = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]
"""

number_list = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]
number_sum = 0

for number in number_list:
    number_sum = number_sum + number
    
lista_numeros = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]
suma_numeros = 0

for numero in lista_numeros:
    suma_numeros = suma_numeros + numero