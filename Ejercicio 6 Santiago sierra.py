# Ejercicio 6: Encontrar el Máximo y Mínimo

def encontrar_max_min(numeros):
    numeros_lista = list(map(int, numeros.split()))
    max_num = max(numeros_lista)
    min_num = min(numeros_lista)
    return max_num, min_num

entrada = input()
max_num, min_num = encontrar_max_min(entrada)
print(max_num, min_num)
