# Exercício 8: Encontrar elementos únicos em uma lista usando set
# Enunciado: Escreva uma função que recebe uma lista de números e retorna uma nova lista contendo apenas os elementos únicos da lista original, sem manter a ordem.
lista = [1, 2, 3, 4, 5, 3, 4, 2, 4, 5]

def elemenetos_unicos(lista):
    return list(set(lista))

print(elemenetos_unicos(lista))