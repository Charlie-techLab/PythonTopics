import re

"""
The postal code for a given region is formed from two alphanumeric characters
and four numeric characters after it (example: XX1234). Create a function,
called verify_zc to check if the zip code passed as an argument follows this
pattern. If the pattern is correct, show the user the message "Ok", otherwise:
"The entered postal code is not correct".

==============================================================================

El código postal de una región determinada se forma a partir de dos caracteres
alfanuméricos y cuatro numéricos a continuación (ejemplo: XX1234). Crea una
función, llamada verificar_cp para comprobar si el código postal pasado como
argumento sigue este patrón. Si el patrón es correcto, mostrar al usuario el
mensaje "Ok", de lo contrario: "El código postal ingresado no es correcto".
"""

def verify_zc(zc):
    pattern = r'\w{2}\d{4}'
    check = re.search(pattern, zc)
    if check:
        print("Ok")
    else:
        print("The entered postal code is not correct")

def verificar_cp(cp):
    patron = r'\w{2}\d{4}'
    verificar = re.search(patron, cp)
    if verificar:
        print("Ok")
    else:
        print("El código postal ingresado no es correcto")