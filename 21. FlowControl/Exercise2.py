"""
The laws of a country state that an adult can drive if they have a license to
do so, and to qualify for a driver's license, you must be 18 years of age or
older.

Create a conditional structure to check if a 16-year-old without a license can
drive, and display the corresponding result on the screen:

"You can drive".

"You can't drive yet. You must be 18 years old and have a license".

"You can't drive. You need to have a license".

Uses the already provided code base to set up the appropriate control flow
structure and check those conditions.

==============================================================================

Las leyes de un país establecen que un adulto puede conducir si tiene licencia
para hacerlo, y para optar por una licencia para conducir, debe de tener 18
años o más.

Crea una estructura condicional para verificar si una persona de 16 años sin
licencia puede conducir, y muestra el resultado que corresponda en pantalla:

"Puedes conducir".

"No puedes conducir aún. Debes tener 18 años y contar con una licencia".

"No puedes conducir. Necesitas contar con una licencia".

Utiliza la base de código ya proporcionada para plantear la estructura de
control de flujo apropiada y verificar dichas condiciones.
"""

age = 16
with_license = False

if age >= 18 and with_license == True:
    print("You can drive.")
elif age < 18 and with_license == False:
    print("You can't drive yet. You must be 18 years old and have a license.")
elif with_license == False:
    print("You can't drive. You need to have a license.")

print("**********************************************************************")

edad = 16
tiene_licencia = False

if edad >= 18 and tiene_licencia == True:
    print("Puedes conducir.")
elif edad < 18 and tiene_licencia == False:
    print("No puedes conducir aún. Debes tener 18 años y contar con una licencia.")
elif tiene_licencia == False:
    print("No puedes conducir. Necesitas contar con una licencia.")