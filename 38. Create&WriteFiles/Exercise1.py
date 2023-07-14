"""
Open the file called "my_file.txt", and change its content to the text
"New text".

Print the entire content of "my_file.txt" when finished.

Hint: you will have to close it in write mode and reopen it in read mode.

=============================================================================

Abre el archivo llamado "mi_archivo.txt", y cambia su contenido por el texto
"Nuevo texto".

Imprime el contenido completo de "mi_archivo.txt" al finalizar.

Pista: deberás cerrarlo en modo escritura y volverlo a abrir en modo lectura.
"""

file = open('my_file.txt', 'w')
file.write('New text')

file.close()

file = open('my_file.txt', 'r')
print(file.read())

print("*"*12)

archivo = open('mi_archivo.txt', 'w')
archivo.write('Nuevo texto')

archivo.close()

archivo = open('mi_archivo.txt', 'r')
print(archivo.read())