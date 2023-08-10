def contar_ocorrencias_palavras(texto):
    palavras = texto.lower().split()
    contador = {}

    for palavra in palavras:
        if palavra.isalnum():
            if palavra in contador:
                contador[palavra] += 1
            else:
                contador[palavra] = 1

    return contador

# Exemplo de uso
texto_input = input("Digite um texto: ")
resultado = contar_ocorrencias_palavras(texto_input)

print("Ocorrências de palavras no texto:")
for palavra, ocorrencias in resultado.items():
    print(f"{palavra}: {ocorrencias}")
