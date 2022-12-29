dici={
    'nome':'produto1',
    'tipo':'categoriaA',
    'valor':'50.5',
    'fornecedor':'ABCD',
}

# 18.1 Crie um script para iterar no dicionário abaixo e mostrar na tela todas as suas chaves, uma a uma.

# Output:
# nome
# tipo
# valor
# fornecedor

print(dici.keys())



# 18.2 Crie um script para iterar no dicionário produto1 e mostrar na tela todos os seus valores, um a um.

# Output:

# produto1
# categoriaA
# 50.5
# ABCD

print(dici.values())

# 18.3 Crie um script para iterar no dicionário produto1 e mostrar chave,valor na tela.

# Output:

# nome produto1
# tipo categoriaA
# valor 50.5
# fornecedor ABCD
# Dica: utilize o método items().

for key in dici.keys():
    print(key, '->', dici[key])

for chave,valor in dici.items():
    print(chave,valor)