"""
To perform the exercise below, you can choose different paths. While the
correct path in programming is the one that returns the correct result,
I encourage you to try applying the concepts of list comprehension to
start solidifying them for the future. They can be very useful in your
professional practice!

Creates an even_values list made up of the numbers in the values list that
(you guessed it!) are even.

values = [1, 2, 3, 4, 5, 6, 9.5]

===============================================================================

Para realizar el ejercicio a continuación, puedes optar por diferentes caminos.
Si bien en programación el camino correcto es el que devuelve el resultado
correcto, te animo a que intentes aplicar los conceptos de comprensión de
listas para comenzar a afianzarlos para el futuro. ¡Pueden resultarte muy
útiles en tu práctica profesional!

Crea una lista valores_pares formada por los números de la lista valores que
(¡adivinaste!) sean pares.

valores = [1, 2, 3, 4, 5, 6, 9.5]
"""

values = [1, 2, 3, 4, 5, 6, 9.5]
even_values = [n for n in values if n %2 == 0]
print(even_values)

print("*"*12)

valores = [1, 2, 3, 4, 5, 6, 9.5]
valores_pares = [n for n in valores if n %2 == 0]
print(valores_pares)