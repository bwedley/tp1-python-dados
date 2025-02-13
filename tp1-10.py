# Exercício 10: Ler um arquivo CSV e imprimir o conteúdo
# Enunciado: Escreva uma função que recebe o nome de um arquivo CSV como entrada, lê o conteúdo do arquivo e imprime cada linha separadamente.

import csv

def leitura_csv(arquivo_lido):
    try:
        with open(arquivo_lido, mode = 'r', encoding='utf-8') as arquivo:
            leitura = csv.reader(arquivo)
            for linha in leitura:
                print(linha)
    except FileNotFoundError:
        print(f"Arquivo '{arquivo_lido}' não encontrado.")

leitura_csv('arquivo a ser lido-tp1-10.csv') # arquivo csv se encontra na mesma pasta do código