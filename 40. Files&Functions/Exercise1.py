"""
Create a function called open_read() that opens (open) a file indicated as a
parameter, and returns its content (read).

==============================================================================

Crea una función llamada abrir_leer() que abra (open) un archivo indicado como
parámetro, y devuelva su contenido (read).
"""

def open_read(file):
    file = open(file)
    return file.read()

def abrir_leer(archivo):
    archivo = open(archivo)
    return archivo.read()