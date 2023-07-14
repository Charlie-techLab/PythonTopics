"""
Create a throw_arrow() instance method that subtracts by -1 the number of
arrows a Character instance has, which has an instance attribute of type
number called number_arrows.

============================================================================

Crea un método de instancia lanzar_flecha() que reste en -1 la cantidad de
flechas que tiene una instancia de Personaje, que cuenta con un atributo de
instancia de tipo número, llamado cantidad_flechas.
"""

class Character:
    def __init__(self, number_arrows):
        self.number_arrows = number_arrows
    
    def throw_arrow(self):
        self.number_arrows = self.number_arrows - 1        

class Personaje:
    def __init__(self, cantidad_flechas):
        self.cantidad_flechas = cantidad_flechas
    
    def lanzar_flecha(self):
        self.cantidad_flechas = self.cantidad_flechas - 1