"""
Substitute in the following sentence:

"If the implementation is hard to explain, it might be a bad idea."

the following word pairs:

"difficult" --> "easy"

"bad" --> "good"

and displays the sentence with both words modified on the screen.

===========================================================================

Reemplaza en la siguiente frase:

"Si la implementación es difícil de explicar, puede que sea una mala idea."

los siguientes pares de palabras:

"difícil" --> "fácil"

"mala" --> "buena"

y muestra en pantalla la frase con ambas palabras modificadas.
"""

text1 = "If the implementation is hard to explain, "
text2 = "it might be a bad idea."
result1 = text1.replace("hard", "easy")
result2 = text2.replace("bad", "good")

print(result1 + result2)

print("**********************************************************************")
texto1 = "Si la implementación es difícil de explicar, "
texto2 = "puede que sea una mala idea."

resultado1 = texto1.replace("difícil", "fácil")
resultado2 = texto2.replace("mala", "buena")

print(resultado1 + resultado2)