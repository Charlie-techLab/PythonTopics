"""
Create a function called describe_person, which takes its name and then any
number of arguments as its parameters. This function should display on the
screen:

Characteristics of {name}:
{argument_name}: {argument_value}
{argument_name}: {argument_value}
etc...

For example:

describe_person("Mary", eye_color="blue", hair_color="blonde")

It will display on the screen:

Characteristics of Maria:
eye_color: blue
hair_color: blond

==============================================================================

Crea una función llamada describir_persona, que tome como parámetros su nombre
y luego una cantidad indeterminada de argumentos. Esta función deberá mostrar
en pantalla:

Características de {nombre}:
{nombre_argumento}: {valor_argumento}
{nombre_argumento}: {valor_argumento}
etc...

Por ejemplo:

describir_persona("María", color_ojos="azules", color_pelo="rubio")

Mostrará en pantalla:

Características de María:
color_ojos: azules
color_pelo: rubio
"""

def describe_person(name, **kwargs):
    print(f'Characteristics of {name}:')
    for argument_name, argument_value in kwargs.items():
        print(f'{argument_name}: {argument_value}')

def describir_persona(nombre, **kwargs):
    print(f'Características de {nombre}:')
    for nombre_argumento, valor_argumento in kwargs.items():
        print(f'{nombre_argumento}: {valor_argumento}')