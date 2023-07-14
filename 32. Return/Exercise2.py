"""
Create a function called usd_to_eur that takes as its only parameter a numeric
value (an amount in US dollars), and returns the equivalent amount in euros as
its result. For the purposes of this example, we will take the conversion 
1 USD = 0.90 EUR.

Create a variable called dollars and store any amount in it to pass to your
function and evaluate its result.

Hint: to perform the conversion, the function internally must multiply this
dollar value by 0.90 to get the equivalent amount in euros.

==============================================================================

Crea una función llamada usd_a_eur que tome como único parámetro un valor
numérico (un monto en dólares estadounidenses), y devuelva como resultado
el monto equivalente en euros. A fines de este ejemplo, tomaremos la
conversión 1 USD = 0.90 EUR.

Crea una variable llamada dolares y almacena en ella un monto cualquiera para
entregárselo a tu función y evaluar su resultado.

Pista: para realizar la conversión, la función internamente debe multiplicar
este valor en dólares por 0.90 para obtener el monto equivalente en euros.
"""

dollars = 55
def usd_to_eur(dollars):
    euros = dollars * 0.90
    return euros

dolares = 55
def usd_a_eur(dolares):
    euros = dolares * 0.90
    return euros