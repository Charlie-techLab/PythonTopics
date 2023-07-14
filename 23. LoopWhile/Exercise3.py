"""
Create a for loop through the following list of numbers, printing each of its
elements to the screen, and break the flow the moment you encounter a negative
value:

numbers_list = [4,5,8,7,6,9,8,2,4,5,7,1,9,5,6,-1,-5,6,-6,-4,-3]

You must not change the order of the list.

==============================================================================

Crea un ciclo for a lo largo de la siguiente lista de números, imprimiendo en
pantalla cada uno de sus elementos, e interrumpe el flujo en el momento que
encuentres un valor negativo:

lista_numeros = [4,5,8,7,6,9,8,2,4,5,7,1,9,5,6,-1,-5,6,-6,-4,-3]

No debes cambiar el orden de la lista.
"""

numbers_list = [4,5,8,7,6,9,8,2,4,5,7,1,9,5,6,-1,-5,6,-6,-4,-3]

for number in numbers_list:
    
    if number > 0:
        print(number)
    else:
        break

lista_numeros = [4,5,8,7,6,9,8,2,4,5,7,1,9,5,6,-1,-5,6,-6,-4,-3]

for numero in lista_numeros:
    
    if numero > 0:
        print(numero)
    else:
        break