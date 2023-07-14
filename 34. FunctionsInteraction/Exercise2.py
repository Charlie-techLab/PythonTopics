"""
Create a function called reduce_list() that takes a list as an argument
(also creates the variable numbers_list), and returns the same list, but
eliminating duplicates (leaving only one of the numbers if there are
duplicates) and eliminating the highest value. The order of the elements
can be changed.

For example, if given the list [1,2,15,7,2] it should return [1,2,7].

Create a function called average() that can receive as an argument the list
returned by the previous function, and that calculates the average of its
values. It should return the result, without printing it.

===========================================================================

Crea una función llamada reducir_lista() que tome una lista como argumento
(crea también la variable lista_numeros), y devuelva la misma lista, pero
eliminando duplicados (dejando uno solo de los números si hay repetidos)
y eliminando el valor más alto. El orden de los elementos puede modificarse.

Por ejemplo, si se le proporciona la lista [1,2,15,7,2] debe devolver [1,2,7].

Crea una función llamada promedio() que pueda recibir como argumento la lista
devuelta por la anterior función, y que calcule el promedio de los valores de
la misma. Debe devolver el resultado, sin imprimirlo.
"""

numbers_list = [1, 2, 15, 7, 2]

def reduce_list(numbers_list):
    list = list(set(numbers_list))
    list.sort()
    list.pop()
    return list
 
def average(list):
    average = sum(list)/len(list)
    return average

lista_numeros = [1, 2, 15, 7, 2]

def reducir_lista(lista_numeros):
    lista = list(set(lista_numeros))
    lista.sort()
    lista.pop()
    return lista
 
def promedio(lista):
    promedio = sum(lista)/len(lista)
    return promedio