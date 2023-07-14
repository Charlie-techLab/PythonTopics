"""
Create a class called Pet, which has the following instance attributes: age,
name, number_paws. Create another class, Dog, that inherits its attributes
from the first.

============================================================================

Crea una clase llamada Mascota, que tenga los siguientes atributos de
instancia: edad, nombre, cantidad_patas. Crea otra clase, Perro, que
herede de la primera sus atributos.
"""

class Pet:
    def __init__(self, age, name, number_paws):
        self.age = age
        self.name = name
        self.number_paws = number_paws
        
class Dog(Pet):
    pass

class Mascota:
    def __init__(self, edad, nombre, cantidad_patas):
        self.edad = edad
        self.nombre = nombre
        self.cantidad_patas = cantidad_patas
        
class Perro(Mascota):
    pass