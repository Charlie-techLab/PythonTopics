"""
Create a class called Person, which has the following instance attributes:
name, age. Create another class, Student, that inherits these attributes
from the first.

==========================================================================

Crea una clase llamada Persona, que tenga los siguientes atributos de
instancia: nombre, edad. Crea otra clase, Alumno, que herede de la
primera estos atributos.
"""

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
class Student(Person):
    pass

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        
class Alumno(Persona):
    pass