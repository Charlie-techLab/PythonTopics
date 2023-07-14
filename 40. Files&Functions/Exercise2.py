"""
Create a function called overwrite() that opens (open) a file given as a
parameter, and overwrites any previous content with the text "content removed".

===============================================================================

Crea una función llamada sobrescribir() que abra (open) un archivo indicado
como parámetro, y sobrescriba cualquier contenido anterior por el texto
"contenido eliminado".
"""

def overwrite(file):
    file = open(file, "w")
    return file.write("contenido eliminado")

def sobrescribir(archivo):
    archivo = open(archivo, "w")
    return archivo.write("contenido eliminado")