# Exercício 15: Criar um conjunto a partir de um arquivo de texto (set de nomes únicos)
# Enunciado: Escreva uma função que recebe um arquivo de texto contendo uma lista de nomes, um por linha, e retorna um conjunto (set)
# contendo apenas os nomes únicos encontrados no arquivo.

arquivo = 'arquivo-tp1-15.txt' # arquivo txt se encontra na mesma pasta do código

def criar_conjunto_texto(arquivo_lido):
    nomes = set()
    try:
        with open(arquivo_lido, mode='r', encoding='utf-8') as arquivo:
            for linha in arquivo:
                nome = linha.strip()
                if nome:
                    nomes.add(nome)
        return nomes
    except FileNotFoundError:
        print(f"Arquivo '{arquivo_lido}' não encontrado")
    except Exception as e:
        print(f"Erro {e}")

print(criar_conjunto_texto(arquivo))