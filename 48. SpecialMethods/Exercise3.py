"""
Given the Book class, implement the special method __del__ so that the user
is informed with the message "Book deleted", displaying it on the screen
each time the book is deleted.

==============================================================================

Dada la clase Libro, implementa el método especial __del__ para que el usuario
sea informado con el mensaje "Libro eliminado", mostrándolo en pantalla cada
vez que el libro se elimine.
"""

class Book():
    def __init__(self, title, author, number_pages):
        self.title = title
        self.author = author
        self.number_pages = number_pages

    def __del__(self):
        print("Book deleted")

class Libro():
    def __init__(self, titulo, autor, cantidad_paginas):
        self.titulo = titulo
        self.autor = autor
        self.cantidad_paginas = cantidad_paginas

    def __del__(self):
        print("Libro eliminado")