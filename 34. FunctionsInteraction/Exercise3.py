import random 

"""
Create a function (called toss_coin) that returns the result of a (random) coin
toss. Such a function must be able to return the results "Face" or "Cross", and
must not receive any arguments to function.

Create a second function (called test_luck), which takes two arguments: the
first must be the result of the coin toss. The second argument will be any list
of numbers (you must create a list with values and call it list_numbers).

If given a "Face", it should display the message to the user: "The list will
self-destruct", and delete it (return it as empty list[]).

If you are given a "Cross", it should print to the screen: "The list was saved"
and return the list intact.

Hints: Uses the random library's choice method to pick an element at random
from a sequence.

===============================================================================

Crea una función (llamada lanzar_moneda) que devuelva el resultado de lanzar
una moneda (al azar). Dicha función debe poder devolver los resultados
"Cara" o "Cruz", y no debe recibir argumentos para funcionar.

Crea una segunda función (llamada probar_suerte), que tome dos argumentos:
el primero, debe ser el resultado del lanzamiento de la moneda. El segundo
argumento, será una lista de números cualquiera (debes crear una lista con
valores y llamarla lista_numeros).

Si se le proporciona una "Cara", debe mostrar el mensaje al usuario: 
"La lista se autodestruirá", y eliminarla (devolverla como lista vacía []).

Si se le proporciona una "Cruz", debe imprimir en pantalla: 
"La lista fue salvada" y devolver la lista intacta.

Pistas: utiliza el método choice de la biblioteca random para elegir un
elemento al azar de una secuencia.
"""

numbers_list = [1, 2, 3, 4]

def toss_coin():
    coin = random.choice(['Face', 'Cross'])
    return coin
    
def test_luck(coin, numbers_list):
    if coin == 'Face':
        print("The list will self-destruct")
        return []
    else:
        print("The list was saved")
        return numbers_list

lista_numeros = [1, 2, 3, 4]

def lanzar_moneda():
    moneda = random.choice(['Cara', 'Cruz'])
    return moneda
    
def probar_suerte(moneda, lista_numeros):
    if moneda == 'Cara':
        print("La lista se autodestruirá")
        return []
    else:
        print("La lista fue salvada")
        return lista_numeros