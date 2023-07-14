"""
Display phrases like the following example on the screen:

The capital of Germany is Berlin.

Use the zip function, loops, and the following lists of countries and capitals
to solve it quickly and efficiently.

capitals = ["Berlin", "Tokyo", "Paris", "Helsinki", "Ottawa", "Canberra"]
countries = ["Germany", "Japan", "France", "Finland", "Canada", "Australia"]

==============================================================================

Muestra en pantalla frases como la del siguiente ejemplo:

La capital de Alemania es Berlín.

Utiliza la función zip, loops, y las siguientes listas de países y capitales
para resolverlo rápida y eficientemente.

capitales = ["Berlín", "Tokio", "París", "Helsinki", "Ottawa", "Canberra"]
paises = ["Alemania", "Japón", "Francia", "Finlandia", "Canadá", "Australia"]
"""

capitals = ["Berlin", "Tokyo", "Paris", "Helsinki", "Ottawa", "Canberra"]
countries = ["Germany", "Japan", "France", "Finland", "Canada", "Australia"]

countries_and_capitals = list(zip(countries, capitals))

for country, capital in countries_and_capitals:
    print(f'The capital of {country} is {capital}.')
    

print("*"*40)

capitales = ["Berlín", "Tokio", "París", "Helsinki", "Ottawa", "Canberra"]
paises = ["Alemania", "Japón", "Francia", "Finlandia", "Canadá", "Australia"]

paises_y_capitales = list(zip(paises, capitales))

for pais, capital in paises_y_capitales:
    print(f'La capital de {pais} es {capital}.')