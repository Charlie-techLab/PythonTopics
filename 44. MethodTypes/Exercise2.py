"""
Create a revive() class method that acts on the alive class attribute of the
Player class, setting it to True each time it is called. The default value
of the live attribute must be False.

==============================================================================

Crea un método de clase revivir() que actúa sobre el atributo de clase vivo de
la clase Jugador, estableciéndolo en True cada vez que es invocado. El valor
predeterminado del atributo vivo, debe ser False.
"""

class Player:
    alive = False
    @classmethod
    def revive(cls):
        cls.alive = True

class Jugador:
    vivo = False
    @classmethod
    def revivir(cls):
        cls.vivo = True