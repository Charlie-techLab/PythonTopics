"""
Create a function called count_attribute that counts the number of parameters
that are passed, and returns that number as the result.

=============================================================================

Crea una función llamada cantidad_atributos que cuente la cantidad de 
parámetros que se entregan, y devuelva esa cantidad como resultado.
"""

def count_attribute(**kwargs):
    quantity = 0
    for key, value in kwargs.items():
        quantity += 1
        
    return quantity
    
def cantidad_atributos(**kwargs):
    cantidad = 0
    for clave, valor in kwargs.items():
        cantidad += 1
        
    return cantidad