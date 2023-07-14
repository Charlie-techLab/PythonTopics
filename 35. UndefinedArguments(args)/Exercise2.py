"""
Create a function called sum_absolutes, which takes a set of arguments of any
extension, and returns the sum of their absolute values (i.e., takes the
unsigned values and adds them, or what is the same, considers them all
- negative and positive- as positive)s.

==============================================================================

Crea una función llamada suma_absolutos, que tome un conjunto de argumentos de
cualquier extensión, y retorne la suma de sus valores absolutos (es decir, que
tome los valores sin signo y los sume, o lo que es lo mismo, los considere a
todos -negativos y positivos- como positivos).
"""

def sum_absolutes(*args):
    sum = 0
    
    for arg in args:
        if arg < 0:
            arg *= -1
            sum += arg
        else:
            sum += arg
    
    return sum
    
def suma_absolutos(*args):
    suma = 0
    
    for arg in args:
        if arg < 0:
            arg *= -1
            suma += arg
        else:
            suma += arg
    
    return suma