# Escreva uma função que receba uma lista de números reais como parâmetro e retorne a média destes números.


def media_lista(lista):
    soma=0
    for num in lista:
        soma+=num
    return soma/len(lista)

print(media_lista([1,2,3,4,5,6,7]))