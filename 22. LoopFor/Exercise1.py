"""
Using for loops, greet all members of a class by printing "Hello" + their name.

For example: "Hello Maria".

students_class = ["María", "José", "Carlos", "Martina", "Isabel", "Tomás",
"Daniela"]

===============================================================================

Utilizando loops for, saluda a todos los miembros de una clase, imprimiendo
"Hola" + su nombre.

Por ejemplo: "Hola María".

alumnos_clase = ["María", "José", "Carlos", "Martina", "Isabel", "Tomás",
"Daniela"]
"""

class_students = ["María", "José", "Carlos", "Martina", "Isabel", "Tomás", 
                  "Daniela"]

for students in class_students:
    print(f'Hello {students}')
    
print("*"*40)

alumnos_clase = ["María", "José", "Carlos", "Martina", "Isabel", "Tomás", 
                 "Daniela"]

for alumnos in alumnos_clase:
    print(f'Hola {alumnos}')