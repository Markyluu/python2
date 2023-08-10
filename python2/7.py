def calcular_fatorial(numero):
    if numero < 0:
        return None
    elif numero == 0 or numero == 1:
        return 1
    else:
        fatorial = 1
        for i in range(2, numero + 1):
            fatorial *= i
        return fatorial

# Exemplo de uso
numero_input = int(input("Digite um número inteiro: "))
fatorial_resultado = calcular_fatorial(numero_input)

if fatorial_resultado is not None:
    print(f"O fatorial de {numero_input} é: {fatorial_resultado}")
else:
    print("O fatorial não está definido para números negativos.")
