# Ejercicio 5: Contar Palabras en una Cadena

def contar_palabras(cadena):
    palabras = cadena.split()
    return len(palabras)

texto = input()
print(contar_palabras(texto))
