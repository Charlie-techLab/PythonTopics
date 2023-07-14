import re

"""
Create a function called verify_email to check if an email address is correct,
that checks if the email given as an argument contains "@" (between the
username and the domain) and ends in ".com" (although also accepting cases that
have an additional domain, such as ".com.br" in the case of a user from
Brazil).

If the pattern is found, the function must finish displaying the message "Ok"
on the screen, but if it detects that the phrase does not contain the indicated
elements, it must inform the user "The email address is incorrect" by printing
the message.

===============================================================================

Crea una función llamada verificar_email para comprobar si una dirección de
email es correcta, que verifique si el email dado como argumento contiene "@"
(entre el nombre de usuario y el dominio) y finaliza en ".com" (aunque
aceptando también casos que cuentan con un dominio adicional, tal como
".com.br" para el caso de un usuario de Brasil).

Si se encuentra el patrón, la función debe finalizar mostrando en pantalla el
mensaje "Ok", pero si detecta que la frase no contiene los elementos indicados,
debe informarle al usuario "La dirección de email es incorrecta" imprimiendo el
mensaje.
"""

def check_email(email):
    pattern = r'\w+\@\w+\.com|D{2}'
    check = re.search(pattern,email)
    if check:
        print("Ok")
    else:
        print("The email address is incorrect")
         
def verificar_email(email):
    patron = r'\w+\@\w+\.com|D{2}'
    verificar = re.search(patron,email)
    if verificar:
        print("Ok")
    else:
        print("La dirección de email es incorrecta")