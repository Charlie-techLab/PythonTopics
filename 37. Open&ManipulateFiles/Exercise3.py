"""
Open the text.txt file and print only the second line.

================================================================

Abre el archivo texto.txt e imprime únicamente la segunda línea.
"""

my_file = open("text.txt")

lines = my_file.readlines()
print(lines[1])

print("*"*64)

mi_archivo = open("texto.txt")

lineas = mi_archivo.readlines()
print(lineas[1])