from pathlib import Path 

"""
Implement and create a relative path that allows us to reach the
"path_practices.py" file from the following folder structure:

PythonCourse -> Day 6 -> path_practices.py

Stores the directory obtained in the path variable. Don't forget
to import Path.

==============================================================================

Implementa y crea una ruta relativa que nos permita llegar al archivo
"practicas_path.py" a partir de la siguiente estructura de carpetas:

CursoPython -> Día 6 -> practicas_path.py

Almacena el directorio obtenido en la variable ruta. No olvides importar Path.
"""

path = Path("PythonCourse", "Day 6", "path_practices.py")
ruta = Path("Curso Python", "Día 6", "practicas_path.py")