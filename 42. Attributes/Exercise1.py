"""
Create a class called House, and assign it attributes: color, number_floors.

Creates a House instance, called white_house, with color "white" and number
of floors equal to 4.

=============================================================================

Crea una clase llamada Casa, y asígnale atributos: color, cantidad_pisos.

Crea una instancia de Casa, llamada casa_blanca, de color "blanco" y cantidad
de pisos igual a 4.
"""

class House:
    
    def __init__(self, color, number_floors):
        self.color = color
        self.cantidad_pisos = number_floors
        
white_house = House('white', 4)

class Casa:
    
    def __init__(self, color, cantidad_pisos):
        self.color = color
        self.cantidad_pisos = cantidad_pisos
        
casa_blanca = Casa('blanco', 4)