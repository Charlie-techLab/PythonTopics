from datetime import datetime

"""
In a variable called minutes, store only the minutes of the current time.

For example, if it were to run at 20:43:17 at night, the variable minutes
would store the value 43.

============================================================================

En una variable llamada minutos, almacena únicamente los minutos de la hora
actual.

Por ejemplo, si se ejecutara a las 20:43:17 de la noche, la variable minutos
debe almacenar el valor 43.
"""

today = datetime.now()
minutes = today.minute

hoy = datetime.now()
minutos = hoy.minute