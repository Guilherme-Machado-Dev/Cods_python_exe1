# Função recursiva que conta quantas vezes um elemento
# aparece dentro de uma lista (vetor)
def conta_ocorrencia(vet, elemento):

    # Caso base:
    # Se a lista estiver vazia, não há ocorrências
    if len(vet) == 0:
        return 0

    # Verifica se o primeiro elemento da lista
    # é igual ao elemento procurado
    if vet[0] == elemento:

        # Soma 1 à contagem e continua procurando
        # no restante da lista
        return 1 + conta_ocorrencia(vet[1:], elemento)

    else:

        # Se não encontrou no primeiro elemento,
        # continua a busca no restante da lista
        return conta_ocorrencia(vet[1:], elemento)


# Exemplo de uso da função:
# Conta quantas vezes o número 3 aparece na lista
print(f"Ocorrências de 3 em [1,3,5,3,7,3] = {conta_ocorrencia([1,3,5,3,7,3], 3)}")
# Saída esperada: 3