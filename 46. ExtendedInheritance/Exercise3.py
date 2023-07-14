"""
A son has inherited all his characteristics from his father, however, they
have different hobbies. Make the Child class inherit all of its methods
and attributes from Parent by overriding the hobby() method so that it
returns [1]: "I play video games in my spare time".

[1]: make sure to use return followed by a string

==============================================================================

Un hijo ha heredado de su padre todas sus características, sin embargo, tienen
diferentes hobbies. Logra que la clase Hijo herede de Padre todos sus métodos
y atributos, sobreescribiendo el método hobby() para que se devuelva[1]:
"Juego videojuegos en mi tiempo libre".

[1]: asegúrate de utilizar return seguido de una cadena de texto
"""

class Father():
    eye_color = "brown"
    hair_type = "curly"
    height = "average"
    voice = "deep"
    favorite_sport = "tennis"
    def laugh(self):
        return "Ha ha ha"
    def hobby(self):
        return "I paint wood in my free time"
    def walk(self):
        return "Walking with long and fast steps"
        
class Son(Father):
    def hobby(self):
        return "I play video games in my spare time"

class Padre():
    color_ojos = "marrón"
    tipo_pelo = "rulos"
    altura = "media"
    voz = "grave"
    deporte_preferido = "tenis"
    def reir(self):
        return "Jajaja"
    def hobby(self):
        return "Pinto madera en mi tiempo libre"
    def caminar(self):
        return "Caminando con pasos largos y rápidos"
        
class Hijo(Padre):
    def hobby(self):
        return "Juego videojuegos en mi tiempo libre"