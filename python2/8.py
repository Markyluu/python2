def encontrar_maior_menor_palavra(lista_palavras):
    if not lista_palavras:
        return None, None
    
    maior_palavra = menor_palavra = lista_palavras[0]
    
    for palavra in lista_palavras:
        if len(palavra) > len(maior_palavra):
            maior_palavra = palavra
        if len(palavra) < len(menor_palavra):
            menor_palavra = palavra
    
    return maior_palavra, menor_palavra

# Exemplo de uso
num_palavras = int(input("Quantas palavras você deseja inserir? "))
lista_de_palavras = []

for i in range(num_palavras):
    palavra = input(f"Digite a palavra {i+1}: ")
    lista_de_palavras.append(palavra)

maior, menor = encontrar_maior_menor_palavra(lista_de_palavras)

if maior is not None and menor is not None:
    print(f"A maior palavra é: {maior}")
    print(f"A menor palavra é: {menor}")
else:
    print("A lista de palavras está vazia.")
