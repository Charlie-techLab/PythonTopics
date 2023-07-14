"""
Create an instance of the Alarm class, which has a method called
postponed(amount_minutes). The method should print the message on
the screen:

"The alarm has been postponed {number_minutes} minutes".

============================================================================

Crea una instancia de la clase Alarma, que tenga un método llamado
postergar(cantidad_minutos). El método debe imprimir en pantalla el mensaje:

"La alarma ha sido pospuesta {cantidad_minutos} minutos".
"""

class Alarm:
    def postpone(self, number_minutes):
        print(f"The alarm has been postponed {number_minutes} minutos")

class Alarma:
    def postergar(self, cantidad_minutos):
        print(f"La alarma ha sido pospuesta {cantidad_minutos} minutos")