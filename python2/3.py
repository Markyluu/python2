def imprimir_numeros_naturais(n):
    if n < 0:
        print("O número deve ser positivo.")
        return
    
    for i in range(n + 1):
        print(i, end=" ")

try:
    numero = int(input("Digite um número inteiro positivo: "))
    imprimir_numeros_naturais(numero)
except ValueError:
    print("Entrada inválida. Por favor, digite um número inteiro positivo.")