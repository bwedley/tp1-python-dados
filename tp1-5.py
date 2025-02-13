# Exercício 5: Inverter chaves e valores de um dicionário
# Enunciado: Escreva uma função que recebe um dicionário como entrada e retorna um novo dicionário onde as chaves e
# os valores estão invertidos, ou seja, os valores se tornam chaves e as chaves se tornam valores.

dicionario = {1: "first", 2: "second", 3: "third", 4: "fourth"}
novo_dicionario = dict(zip(dicionario.values(), dicionario.keys()))
print(novo_dicionario) #{'first': 1, 'second': 2, 'third': 3, 'fourth': 4}