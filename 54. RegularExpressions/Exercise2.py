import re

"""
Create a function called check_greeting to check if a sentence passed as an
argument starts with the word "Hello". If the pattern is found, the function
should terminate by displaying the message "Ok", but if it detects that the
sentence does not contain "Hello", it should inform the user "You didn't say
hello" by printing the message on the screen.

===============================================================================

Crea una función llamada verificar_saludo para verificar si una frase entregada
como argumento inicia con la palabra "Hola". Si se encuentra el patrón, la
función debe finalizar mostrando el mensaje "Ok", pero si detecta que la frase
no contiene "Hola", debe informarle al usuario "No has saludado" imprimiendo el
mensaje en pantalla.
"""

def check_greeting(phrase):
    pattern = r'^Hello'
    check = re.search(pattern, phrase)
    if check:
        print("Ok")
    else:
        print("You didn't say hello")
        
def verificar_saludo(frase):
    patron = r'^Hola'
    verificar = re.search(patron, frase)
    if verificar:
        print("Ok")
    else:
        print("No has saludado")