"""
Create a print function that returns the second list item named points2, inside
the following dictionary.

If the value 300 were to change in the future, the code should work the same to
return the value at that position. To do this, you must refer to the names of
the keys and/or indexes as appropriate.

===============================================================================

Crea una función print que devuelva del segundo item de la lista llamada
points2, dentro del siguiente diccionario.

Si el valor 300 cambiara en el futuro, el código debería funcionar igual para
devolver el valor que se encuentre en esa misma posición. Para ello, hacer
referencia a los nombres de las claves y/o índices según corresponda.
"""

my_dict = {"values_1":{"v1":3,"v2":6},"points":{"points1":9,"points2":[10,300,15]}}
print(my_dict['points']['points2'][1])
print("************")
mi_dict = {"valores_1":{"v1":3,"v2":6},"puntos":{"points1":9,"points2":[10,300,15]}}
print(mi_dict['puntos']['points2'][1])