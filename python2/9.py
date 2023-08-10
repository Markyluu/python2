def converter_para_maiusculas(lista_strings):
    return [palavra.upper() for palavra in lista_strings]

# Exemplo de uso
lista_input = input("Digite uma lista de palavras separadas por vírgula: ")
lista_de_strings = lista_input.split(',')

nova_lista_maiusculas = converter_para_maiusculas(lista_de_strings)
print("Lista de palavras em letras maiúsculas:", nova_lista_maiusculas)
