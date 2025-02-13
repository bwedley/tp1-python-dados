# Exercício 7: União, interseção e diferença de conjuntos
# Enunciado: Escreva uma função que recebe dois conjuntos e retorna um dicionário contendo três chaves:
# "união" representando a união dos conjuntos, "interseção" representando a interseção dos conjuntos e
# "diferença" representando os elementos que estão no primeiro conjunto, mas não no segundo.
conj1 = {1, 2, 3, 4, 5}
conj2 = {4, 5, 6, 7, 8}

def conjuntos(conj1, conj2):
    operacao = {
        "união": conj1.union(conj2),
        "interseção": conj1.intersection(conj2),
        "diferença": conj1.difference(conj2)
    }
    return operacao

print(conjuntos(conj1, conj2))