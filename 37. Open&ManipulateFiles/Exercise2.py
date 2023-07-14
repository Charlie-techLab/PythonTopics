"""
Print the first line of the file text.txt.

Don't forget to open the file and close it after running your code.

Note: the file is saved in the same folder where your code is stored.

============================================================================

Imprime la primera línea del archivo texto.txt.

No olvides abrir el archivo y cerrarlo luego de ejecutar tu código.

Nota: el archivo se encuentra guardado en la misma carpeta donde se aloja tu
código.
"""

my_file = open("text.txt")
print(my_file.readline())

my_file.close()

print("*"*64)

mi_archivo = open("texto.txt")
print(mi_archivo.readline())

mi_archivo.close()