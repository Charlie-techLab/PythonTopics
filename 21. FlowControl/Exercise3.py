"""
To access a certain job position, the candidate must be able to program in
Python and have knowledge of English.

Creates a conditional structure to evaluate a candidate given these conditions,
and displays the corresponding message on the screen:

"You meet the requirements to apply".

"To apply, you need to know how to program in Python and have knowledge of
English".

"To apply, you need to have knowledge of English".

"To apply, you need to know how to program in Python".

Use the already provided code base to set up the appropriate control flow
structure and check those conditions. Evaluate a candidate who knows English,
but doesn't program in Python.

===============================================================================

Para acceder a un determinado puesto de trabajo, el candidato debe ser capaz
de programar en Python y tener conocimientos de inglés.

Crea una estructura condicional para evaluar a un candidato dadas estas
condiciones, y muestra el mensaje correspondiente en pantalla:

"Cumples con los requisitos para postularte".

"Para postularte, necesitas saber programar en Python y tener conocimientos de
inglés".

"Para postularte, necesitas tener conocimientos de inglés".

"Para postularte, necesitas saber programar en Python".

Utiliza la base de código ya proporcionada para plantear la estructura de
control de flujo apropiada y verificar dichas condiciones. Evalúa a un
candidato que sabe inglés, pero no programa en Python.
"""

speak_english = True
know_python = False

if speak_english == True and know_python == True:
    print("You meet the requirements to apply.")
elif speak_english == False and know_python == False:
    print("""To apply, you need to know how to program in Python and have
          knowledge of English.""")
elif know_python == True and speak_english == False:
    print("To apply, you need to have knowledge of English.")
elif speak_english == True and know_python == False:
    print("To apply, you need to know how to program in Python.")

print("*"*60)

habla_ingles = True
sabe_python = False

if habla_ingles == True and sabe_python == True:
    print("Cumples con los requisitos para postularte.")
elif habla_ingles == False and sabe_python == False:
    print("""Para postularte, necesitas saber programar en Python y tener
          conocimientos de inglés.""")
elif sabe_python == True and habla_ingles == False:
    print("Para postularte, necesitas tener conocimientos de inglés.")
elif habla_ingles == True and sabe_python == False:
    print("Para postularte, necesitas saber programar en Python.")