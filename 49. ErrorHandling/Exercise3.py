"""
We have seen in the lesson how error handling is commonly implemented in
Python. In the case of this exercise, however, I'll need us to do it in
a slightly different way so that it can be evaluated: you'll need to
implement it INSIDE the function. In the form of a comment, you will
see an example resolution. Keep in mind, however, that the preferred
form is the one we have seen in class.

Implement an error handler inside the following function, open_file():

In the event that the file you are trying to open cannot be found
(FileNotFoundError), display the message: "The file was not found".

In case another type of error occurs, display the message: "Unknown error".

If no error occurs, print on screen: "Opening successfully".

In all cases, when finished, print: "Finishing execution".

==============================================================================

Hemos visto en la lección de qué manera se implementa el manejo de errores
habitualmente en Python. En el caso de este ejercicio, sin embargo, necesitaré
que lo hagamos de una forma ligeramente distinta para que pueda ser evaluado:
deberás implementarlo DENTRO de la función. En forma de comentario, verás un
ejemplo de resolución. Ten presente, sin embargo, que la forma preferida es
la que hemos visto en clase.

Implementa un manejador de errores dentro de la siguiente función,
abrir_archivo():

En caso de que el archivo que se intenta abrir no pueda ser hallado
(FileNotFoundError), mostrar en pantalla el mensaje: 
"El archivo no fue encontrado".

En caso de que otro tipo de error ocurra, mostrar el mensaje: 
"Error desconocido".

Si no se produce ningún error, imprimir en pantalla: 
"Abriendo exitosamente".

En todos los casos, al finalizar, imprimir: "Finalizando ejecución".
"""

"""
Resolution example:

def function_name(argument):
     try:
         {What the function would usually do}
     except:
         {Exception}
     else:
         ... etc.
"""

def open_file(file_name):
    try:
        file = open(file_name)
    except FileNotFoundError:
        print("The file was not found")
    except:
        print("Unknown error")
    else:
        print("Opening successfully")
    finally:
        print("Finishing execution")

"""
Ejemplo de resolución:

def nombre_funcion(argumento):
    try:
        {Lo que haría la función habitualmente}
    except:
        {Excepción}
    else:
        ... etc.
"""

def abrir_archivo(nombre_archivo):
    try:
        archivo = open(nombre_archivo)
    except FileNotFoundError:
        print("El archivo no fue encontrado")
    except:
        print("Error desconocido")
    else:
        print("Abriendo exitosamente")
    finally:
        print("Finalizando ejecución")