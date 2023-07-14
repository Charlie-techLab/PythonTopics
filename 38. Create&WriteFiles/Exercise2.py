"""
Open the file called "my_file.txt", and add a line to the end of it that
says: "New login".

Prints the entire content of "my_file.txt" when finished.

Hint: you will have to close it in write mode and reopen it in read mode.

==============================================================================

Abre el archivo llamado "mi_archivo.txt", y añade una línea al final del mismo
que diga: "Nuevo inicio de sesión".

Imprime el contenido completo de "mi_archivo.txt" al finalizar.

Pista: deberás cerrarlo en modo escritura y volverlo a abrir en modo lectura.
"""

archivo = open('mi_archivo.txt', 'a')
archivo.write("Nuevo inicio de sesión")

archivo.close()

archivo = open('mi_archivo.txt', 'r')
print(archivo.read())

archivo = open('mi_archivo.txt', 'a')
archivo.write("Nuevo inicio de sesión")

archivo.close()

archivo = open('mi_archivo.txt', 'r')
print(archivo.read())