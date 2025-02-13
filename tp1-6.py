# Exercício 6: Unir dois dicionários somando valores comuns
# Enunciado: Dado dois dicionários contendo chaves e valores numéricos, escreva uma função que retorne um novo dicionário que contenha todas as chaves de ambos os dicionários. 
# Observações:
# Se uma chave estiver presente nos dois dicionários, o valor correspondente no dicionário resultante deve ser a soma dos valores dos dicionários de entrada.

dic1 = {'a': 1, 'b': 2, 'c': 3}
dic2 = {'b': 3, 'c': 4, 'd': 5}

def unir_dicionarios(dic1, dic2):
    novo_dic = {}

    for chave, valor in dic1.items():
        novo_dic[chave] = valor
    
    for chave, valor in dic2.items():
        if chave in novo_dic:
            novo_dic[chave] += valor
        else:
            novo_dic[chave] = valor

    return novo_dic

print(unir_dicionarios(dic1, dic2))