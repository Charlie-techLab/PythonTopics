"""
You have three classes of characters in a game, which have their specific
methods of innovation.

Create an iterator that achieves a conjugate innovation in the following
order: Inventor, Researcher, Scientist, by calling the innovate() method
of each character. You'll need to instantiate each of the above classes
to build an iterable (a list called characters) that can be traversed in
that order.

==============================================================================

Cuentas con tres clases de personajes en un juego, los cuales cuentan con sus
métodos de innovar específicos.

Crea un iterador que logre una innovación conjugada en el siguiente orden:
Inventor, Investigador, Científico, llamando al método innovar() de cada
uno de los personajes.

Deberás crear instancias de cada una de las clases anteriores para construir
un iterable (una lista llamada personajes) que pueda recorrese en dicho orden.
"""

class Inventor():
    def innovate(self):
        print("Invent")

class Researcher():
    def innovate(self):
        print("Research")

class Scientist():
    def innovate(self):
        print("Discover")
        
DaVinci = Inventor()
Feifeili= Researcher()
IsaacNewton = Scientist()

characters = [DaVinci, Feifeili, IsaacNewton]

for character in characters:
    character.innovate()

print("*"*12)

class Inventor():
    def innovar(self):
        print("Inventar")

class Investigador():
    def innovar(self):
        print("Investigar")

class Cientifico():
    def innovar(self):
        print("Descubrir")
        
davinci = Inventor()
feifeili= Investigador()
isaacnewton = Cientifico()

personajes = [davinci, feifeili, isaacnewton]

for personaje in personajes:
    personaje.innovar()