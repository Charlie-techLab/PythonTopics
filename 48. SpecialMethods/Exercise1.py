"""
Given the Book class, implement the special method __str__ so that each time
the object is printed, it returns '"{title}", by {author}' (note: the title
must be enclosed in double quotes).

============================================================================

Dada la clase Libro, implementa el método especial __str__ para que cada vez
que se imprima el objeto, devuelva '"{titulo}", de {autor}' (atención: el
título debe estar encerrado entre comillas dobles).
"""

class Book():
    def __init__(self, title, author, number_pages):
        self.title = title
        self.author = author
        self.number_pages = number_pages
        
    def __str__(self):
        return f'"{self.title}" by {self.author}'

class Libro():
    def __init__(self, titulo, autor, cantidad_paginas):
        self.titulo = titulo
        self.autor = autor
        self.cantidad_paginas = cantidad_paginas
        
    def __str__(self):
        return f'"{self.titulo}", de {self.autor}'