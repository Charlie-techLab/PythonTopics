"""
Create a list made up of the tuples (index, element), formed by obtaining the
indices of each character of the string "Python" through enumerate().

Calls the list obtained with the variable name index_list .

==============================================================================

Crea una lista formada por las tuplas (indice, elemento), formadas a partir de
obtener mediante enumerate() los índices de cada caracter del string "Python".

Llama a la lista obtenida con el nombre de variable lista_indices.
"""

indexes_list = list(enumerate("Python"))

for index, element in enumerate(indexes_list):
    print(index, element)

print("*"*24)

lista_indices = list(enumerate("Python"))

for indice, elemento in enumerate(lista_indices):
    print(indice, elemento)