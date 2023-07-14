"""
Create a function called reverse_word that takes the characters of a given word
as an argument, reverses the order of its characters, and returns them that way
and in uppercase.

For example, if we give it the word "Python", it should return: "NOHTYP".

Also, you must create a variable called word, which contains the string that
you prefer, to supply it as an argument to the created function.

Hint: inside the created function, you will have to use already seen string
methods.

===============================================================================

Crea una función llamada invertir_palabra que tome los caracteres de una
palabra dada como argumento, invierta el orden de sus caracteres y los
devuelva de ese modo y en mayúsculas.

Por ejemplo, si le proporcionamos la palabra "Python", deberá devolver: 
"NOHTYP".

También, deberás crear una variable llamada palabra, que contenga el string
que tú prefieras, para suministrarle como argumento a la función creada.

Pista: dentro de la función creada, deberás utilizar métodos de strings ya
vistos.
"""

word = "Python"
def reverse_word(word):
    word_list = list(word)
    word_list.reverse()
    reversed_word = "".join(word_list)
    return reversed_word.upper()

palabra = "Python"
def invertir_palabra(palabra):
    lista_palabra = list(palabra)
    lista_palabra.reverse()
    palabra_invertida = "".join(lista_palabra)
    return palabra_invertida.upper()