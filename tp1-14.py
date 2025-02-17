# Exercício 14: Processar um arquivo CSV e criar um dicionário de cidades para nomes
# Enunciado: Escreva uma função que recebe um arquivo CSV contendo colunas de nome e cidade. 
# Observações:
# A função deve retornar um dicionário onde as chaves são as cidades e os valores são listas contendo os nomes das pessoas que pertencem a cada cidade.

import csv
arquivo = 'arquivo-tp1-14.csv' # arquivo csv se encontra na mesma pasta do código
def processar_arquivo_criar_dicionario(arquivo_processado):
    cidades = {}

    try:
        with open(arquivo_processado, mode='r', encoding='utf-8') as arquivo:
            leitura = csv.reader(arquivo)
            next(leitura)
            for linha in leitura:
                nome, cidade = linha[0], linha[1]
                if cidade in cidades:
                    cidades[cidade].append(nome)
                else:
                    cidades[cidade] = [nome]
            return cidades
    except FileNotFoundError:
        print(f"Arquivo '{arquivo_processado}' não encontrado")
    except Exception as e:
        print(f"Erro {e}")

print(processar_arquivo_criar_dicionario(arquivo))