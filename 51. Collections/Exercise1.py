from collections import Counter

"""
Apply a Counter to the list of numbers given below, and store it in a variable
called counter.

==============================================================================

Aplica un Counter (contador) sobre la lista de números entregada a 
continuación, y almacénalo en una variable llamada contador.
"""

list = [1, 2, 3, 6, 7, 1, 2, 4, 5, 5, 5, 5, 3, 2, 6, 7]

counter = Counter(list)
print(counter)

print("*"*51)

lista = [1, 2, 3, 6, 7, 1, 2, 4, 5, 5, 5, 5, 3, 2, 6, 7]

contador = Counter(lista)
print(contador)