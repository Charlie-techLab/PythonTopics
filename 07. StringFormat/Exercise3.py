"""
Show the user the number of points accumulated within the following sentence:

You have earned (new_points) points! In total, you accumulate (total_points)
points.

On this occasion, the amount of accumulated points (total) will be equal to
the old_points plus the new_points.

Remember that the precision of your answer (spaces, spelling and punctuation)
is very important to reach the correct result.

==============================================================================

Muestra al usuario la cantidad de puntos acumulados dentro de la siguiente
frase:

Has ganado (puntos_nuevos) puntos! En total, acumulas (puntos_totales) puntos.

En esta ocasión, la cantidad de puntos acumulados (totales) será igual a los
puntos_anteriores más los puntos_nuevos.

Recuerda que la precisión de tu respuesta (espacios, ortografía y puntuación),
es muy importante para llegar al resultado correcto.
"""

puntos_anteriores = 875
puntos_nuevos = 350
puntos_totales = puntos_anteriores + puntos_nuevos

print(f'''Has ganado {puntos_nuevos} puntos! En total, acumulas {puntos_totales}
puntos''')

print("*"*64)

previous_points = 875
new_points = 350
total_points = 1225

print(f'''You have earned {new_points} points! In total, you accumulate
{total_points} points''')