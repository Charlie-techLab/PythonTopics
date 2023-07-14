"""
Check if the words stored in the following variables:

word1 = "success", and

word2 = "technology"

are not found in the sentence below, and stores the result of this check 
(a boolean) in a variable called my_bool:

"When something is important enough, you do it even if the odds are not with
you"

Elon Musk

============================================================================

Verifica si las palabras almacenadas en las siguientes variables:

palabra1 = "éxito", y

palabra2 = "tecnología"

no se encuentran en la frase a continuación, y almacena el resultado de esta
comprobación (un booleano) en una variable llamada mi_bool:

"Cuando algo es lo suficientemente importante, lo haces incluso si las
probabilidades de que salga bien no te acompañan"

Elon Musk
"""

phrase = """When something is important enough, you do it even if the odds are
not with you"""
word1 = "success"
word2 = "technology"

my_bool = not(word1 in phrase and word2 in phrase)

frase = """Cuando algo es lo suficientemente importante, lo haces incluso si
las probabilidades de que salga bien no te acompañan"""
palabra1 = "éxito"
palabra2 = "tecnología"

mi_bool = not(palabra1 in frase and palabra2 in frase)