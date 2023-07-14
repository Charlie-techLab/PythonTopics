"""
Print sentences like the following on the screen:

'{name} is found at index {index}'

Where name should be each of the names in the list below, and the index,
obtained by enumerate().

list_names = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta",
"Darío", "Emiliano", "Melisa"]

You can modify the print() line given as an example, but the sentences
returned must be the same.

Tip: use loops!

==============================================================================

Imprime en pantalla frases como la siguiente:

'{nombre} se encuentra en el índice {indice}'

Donde nombre debe ser cada uno de los nombres de la lista a continuación, y el
índice, obtenido mediante enumerate().

lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta",
"Darío", "Emiliano", "Melisa"]

Puedes modificar la línea print() otorgada como ejemplo, pero las frases
entregadas deberán ser iguales.

Tip: utiliza loops!
"""

names_list = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta",
                 "Darío", "Emiliano", "Melisa"]

for index, name in enumerate(names_list):
    print(f'{name} is found at index {index}')

print("*"*40)

lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta",
                 "Darío", "Emiliano", "Melisa"]

for indice, nombre in enumerate(lista_nombres):
    print(f'{nombre} se encuentra en el índice {indice}')
