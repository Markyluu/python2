import random

def lancar_dado():
    return random.randint(1, 6)

def main():
    dado1 = lancar_dado()
    dado2 = lancar_dado()

    soma = dado1 + dado2

    print("Dado 1:", dado1)
    print("Dado 2:", dado2)
    print("Soma:", soma)

if __name__ == "__main__":
    main()
