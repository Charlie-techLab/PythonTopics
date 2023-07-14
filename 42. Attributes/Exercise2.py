"""
Create a class called Cube, and assign it the class attribute:

. faces = 6

and the instance attribute:

. color

Creates a red_cube instance of that color.

==============================================================

Crea una clase llamada Cubo, y asígnale el atributo de clase:

. caras = 6

y el atributo de instancia:

. color

Crea una instancia cubo_rojo, de dicho color.
"""

class Cube:
    faces = 6
    def __init__(self, color):
        self.color = color

red_cube = Cube('red')

class Cubo:
    caras = 6
    def __init__(self, color):
        self.color = color

cubo_rojo = Cubo('rojo')