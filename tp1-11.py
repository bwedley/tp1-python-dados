# Exercício 11: Escrever dados em um arquivo CSV
# Enunciado: Escreva uma função que recebe o nome de um arquivo CSV e uma lista de dicionários, onde cada dicionário representa uma linha do arquivo. 
# Observações:
# A função deve criar e escrever os dados no arquivo CSV, incluindo os cabeçalhos.

import csv

arquivo_escrito = 'arquivo a ser escrito-tp1-11.csv' # arquivo csv vai ser criado na mesma pasta do código

def escrever_dados(arquivo_lido, lista_dict):
    try:
        with open(arquivo_lido, mode='w', encoding='utf-8') as arquivo:
            escrever_csv = csv.DictWriter(arquivo, fieldnames=lista_dict[0])
            escrever_csv.writeheader()
            escrever_csv.writerows(lista_dict)

        print(f"Dados foram escritos no arquivo '{arquivo_lido}' com sucesso")
    except FileNotFoundError:
        print(f"Arquivo '{arquivo_lido}' não encontrado.")
    except Exception as e:
        print(f"Erro {e}")

dados = [
    {'Carro': 'Gol', 'Placa': 'JXW2E28', 'Dono': 'Roberto'},
    {'Carro': 'Punto', 'Placa': 'ASC3F12', 'Dono': 'Jorge'},
    {'Carro': 'Hilux', 'Placa': 'NWE9X34', 'Dono': 'Fausto'},
]

escrever_dados(arquivo_escrito, dados)