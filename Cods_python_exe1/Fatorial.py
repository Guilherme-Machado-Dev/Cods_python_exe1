# Função recursiva que calcula o fatorial de um número
def fatorial(n):

    # Caso base:
    # O fatorial de 0 e de 1 é igual a 1
    if n == 0 or n == 1:
        return 1

    else:
        # Chamada recursiva:
        # Multiplica o número atual pelo fatorial do número anterior
        return n * fatorial(n - 1)


# Exemplo de uso da função
# Calcula o fatorial de 5
print(f"Fatorial de 5 = {fatorial(5)}")

# Saída esperada:
# Fatorial de 5 = 120