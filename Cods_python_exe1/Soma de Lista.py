# Função recursiva que calcula a soma de todos os elementos de uma lista
def soma_lista(lista):

    # Caso base:
    # Se a lista estiver vazia, retorna 0
    if len(lista) == 0:
        return 0

    else:
        # Chamada recursiva:
        # Soma o primeiro elemento da lista
        # com a soma dos demais elementos
        return lista[0] + soma_lista(lista[1:])


# Exemplo de uso da função
# Soma todos os números da lista
print(f"Soma da lista [1,3,5,7,9] = {soma_lista([1,3,5,7,9])}")

# Saída esperada:
# Soma da lista [1,3,5,7,9] = 25