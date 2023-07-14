"""
You have three classes of characters in a game, all of which have their
specific defense methods.

Create a function called character_defender(), which can receive an object
(an instance of your character classes), and call its defend() method
regardless of what kind of character it is.

==========================================================================

Tienes tres clases de personajes en un juego, los cuales cuentan con sus
métodos de defensa específicos.

Crea una función llamada personaje_defender(), que pueda recibir un objeto
(una instancia de las clases de tus personajes), y ejecutar su método
defender() independientemente de qué tipo de personaje se trate.
"""

class Defender():
    def defend(self):
        print("Mark and sweep")

class Goalkeeper():
    def defend(self):
        print("Watch out the goal")

class Midfielder():
    def defend(self):
        print("Back off and block attacks")
        
robertocarlos = Defender()
iker = Goalkeeper()
zidane = Midfielder()

characters = [robertocarlos, iker, zidane]

def character_defender(character):
    character.defender()

print("*"*12)

class Defensa():
    def defender(self):
        print("Marcar y barrer")

class Arquero():
    def defender(self):
        print("Proteger portería")

class Centrocampista():
    def defender(self):
        print("Bajar y bloquear ataques")
        

robertocarlos = Defensa()
iker = Arquero()
zidane = Centrocampista()

personajes = [robertocarlos, iker, zidane]

def personaje_defender(personaje):
    personaje.defender()