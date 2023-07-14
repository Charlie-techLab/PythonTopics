"""
Updates the information in our dictionary called my_dic (reassigning new values
to the keys as appropriate), and adds a new key called "country" (without
tilde). The new data is:

name: Hedy

surname: Lamarr

age: 84

occupation: screenwriter, producer...

Country: Austria and United States

to do this, you should not change the line of code already written, but update
the values using dictionary methods.

===============================================================================

Actualiza la información de nuestro diccionario llamado mi_dic  (reasignando
nuevos valores a las claves según corresponda), y agrega una nueva clave
llamada "pais" (sin tilde). Los nuevos datos son:

nombre: Hedy

apellido: Lamarr

edad: 84

ocupacion: guionista, productora...

pais: Austria y Estados Unidos

para ello, no debes cambiar la línea de código ya escrita, sino actualizar los
valores mediante métodos de diccionarios.
"""

my_dic = {'name': 'Hedy', 'surname': 'Lamarr', 'age':84, 'occupation':
    'Inventor and much more...'}
my_dic['age'] = 85
my_dic['occupation'] = 'screenwriter, producer'
my_dic['Country'] = 'Austria and United States'

mi_dic = {"nombre":"Hedy", "apellido":"Lamarr", "edad":84, "ocupacion":
    "guionista, productora"}
mi_dic['edad'] = 85
mi_dic['ocupacion'] = 'guionista, productora...'
mi_dic['pais'] = 'Austria y Estados Unidos'