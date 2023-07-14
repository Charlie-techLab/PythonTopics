"""
Use the writelines method to write the values from the following list to the
end of the "log.txt" file. Insert a tab between each list item to separate
them.

record_last_session = ["Federico", "20/12/2021", "08:17:32 hs",
"No loading errors"]

Prints the entire content of "log.txt" upon completion.

Hint: remember that the symbol to concatenate a tab in a string is \t.
Also, you must close the file in write mode and reopen it in read mode
in order to print its contents.

===============================================================================

Utiliza el método writelines para escribir los valores de la siguiente lista al
final del archivo "registro.txt" . Inserta un tabulador entre cada elemento de
la lista para separarlos.

registro_ultima_sesion = ["Federico", "20/12/2021", "08:17:32 hs",
"Sin errores de carga"]

Imprime el contenido completo de "registro.txt" al finalizar.

Pista: recuerda que el símbolo para concatenar un tabulador en un string es \t.
También, deberás cerrar el archivo en modo escritura y volverlo a abrir en modo
lectura para poder imprimir su contenido.
"""

file = open('log.txt', 'a')

last_session_log = ["Federico", "20/12/2021", "08:17:32 hs", 
                    "No loading errors"]

for data in last_session_log:
    file.writelines(data + '\t')
    
file.close()

file = open("log.txt", "r")

print(file.read())

print("*"*12)

archivo = open('registro.txt', 'a')

registro_ultima_sesion = ["Federico", "20/12/2021", "08:17:32 hs",
                          "Sin errores de carga"]

for dato in registro_ultima_sesion:
    archivo.writelines(dato + '\t')
    
archivo.close()

archivo = open("registro.txt", "r")

print(archivo.read()) 