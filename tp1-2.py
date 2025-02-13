# Exercício 2: Remover elementos duplicados mantendo a ordem
# Enunciado: Dada uma lista contendo elementos repetidos, escreva uma função que retorna uma nova lista sem elementos duplicados,
# mantendo a ordem original dos elementos conforme aparecem na lista de entrada.
lista = [1, 2, 3, 2, 4, 1]
def remover_elementos_dup(lista):
    item_unico = []
    for item in lista:
        if item not in item_unico:
            item_unico.append(item)
    return item_unico

print(remover_elementos_dup(lista))