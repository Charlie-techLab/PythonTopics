from pathlib import Path  

"""
Implement and create an absolute path that allows us to reach the
"path_practices.py" file from the following folder structure:

home (base directory) -> Python Course -> Day 6 -> path_practices.py

Store the directory obtained in the path variable. Don't forget to import
Path, and to concatenate the Path object that refers to the user's home folder.

===============================================================================

Implementa y crea una ruta absoluta que nos permita llegar al archivo
"practicas_path.py" a partir de la siguiente estructura de carpetas:

home (directorio base) -> CursoPython -> Día 6 -> practicas_path.py

Almacena el directorio obtenido en la variable ruta. No olvides importar
Path, y de concatenar el objeto Path que refiere a la carpeta base del usuario.
"""

base = Path.home()
path = Path(base, "Python Course", "Day 6", "path_practices.py")

base = Path.home()
ruta = Path(base, "Curso Python", "Día 6", "practicas_path.py")