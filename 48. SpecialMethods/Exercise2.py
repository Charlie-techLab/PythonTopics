"""
Given the Book class, implement the special method __len__ so that each time
the len() function is executed on it, it returns the number of pages as an
integer.

=============================================================================

Dada la clase Libro, implementa el método especial __len__ para que cada vez
que se ejecute la función len() sobre el mismo, devuelva el número de páginas
como número entero.
"""

class Book():
    def __init__(self, title, author, number_pages):
        self.title = title
        self.author = author
        self.number_pages = number_pages

    def __len__(self):
        return self.number_pages

class Libro():
    def __init__(self, titulo, autor, cantidad_paginas):
        self.titulo = titulo
        self.autor = autor
        self.cantidad_paginas = cantidad_paginas

    def __len__(self):
        return self.cantidad_paginas