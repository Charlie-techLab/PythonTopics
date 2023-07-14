"""
Utiliza la función range() y un loop para sumar los cuadrados de todos los
números del 1 al 15 (inclusive). Almacena el resultado en una variable
llamada suma_cuadrados.

Para ello:

Crea un rango de valores que puedas recorrer en un loop.

Para cada uno de estos valores, calcula su valor al cuadrado (potencia de 2).
Puede que necesites crear variables intermedias (de manera opcional).

Suma todos los valores al cuadrado obtenidos. Acumula la suma en la variable
suma_cuadrados.

=============================================================================

Use the range() function and a loop to add the squares of all numbers from 1
to 15 (inclusive). Store the result in a variable called sum_squares.

For it:

Create a range of values that you can loop through.

For each of these values, find its squared value (power of 2). You may need to
create intermediate variables (optionally).

Add all the squared values obtained. Accumulates the sum in the variable
sum_squares.
"""

sum_squares = 0

for number in range(1, 16):
    squared_value = number **2
    sum_squares += squared_value

suma_cuadrados = 0

for numero in range(1, 16):
    valor_cuadrado = numero **2
    suma_cuadrados += valor_cuadrado