"""
Create the zip with the translations of the numbers from 1 to 5 in Spanish,
Portuguese and English (in the same order), and convert the generated object
into a list stored in the numbers variable:

one / um / one

two / two / two

three / three / three

four / four / four

five / five / five

The result should follow the structure:

[('one', 'um', 'one'), ('two', 'two', 'two'), ... ]

=============================================================================

Crea el zip con las traducciones los números del 1 al 5 en español, portugués
e inglés (en el mismo orden), y convierte el objeto generado en una lista
almacenada en la variable numeros:

uno / um / one

dos / dois / two

tres / três / three

cuatro / quatro / four

cinco / cinco / five

El resultado deberá seguir la estructura:

[('uno', 'um', 'one'), ('dos', 'dois', 'two'), ... ]
"""

spanish_numbers = ['uno', 'dos', 'tres', 'cuatro', 'cinco']
portuguese_numbers = ['um', 'dois', 'três', 'quatro', 'cinco']
english_numbers = ['one', 'two', 'three', 'four', 'five']

numbers = list(zip(spanish_numbers, portuguese_numbers, english_numbers))
print(numbers)

print("*"*131)

numeros_espaniol = ['uno', 'dos', 'tres', 'cuatro', 'cinco']
numeros_portugues = ['um', 'dois', 'três', 'quatro', 'cinco']
numeros_ingles = ['one', 'two', 'three', 'four', 'five']

numeros = list(zip(numeros_espaniol, numeros_portugues, numeros_ingles))
print(numeros)