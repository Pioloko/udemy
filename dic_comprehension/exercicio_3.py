
lista = ['  Banana  ', ' Laranja   ', '  Maçã', ' Melão ']


# Use Dict Comprehension para construir o dicionário abaixo:



{'1': 'Banana', '2': 'Laranja', '3': 'Maçã', '4': 'Melão'}


print({i:lista.strip() for i,lista in enumerate(lista,start=1)})


# dicionario = {str(i):fruta.strip() for i,fruta in enumerate(frutas, start=1)}



