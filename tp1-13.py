# Exercício 13: Escrever um dicionário em um arquivo JSON
# Enunciado: Escreva uma função que recebe um nome de arquivo e um dicionário como entrada e salva os dados no arquivo JSON no formato adequado,
# garantindo que o conteúdo seja formatado corretamente para fácil leitura.

import json

arquivo = 'arquivo-tp1-13.json' # arquivo json vai ser criado na mesma pasta do código
dicionario = {
    "Curso": "Análise e desenvolvimento de sistemas",
    "Matéria": "Python",
    "Professor": "Luis Eduardo"
}
def salvar_arquivo_json(arquivo_a_salvar, dicionario_recebido):
    try:
        with open(arquivo_a_salvar, mode='w', encoding='utf-8') as arquivo:
            print(f'Arquivo {arquivo.name} salvo com sucesso')
            return json.dump(dicionario_recebido, arquivo, ensure_ascii=False, indent=4)
    except FileNotFoundError:
        print(f"Arquivo '{arquivo_a_salvar}' não encontrado")
    except Exception as e:
        print(f"Erro {e}")

salvar_arquivo_json(arquivo, dicionario)