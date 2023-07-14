"""
Create a static method breathe() for the Pet class. When called, it should
print to the screen "Inhale...Exhale".

===============================================================================

Crea un método estático respirar() para la clase Mascota. Cuando se llame, debe
imprimir en pantalla "Inhalar... Exhalar".
"""

class Pet:
    @staticmethod
    def breathe():
        print("Inhale... Exhale")

Pet.respirar()

class Mascota:
    @staticmethod
    def respirar():
        print("Inhalar... Exhalar")

Mascota.respirar()