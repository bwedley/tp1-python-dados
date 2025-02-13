# Exercício 12: Ler um arquivo JSON e retornar um dicionário
# Enunciado: Escreva uma função que recebe o nome de um arquivo JSON como entrada, lê o conteúdo do arquivo e retorna um dicionário representando os dados contidos no arquivo.

import json

arquivo = 'arquivo a ser lido-tp1-12.json'

def ler_arquivo_json(arquivo_lido):
    try:
        with open(arquivo_lido, mode='r', encoding='utf-8') as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        print(f"Arquivo '{arquivo_lido}' não encontrado.")
    
print(ler_arquivo_json(arquivo))