"""
To perform the exercise below, you can choose different paths. While the
correct path in programming is the one that returns the correct result,
I encourage you to try applying the concepts of list comprehension to 
start solidifying them for the future. They can be very useful in your
professional practice!

For the following list of temperatures in Fahrenheit, express these same values
in a new list of temperature values in Celsius. The conversion between types of
units is as follows:

°C = (°F - 32) * (5/9)

or expressed in another way:

(degrees_fahrenheit-32)*(5/9)

The temperature list is as follows:

temperature_fahrenheit = [32, 212, 275]
Store this new list in a variable called degrees_celsius.

===============================================================================

Para realizar el ejercicio a continuación, puedes optar por diferentes caminos.
Si bien en programación el camino correcto es el que devuelve el resultado
correcto, te animo a que intentes aplicar los conceptos de comprensión de
listas para comenzar a afianzarlos para el futuro. ¡Pueden resultarte muy
útiles en tu práctica profesional!

Para la siguiente lista de temperaturas en grados Fahrenheit, expresa estos
mismos valores en una nueva lista de valores de temperatura en grados Celsius.
La conversión entre tipo de unidades es la siguiente:

°C = (°F - 32) * (5/9)

o expresado de otro modo:

(grados_fahrenheit-32)*(5/9)

La lista de temperaturas es la siguiente:

temperatura_fahrenheit = [32, 212, 275] 
Almacena esta nueva lista en una variable llamada grados_celsius.
"""

fahrenheit_temperature = [32, 212, 275]

celsius_degrees = [(n - 32) * (5/9) for n in fahrenheit_temperature]
print(celsius_degrees)

print("*"*24)

temperatura_fahrenheit = [32, 212, 275]

grados_celsius = [(n - 32) * (5/9) for n in temperatura_fahrenheit]
print(grados_celsius)