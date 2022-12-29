# a) Use compreensão de dicionários para extrair os produtos com preço superior a dois mil reais.



produtos = {
    'geladeira':1619.1,
    'ps5':4999,
    'liquidificador':89.9,
    'notebook':3500,
    'TV':1500,
    'ventilador':79.99,
    'microondas':399.99
    }


# b) Considerando que cada valor deste dicionário representa o preço de cada produto, obtenha o custo total desta cesta de produtos.


produtosaioresq2k=({i:v for i,v in produtos.items() if v > 2000})

total = sum(produtos.values())

print(total)
