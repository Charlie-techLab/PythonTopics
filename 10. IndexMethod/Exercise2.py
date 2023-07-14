"""
Finds and displays the index of the first occurrence of the word "practice" in
the following sentence:

"In theory, theory and practice are the same. In practice, they are not."

===============================================================================

Encuentra y muestra en pantalla el índice de la primera aparición de la palabra
"práctica" en la siguiente frase:

"En teoría, la teoría y la práctica son los mismos. En la práctica, no lo son."
"""

phrase = """In theory, theory and practice are the same. In practice, they are 
not."""
result = phrase.index("practice")
print(result)
print("************")
frase = """En teoría, la teoría y la práctica son los mismos. En la práctica, 
no lo son."""
resultado = frase.index("práctica")
print(resultado)