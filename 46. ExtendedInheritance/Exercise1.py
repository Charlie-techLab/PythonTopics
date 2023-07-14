"""
If the Daughter class has inherited from her father the way of laughing,
and from her mother the vocation, and today they have the same job in the
Prosecutor's Office, create multiple inheritance that allows this class to
correctly inherit from Father and Mother.

Fill in the code provided below to achieve this.

============================================================================

Si la clase Hija ha heredado de su padre la forma de reir, y de su madre la
vocación, y hoy tienen el mismo trabajo en la Fiscalía, crea la herencia
múltiple que le permita a esta clase heredar correctamente de Padre y Madre.

Completa el código suministrado a continuación para lograrlo.
"""

class Father():
    def work(self):
        print("Working at Hospital")

    def laugh(self):
        print("Ha ha ha!")

class Mother():
    def work(self):
        print("Working at Prosecutor's Office")
        
class Daughter(Mother, Father):
    pass

class Padre():
    def trabajar(self):
        print("Trabajando en el Hospital")

    def reir(self):
        print("Ja ja ja!")

class Madre():
    def trabajar(self):
        print("Trabajando en la Fiscalía")
        
class Hija(Madre,Padre ):
    pass