"""
Takes every third character starting from the ninth to the end of the sentence,
and print the result.

"Never trust a computer you can't throw out a window".

===============================================================================

Toma cada tercer caracter empezando desde el noveno hasta el final de la frase,
e imprime el resultado.

"Nunca confíes en un ordenador que no puedas lanzar por una ventana".
"""

phrase = "Never trust a computer you can't throw out a window"
fragment = phrase[8::3]
print(fragment)

print("************")
frase = "Nunca confíes en un ordenador que no puedas lanzar por una ventana"
fragmento = frase[8::3]
print(fragmento)