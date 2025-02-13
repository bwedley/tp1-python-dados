# Exercício 9: Testar subconjunto e superconjunto
# Enunciado: Escreva uma função que recebe dois conjuntos como entrada e retorna um valor booleano indicando se o primeiro conjunto é um subconjunto do segundo.
conj1 = {1, 2, 3, 4, 5}
conj2 = {4, 5, 6, 7, 8}

conj1s = {1, 2, 3}
conj2s = {1, 2, 3, 4, 5}

def test_conj(conj1, conj2):
    return conj1.issubset(conj2)

print(test_conj(conj1, conj2))
print(test_conj(conj1s, conj2s))