def encontrar_maior_menor_numero(sequencia):
    if not sequencia:
        return None, None
    
    maior = menor = sequencia[0]
    
    for numero in sequencia:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero
    
    return maior, menor

# Função para obter a sequência de números do usuário
def obter_sequencia():
    entrada = input("Digite uma sequência de números separados por espaço: ")
    numeros = [int(num) for num in entrada.split()]
    return numeros

# Exemplo de uso
numeros = obter_sequencia()
maior_numero, menor_numero = encontrar_maior_menor_numero(numeros)

if maior_numero is not None and menor_numero is not None:
    print(f"O maior número é: {maior_numero}")
    print(f"O menor número é: {menor_numero}")
else:
    print("A sequência está vazia.")
