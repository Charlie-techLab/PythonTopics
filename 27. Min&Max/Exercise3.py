"""
Using the max(), min() and dictionary methods, get the minimum value from the
following dictionary:

ages_dictionary = {"Carlos":55, "María":42, "Mabel":78, "José":44,
"Lucas":24, "Rocío":35, "Sebastián":19, "Catalina":2 ,"Dario":49}

Store this value in a variable called minimum_age.

Also, get the name that comes last in alphabetical order, and store it in a
variable named last_name.

=============================================================================

Utilizando max(), min() y métodos de diccionarios, obtén el mínimo valor a
partir del siguiente diccionario:

diccionario_edades = {"Carlos":55, "María":42, "Mabel":78, "José":44,
"Lucas":24, "Rocío":35, "Sebastián":19, "Catalina":2,"Darío":49}

Almacena dicho valor en una variable llamada edad_minima.

También, obtén el nombre que se ubica último en orden alfabético, y almacénalo
en una variable llamada ultimo_nombre.
"""

ages_dictionary = {"Carlos":55, "María":42, "Mabel":78, "José":44,
                      "Lucas":24, "Rocío":35, "Sebastián":19, "Catalina":2,
                      "Darío":49}
minimum_age = min(ages_dictionary.values())
last_name = max(ages_dictionary)

diccionario_edades = {"Carlos":55, "María":42, "Mabel":78, "José":44,
                      "Lucas":24, "Rocío":35, "Sebastián":19, "Catalina":2,
                      "Darío":49}
edad_minima = min(diccionario_edades.values())
ultimo_nombre = max(diccionario_edades)