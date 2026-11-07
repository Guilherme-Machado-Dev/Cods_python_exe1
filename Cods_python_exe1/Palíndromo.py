# Função recursiva que verifica se uma palavra é um palíndromo
# (pode ser lida da mesma forma de trás para frente)
def palindromo(palavra):

    # Caso base:
    # Se a palavra tiver 0 ou 1 caractere,
    # ela é considerada um palíndromo
    if len(palavra) <= 1:
        return True

    # Verifica se o primeiro e o último caracteres são diferentes
    # Se forem, a palavra não é um palíndromo
    if palavra[0] != palavra[-1]:
        return False

    # Chamada recursiva:
    # Remove o primeiro e o último caracteres
    # e verifica o restante da palavra
    return palindromo(palavra[1:-1])


# Exemplo de uso da função
# Verifica se a palavra "arara" é um palíndromo
print(f"'arara' é palíndromo? {palindromo('arara')}")

# Saída esperada:
# 'arara' é palíndromo? True