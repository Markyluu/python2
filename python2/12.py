def calcular_mediana(lista):
    lista_ordenada = sorted(lista)
    tamanho = len(lista_ordenada)

    if tamanho % 2 == 0:
        indice_meio1 = tamanho // 2 - 1
        indice_meio2 = tamanho // 2
        mediana = (lista_ordenada[indice_meio1] + lista_ordenada[indice_meio2]) / 2
    else:
        indice_meio = tamanho // 2
        mediana = lista_ordenada[indice_meio]

    return mediana

# Exemplo de uso
numeros = [6, 3, 9, 1, 5, 2, 8, 4, 7]
mediana_resultado = calcular_mediana(numeros)

print("A mediana dos números é:", mediana_resultado)
