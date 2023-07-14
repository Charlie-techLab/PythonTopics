"""
"The platypus is one of the rarest creatures in the world: although it is a
mammal, it lays eggs; and it nurses its young but they do not have breasts."
(National Geographic)

Create a Platypus class that inherits from other classes: Vertebrate, Fish,
Reptile, Bird, and Mammal, such that you "build" an animal that has the
following methods and attributes:

- lay_eggs()

- has_beak = True

-vertebrate = True

- poisonous = True

- swim()

- walk()

- nurse()

============================================================================

"El ornitorrinco es una de las criaturas más raras del mundo: aunque es un
mamífero, pone huevos; y amamanta a sus crías pero no tienen mamas."
(National Geographic)

Crea una clase Ornitorrinco que herede de otras clases: Vertebrado, Pez,
Reptil, Ave y Mamifero, tal que "construyas" un animal que tiene los
siguientes métodos y atributos:

- poner_huevos()

- tiene_pico = True

- vertebrado = True

- venenoso = True

- nadar()

- caminar()

- amamantar()
"""

class Vertebrate:
    vertebrate = True

class Bird(Vertebrate):
    has_beak = True
    def lay_eggs(self):
        print("Laying eggs")

class Reptile(Vertebrate):
    poisonous = True

class Fish(Vertebrate):
    def swim(self):
        print("Swimming")
    def lay_eggs(self):
        print("Laying eggs")

class Mammal(Vertebrate):
    def walk(self):
        print("Walking")
    def nurse(self):
        print("Nursing youngs")

class Platypus(Bird, Reptile, Fish, Mammal):
    pass 

class Vertebrado:
    vertebrado = True

class Ave(Vertebrado):
    tiene_pico = True
    def poner_huevos(self):
        print("Poniendo huevos")

class Reptil(Vertebrado):
    venenoso = True

class Pez(Vertebrado):
    def nadar(self):
        print("Nadando")
    def poner_huevos(self):
        print("Poniendo huevos")

class Mamifero(Vertebrado):
    def caminar(self):
        print("Caminando")
    def amamantar(self):
        print("Amamantando crías")

class Ornitorrinco(Ave, Reptil, Pez, Mamifero):
    pass 