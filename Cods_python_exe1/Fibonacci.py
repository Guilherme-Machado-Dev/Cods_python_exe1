# Função recursiva que calcula o n-ésimo termo da sequência de Fibonacci
def fibonacci(n):

    # Caso base:
    # Se n for 0, retorna 0
    if n == 0:
        return 0

    # Caso base:
    # Se n for 1, retorna 1
    elif n == 1:
        return 1

    else:
        # Chamada recursiva:
        # O valor atual é a soma dos dois termos anteriores
        return fibonacci(n - 1) + fibonacci(n - 2)


# Exemplo de uso da função
# Calcula o 6º termo da sequência de Fibonacci
print(f"Fibonacci(6) = {fibonacci(6)}")

# Saída esperada:
# Fibonacci(6) = 8