# Exercício 10: Ler um arquivo CSV e imprimir o conteúdo
# Enunciado: Escreva uma função que recebe o nome de um arquivo CSV como entrada, lê o conteúdo do arquivo e imprime cada linha separadamente.

import csv

arquivo = 'arquivo a ser lido-tp1-10.csv' # arquivo csv se encontra na mesma pasta do código
def leitura_csv(arquivo_lido):
    try:
        with open(arquivo_lido, mode = 'r', encoding='utf-8') as arquivo:
            leitura = csv.reader(arquivo)
            for linha in leitura:
                print(linha)
    except FileNotFoundError:
        print(f"Arquivo '{arquivo_lido}' não encontrado.")
    except Exception as e:
        print(f"Erro {e}")
        
leitura_csv(arquivo) 