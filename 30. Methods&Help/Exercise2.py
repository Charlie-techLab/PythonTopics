"""
Add the element "orange" as the fourth element of the following list "fruits",
using the insert() method:

fruits = ["mango", "banana", "cherry", "plum", "grapefruit"]

Search the documentation about the operation of the requested method to find
out how it works and how it functions.

==============================================================================

Añade el elemento "naranja" como el cuarto elemento de la siguiente lista
"frutas", utilizando el método insert():

frutas = ["mango", "banana", "cereza", "ciruela", "pomelo"]

Busca en la documentación acerca del funcionamiento del método solicitado para
saber cómo actúa y cómo es su funcionamiento.
"""

fruits = ["mango", "banana", "cherry", "plum", "grapefruit"]
fruits.insert(3, "orange")
print(fruits)

print("*"*64)

frutas = ["mango", "banana", "cereza", "ciruela", "pomelo"] 
frutas.insert(3, "naranja")
print(frutas)