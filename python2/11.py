import random

def jogo_adivinhacao():
    numero_secreto = random.randint(1, 100)
    tentativas = 0
    limite_tentativas = 10

    print("Bem-vindo ao jogo de adivinhação! Tente adivinhar o número entre 1 e 100.")

    while tentativas < limite_tentativas:
        tentativa = int(input("Digite sua tentativa: "))
        tentativas += 1

        if tentativa < numero_secreto:
            print("Tente um número maior.")
        elif tentativa > numero_secreto:
            print("Tente um número menor.")
        else:
            print(f"Parabéns! Você acertou o número em {tentativas} tentativas.")
            break

    if tentativas >= limite_tentativas:
        print(f"Suas {tentativas} tentativas acabaram. O número era {numero_secreto}.")

jogo_adivinhacao()
