# Exercício 16: Criar um índice invertido de palavras em um texto
# Enunciado: Escreva uma função que recebe um arquivo de texto como entrada e retorna um dicionário onde as chaves são palavras
# e os valores são conjuntos de números de linha onde cada palavra aparece no texto.
arquivo = 'arquivo-tp1-16.txt' # arquivo txt se encontra na mesma pasta do código
lista_pontos = '".",",","!","?"'
def criar_indice_inverido(arquivo_lido):
    indice = {}
    try:
        with open(arquivo_lido, mode='r', encoding='utf-8') as arquivo:
            for contagem_linha, linha in enumerate(arquivo):
                palavras = linha.strip().split()
                print(palavras)
                for palavra in palavras:
                    palavra = palavra.lower().strip(lista_pontos)
                    if palavra not in indice:
                        indice[palavra] = set()
                    indice[palavra].add(contagem_linha + 1)
        print(indice)
    except FileNotFoundError:
        print(f"Arquivo '{arquivo_lido}' não encontrado")
    except Exception as e:
        print(f"Erro {e}")

criar_indice_inverido(arquivo)