from collections import defaultdict

"""
Creates a dictionary called my_dictionary, for which, when a searched keyword 
is not found, it is loaded with the string "Value not found".

Load the dictionary with at least the following data pair:

keyword = age

value = 44

Use the defaultdict method of the Collections module.

=============================================================================

Crea un diccionario llamado mi_diccionario, para el cual, cuando no se halle
una palabra clave buscada, se cargue con el string "Valor no hallado".

Carga el diccionario, al menos, con el siguiente par de datos:

palabra clave = edad

valor = 44

Utiliza el método defaultdict del módulo Collections.
"""

my_dictionary = defaultdict(lambda:"Value not found")
my_dictionary["age"] = 44

mi_diccionario = defaultdict(lambda:"Valor no hallado")
mi_diccionario["edad"] = 44