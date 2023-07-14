"""
The built-in function in Python len() has a polymorphic behavior, since it
calculates the length of an object based on its type (strings, lists,
tuples, among others), returning the number of items or characters that
compose it.

Create an iterator that loops through the following objects: word, list,
tuple, and prints (print()) each of its lengths with the len() function.

You can remember how to implement the len() function in the following 
link: https://docs.aws.amazon.com/es_es/redshift/latest/dg/r_LEN.html

============================================================================

La función incorporada en Python len() tiene un comportamiento polimórfico,
ya que calcula el largo de un objeto en función de su tipo (strings, listas,
tuples, entre otros), devolviendo la cantidad de items o caracteres que lo
componen.

Crea un iterador que recorra los siguientes objetos: palabra, lista, tupla y
muestre en pantalla (print()) para cada uno de ellos su longitud con la
función len().

Puedes recordar cómo implementar la función len() siguiente enlace: 
https://docs.aws.amazon.com/es_es/redshift/latest/dg/r_LEN.html
"""

word = "polymorphism"
list = ["Classes", "OOP", "Polymorphism"]
tuple = (1, 2, 3, 80)

for letter in word:
    word_length = len(word)
    
print(word_length)

for word in list:
    list_length = len(list)
    
print(list_length)

for number in tuple:
    tuple_length = len(tuple)
    
print(tuple_length)

print("*"*12)

palabra = "polimorfismo"
lista = ["Clases", "POO", "Polimorfismo"]
tupla = (1, 2, 3, 80)

for letra in palabra:
    longitud_palabra = len(palabra)
    
print(longitud_palabra)

for palabra in lista:
    longitud_lista = len(lista)
    
print(longitud_lista)

for numero in tupla:
    longitud_tupla = len(tupla)
    
print(longitud_tupla)