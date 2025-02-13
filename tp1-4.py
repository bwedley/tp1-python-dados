# Exercício 4: Contar frequência de palavras em um texto
# Enunciado: Escreva uma função que recebe uma string contendo um texto e retorna um dicionário onde as chaves são palavras
# e os valores correspondem ao número de vezes que cada palavra aparece no texto.
texto = "O cachorro correu pelo parque e o gato também correu pelo parque, O cachorro estava muito feliz."
lista_pontos = [".",",","!","?"]
texto = ''.join(palavra for palavra in texto if palavra not in lista_pontos)
def contar_freq_palavras(texto):
    palavras = texto.split()
    frequencia = {}

    for palavra in palavras:
        palavra = palavra.lower()
        if palavra in frequencia:
            frequencia[palavra] += 1
        else:
            frequencia[palavra] = 1
    return frequencia

print(contar_freq_palavras(texto))