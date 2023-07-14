"""
Create a function called error_log() that opens (open) a file specified as a
parameter, and updates it by adding a line at the end that says "an execution
error has been logged". Finally, you should close the open file.

==============================================================================

Crea una función llamada registro_error() que abra (open) un archivo indicado
como parámetro, y lo actualice añadiendo una línea al final que indique "se ha
registrado un error de ejecución". Finalmente, debe cerrar el archivo abierto.
"""

def log_error(file):
    file = open(file, "a")
    return file.write("se ha registrado un error de ejecución")
    archivo.close()

def registro_error(archivo):
    archivo = open(archivo, "a")
    return archivo.write("se ha registrado un error de ejecución")
    archivo.close()