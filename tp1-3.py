# Exercício 3: Ordenação personalizada de uma lista de tuplas 
# Enunciado: Dada uma lista de tuplas onde cada tupla contém um nome e uma idade, escreva uma função que ordene a lista com base na idade, da menor para a maior.
lista = [("Bruno", 31), ("Laura", 28), ("Ana", 24), ("Carem", 26)]
def ordenacao_tupla_idade(lista):
    return sorted(lista, key=lambda x: x[1])

print(ordenacao_tupla_idade(lista))
