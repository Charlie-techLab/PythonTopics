"""
Create a generator (stored in the generator variable) that is capable of
returning multiples of 7 indefinitely, starting from 7 itself, and that
each time it is called it returns the next multiple (7, 14, 21, 28... ).

=========================================================================

Crea un generador (almacenado en la variable generador) que sea capaz de
devolver de manera indefinida múltiplos de 7, iniciando desde el mismo 7,
y que cada vez que sea llamado devuelva el siguiente múltiplo 
(7, 14, 21, 28...).
"""

def multiples_seven_generator():
    num = 0
    while True:
        num += 7
        yield num
    
generator = multiples_seven_generator()

def generador_multiplos_siete():
    num = 0
    while True:
        num += 7
        yield num
    
generador = generador_multiplos_siete()