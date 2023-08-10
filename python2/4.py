def eh_palindromo(palavra):
    palavra = ''.join(e for e in palavra if e.isalnum())  # Remover caracteres não alfanuméricos
    palavra = palavra.lower()  # Converter a palavra para minúsculas
    return palavra == palavra[::-1]

palavra_input = input("Digite uma palavra: ")
if eh_palindromo(palavra_input):
    print("A palavra é um palíndromo.")
else:
    print("A palavra não é um palíndromo.")