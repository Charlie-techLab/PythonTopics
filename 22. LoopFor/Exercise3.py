"""
Given the following list of numbers, perform the sum of all even and odd*
numbers separately in the variables sum_even and sum_odd respectively:

numbers_list = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]

*Remembering from the previous days: the module (or remainder) of a number
divided by 2 is zero when said value is even, and 1 when it is odd.

num % 2 == 0 (even values)

num % 2 == 1 (odd values)

==============================================================================

Dada la siguiente lista de números, realiza la suma de todos los números pares
e impares* por separado en las variables suma_pares y suma_impares
respectivamente:

lista_numeros = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]

*Recordando de los días anteriores: el módulo (o resto) de un número dividido 2
es cero cuando dicho valor es par, y 1 cuando es impar.

num % 2 == 0 (valores pares)

num % 2 == 1 (valores impares)
"""

numbers_list = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]
sum_evens = 0
sum_odds = 0 

for number in numbers_list:
    if number %2 == 0:
        sum_evens = sum_evens + number
    else:
        sum_odds = sum_odds + number

lista_numeros = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]
suma_pares = 0
suma_impares = 0 

for numero in lista_numeros:
    if numero %2 == 0:
        suma_pares = suma_pares + numero
    else:
        suma_impares = suma_impares + numero