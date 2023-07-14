"""
Create a while loop that subtracts one by one the numbers from 50 to 0
(both numbers included) with the following additional conditions:

- If the number is divisible by 5, display that number on the screen
(remember that here you can use the modulo operation dividing by 5 and
checking the remainder!).

- If the number is not divisible by 5, continue executing the loop without
displaying the value on the screen (don't forget to continue subtracting
so that the program does not run infinitely).

==========================================================================

Crea un ciclo while que reste de uno en uno los números desde el 50 al 0
(ambos números incluídos) con las siguientes condiciones adicionales:

- Si el número es divisible por 5, mostrar dicho número en pantalla
(¡recuerda que aquí puedes utilizar la operación módulo dividiendo
por 5 y verificando el resto!).

- Si el número no es divisible por 5, continuar ejecutando el loop sin
mostrar el valor en pantalla (no te olvides de seguir restando para que
el programa no corra infinitamente).
"""

number = 55

while number >= 0:
    number -= 1
    if number %5 == 0:
        print(number)
    else:
        continue
    
numero = 55

while numero >= 0:
    numero -= 1
    if numero %5 == 0:
        print(numero)
    else:
        continue