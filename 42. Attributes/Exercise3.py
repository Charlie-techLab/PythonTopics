"""
Create a class called Character, and give it the following class attribute:

true = False

Create an instance named ironman with the following instance attributes:

species = "Human"

inventor = True

age = 53

============================================================================

Crea una clase llamada Personaje, y asígnale el siguiente atributo de clase:

real = False

Crea una instancia llamada ironman con los siguientes atributos de
instancia:

especie = "Humano"

inventor = True

edad = 53
"""

class Character:
    real = False
    
    def __init__(self, species, inventor, age):
        self.species = species
        self.inventor = inventor
        self.age = age
        
ironman = Character("Human", True, 53)

class Personaje:
    real = False
    
    def __init__(self, especie, inventor, edad):
        self.especie = especie
        self.inventor = inventor
        self.edad = edad
        
ironman = Personaje("Humano", True, 53)