# Ejercicio 3: Verificar Palíndromo

def es_palindromo(cadena):
    cadena_limpia = ''.join(cadena.split()).lower()
    if cadena_limpia == cadena_limpia[::-1]:
        return "Sí"
    else:
        return "No"
    
texto = input()
print(es_palindromo(texto))
