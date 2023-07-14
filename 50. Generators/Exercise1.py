"""
Create a generator (stored in the generator variable) that is capable of
returning an infinite sequence of numbers, starting at 1, and returning
a higher consecutive number each time next is called.

==============================================================================

Crea un generador (almacenado en la variable generador) que sea capaz de
devolver una secuencia infinita de números, iniciando desde el 1, y entregando
un número consecutivo superior cada vez que sea llamada mediante next.
"""

def infinite_generator():
    num = 0
    while True:
        num += 1
        yield num

generator = infinite_generator()
    
def generador_infinito():
    num = 0
    while True:
        num += 1
        yield num

generador = generador_infinito()