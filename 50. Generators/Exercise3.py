"""
Create a generator that subtracts the lives of a video game character one by
one, and returns a message each time it is called:

"You have 3 lives left".

"You have 2 lives left".

"You have 1 life left".

"Game Over".

Store the generator in the lose_life variable.

==============================================================================

Crea un generador que reste una a una las vidas de un personaje de videojuego,
y devuelva un mensaje cada vez que sea llamado:

"Te quedan 3 vidas".

"Te quedan 2 vidas".

"Te queda 1 vida".

"Game Over".

Almacena el generador en la variable perder_vida.
"""

def lives_game():
    lives_number = "You have 3 lives left"
    yield lives_number
    
    lives_number = "You have 2 lives left"
    yield lives_number
    
    lives_number = "You have 1 live left"
    yield lives_number
    
    lives_number = "Game Over"
    yield lives_number
    
lose_life = lives_game()

def vidas_juego():
    cantidad_vidas = "Te quedan 3 vidas"
    yield cantidad_vidas
    
    cantidad_vidas = "Te quedan 2 vidas"
    yield cantidad_vidas
    
    cantidad_vidas = "Te queda 1 vida"
    yield cantidad_vidas
    
    cantidad_vidas = "Game Over"
    yield cantidad_vidas
    
    
perder_vida = vidas_juego()