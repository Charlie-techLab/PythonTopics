"""
Create a function called list_attributes that returns in the form of a list the
values of the attributes given in the form of keywords (keywords). The function
must expect to receive any number of such arguments.

===============================================================================

Crea una función llamada lista_atributos que devuelva en forma de lista los
valores de los atributos entregados en forma de palabras clave (keywords).
La función debe preveer recibir cualquier cantidad de argumentos de este tipo.
"""

def list_attributes(**kwargs):
    list = []
    for key, value in kwargs.items():
        list.append(value)
        
    return list

def lista_atributos(**kwargs):
    lista = []
    for clave, valor in kwargs.items():
        lista.append(valor)
        
    return lista