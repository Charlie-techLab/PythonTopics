from random import choice

"""
Create a function (roll_dice) that rolls two random dice and returns their
results:

The function must return two result values, which are between 1 and 6.

Such a function must not require any arguments to function, but must internally
generate the random values.

Provide the result of these two dice to a function called evaluate_move
(that is, this second function must receive two arguments) and return 
-without printing- a message based on the sum of these values:

If the sum is less than or equal to 6:

"The sum of your dice is {dice_sum}. Sorry."

If the sum is greater than 6 and less than 10:

"The sum of your dice is {dice_sum}. You have a good chance."

If the sum is greater than or equal to 10:

"The sum of your dice is {dice_sum}. It looks like a winning move."

Hints: Use the choice or randint method of the random library to choose a
random value between 1 and 6.

===============================================================================

Crea una función (lanzar_dados) que arroje dos dados al azar y devuelva sus
resultados:

La función debe retornar dos valores resultado, que se encuentren entre 1 y 6).

Dicha función no debe requerir argumentos para funcionar, sino que debe generar
internamente los valores aleatorios.

Proporciona el resultado de estos dos dados a una función que se llame
evaluar_jugada (es decir, esta segunda función debe recibir dos argumentos)
y que retorne -sin imprimirlo- un mensaje según la suma de estos valores:

Si la suma es menor o igual a 6:

"La suma de tus dados es {suma_dados}. Lamentable."

Si la suma es mayor a 6 y menor a 10:

"La suma de tus dados es {suma_dados}. Tienes buenas chances."

Si la suma es mayor o igual a 10:

"La suma de tus dados es {suma_dados}. Parece una jugada ganadora."

Pistas: utiliza el método choice o randint de la biblioteca random para elegir
un valor al azar entre 1 y 6.
"""

numbers = [1, 2, 3, 4, 5, 6 ]

def roll_dice():
     dice1 = choice(numbers)
     dice2 = choice(numbers)
     return dice1, dice2

def evaluate_move(dice1, dice2):
     dice_sum = dice1 + dice2
     if dice_sum <= 6:
         return f"The sum of your dice is {dice_sum}. Sorry."
     elif dice_sum > 6 and dice_sum < 10:
         return f"The sum of your dice is {dice_sum}. You have a good chance."
     elif dice_sum >= 10:
         return f"The sum of your dice is {dice_sum}. It looks like a winning move."

numeros = [1, 2, 3, 4, 5, 6 ]

def lanzar_dados():
    dado1 = choice(numeros)
    dado2 = choice(numeros)
    return dado1, dado2

def evaluar_jugada(dado1, dado2):
    suma_dados = dado1 + dado2
    if suma_dados <= 6:
        return f"La suma de tus dados es {suma_dados}. Lamentable."
    elif suma_dados > 6 and suma_dados < 10:
        return f"La suma de tus dados es {suma_dados}. Tienes buenas chances."
    elif suma_dados >= 10:
        return f"La suma de tus dados es {suma_dados}. Parece una jugada ganadora."