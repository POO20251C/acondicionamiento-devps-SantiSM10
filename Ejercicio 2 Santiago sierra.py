# Ejercicio 2: Contar vocales en una cadena

def contar_vocales(texto):
    vocales = "aeiouAEIOU"
    contador = sum(1 for letra in texto if letra in vocales)
    return contador

# Entrada del usuario
texto = input()
# Salida del resultado
print(contar_vocales(texto))
