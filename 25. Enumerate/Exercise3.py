"""
Print on the screen only the indices of those names in the list below,
beginning with M:

names_list = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta",
"Darío", "Emiliano", "Melisa"]

You can solve it in different ways, but it will help to keep in mind all
or some of the following elements:

loops

if conditionals

The enumerate() method

String or indexing methods

==========================================================================

Imprime en pantalla únicamente los índices de aquellos nombres de la lista
a continuación, que empiecen con M:

lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta",
"Darío", "Emiliano", "Melisa"]

Puedes resolverlo de diferentes maneras, pero servirá que tengas presente
todos o algunos de los siguientes elementos:

Loops

Condicionales if

El método enumerate()

Métodos de strings o indexado
"""

names_list = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta",
              "Darío", "Emiliano", "Melisa"]

for index, name in enumerate(names_list):
    if name.startswith("M"):
        print(index)

print("*"*24)

lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta",
                 "Darío", "Emiliano", "Melisa"]

for indice, nombre in enumerate(lista_nombres):
    if nombre.startswith("M"):
        print(indice)