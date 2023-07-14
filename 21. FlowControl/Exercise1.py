"""
Using the variables num1 and num2, which are fed with user input (just like in
the code already provided):

Create a control flow structure that compares the values of the variables, and
returns a result accordingly:

"num1 is greater than num2".

"num2 is greater than num1".

"num1 and num2 are equal".

You must display on the screen the value of the entered variables instead of
num1 and num2.

===============================================================================

Utilizando las variables num1 y num2, que se alimentan con el input del usuario
(tal como en el código ya proporcionado):

Crea una estructura de control de flujo que compare los valores de las
variables, y arroje un resultado de acuerdo al caso:

"num1 es mayor que num2".

"num2 es mayor que num1".

"num1 y num2 son iguales".

Debes mostrar en pantalla el valor de las variables ingresadas en lugar de num1
y num2.
"""

num1 = input("Enter a number:")
num2 = input("Enter another number:")

f"{num1} is greater than {num2}"
"num2 is greater than num1"
"num1 and num2 are equal"

if num1 > num2:
    print(f"{num1} is greater than {num2}")
elif num1 < num2:
    print(f"{num2} is greater than {num1}")
else:
    print(f"{num1} and {num2} are equal")

print("************************")

num1 = input("Ingresa un número:")
num2 = input("Ingresa otro número:")

f"{num1} es mayor que {num2}"
"num2 es mayor que num1"
"num1 y num2 son iguales"

if num1 > num2:
    print(f"{num1} es mayor que {num2}")
elif num1 < num2:
    print(f"{num2} es mayor que {num1}")
else:
    print(f"{num1} y {num2} son iguales")