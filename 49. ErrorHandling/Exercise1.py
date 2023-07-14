"""
We have seen in the lesson how error handling is commonly implemented in
Python. In the case of this exercise, however, I'll need us to do it in
a slightly different way so that it can be evaluated: you'll need to
implement it INSIDE the function. In the form of a comment, you will see
an example resolution. Keep in mind, however, that the preferred form is
the one we have seen in class.

Implement for the following function sum(), a simple error handler that,
upon any error, prints the message: "Unexpected error" on the screen.
Otherwise, it should limit itself to displaying the result of the sum 
between the two numbers.

==============================================================================

Hemos visto en la lección de qué manera se implementa el manejo de errores
habitualmente en Python. En el caso de este ejercicio, sin embargo, necesitaré
que lo hagamos de una forma ligeramente distinta para que pueda ser evaluado:
deberás implementarlo DENTRO de la función. En forma de comentario, verás un
ejemplo de resolución. Ten presente, sin embargo, que la forma preferida es la
que hemos visto en clase.

Implementa para la siguiente función suma(), un manejador de errores simple que
ante cualquier error, imprima en pantalla el mensaje: "Error inesperado". En
caso contrario, deberá limitarse a mostrar el resultado de la suma entre los
dos números.
"""

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

def sum(num1,num2):
    try:
        print(num1+num2)
    except:
        print("Unexpected error")

def suma(num1,num2):
    try:
        print(num1+num2)
    except:
        print("Error inesperado")