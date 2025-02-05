# Ejercicio 4: Invertir una Lista de Números

def invertir_lista(numeros):
    numeros_lista = list(map(int, numeros.split()))
    numeros_lista.reverse()
    return " ".join(map(str, numeros_lista))

entrada = input()
print(invertir_lista(entrada))
