"""
We have seen in the lesson how error handling is commonly implemented in
Python. In the case of this exercise, however, I'll need us to do it in
a slightly different way so that it can be evaluated: you'll need to
implement it INSIDE the function. In the form of a comment, you will see
an example resolution. Keep in mind, however, that the preferred form is
the one we have seen in class.

Implement an error handler for the following quotient() function:

In the event of a type error (TypeError), the message must be printed on
the screen: "The arguments to be entered must be numbers".

If a division by zero is generated (error of type ZeroDivisionError),
the message displayed should be: "The second argument must not be zero".

If an error does not occur, it should simply print the result of the
quotient (division) between the two numbers given as argument.

==============================================================================

Hemos visto en la lección de qué manera se implementa el manejo de errores
habitualmente en Python. En el caso de este ejercicio, sin embargo, necesitaré
que lo hagamos de una forma ligeramente distinta para que pueda ser evaluado:
deberás implementarlo DENTRO de la función. En forma de comentario, verás un
ejemplo de resolución. Ten presente, sin embargo, que la forma preferida es
la que hemos visto en clase.

Implementa para la siguiente función cociente(), un manejador de errores:

Ante un error de tipo (TypeError), debe imprimir en pantalla el mensaje:
"Los argumentos a ingresar deben ser números".

Si se generara una división por cero (error del tipo ZeroDivisionError),
el mensaje mostrado debe ser: "El segundo argumento no debe ser cero".

En caso que no se produzca un error, deberá limitarse a imprimir el resultado
del cociente (división) entre los dos números entregados como argumento.
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

def quotient(num1,num2):
    try:  
        print(num1/num2)
    except TypeError:
        print("The arguments to be entered must be numbers")
    except ZeroDivisionError:
        print("The second argument must not be zero")

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

def cociente(num1,num2):
    try:  
        print(num1/num2)
    except TypeError:
        print("Los argumentos a ingresar deben ser números")
    except ZeroDivisionError:
        print("El segundo argumento no debe ser cero")