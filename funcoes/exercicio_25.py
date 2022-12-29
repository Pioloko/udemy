# Converta as listas abaixo para um dicionário. Use dict() e zip().



chaves=['cidades_EUA','cidades_BR']
valores=[
    ['Nova Iorque','Houston','Boston','Detroit','Seattle'],
    ['Rio de Janeiro','São Paulo','Brasília','Goiânia','Recife']
        ]


# Resultado esperado:

# {
# 'cidades_EUA': ['Nova Iorque', 'Houston', 'Boston', 'Detroit', 'Seattle'], 
# 'cidades_BR': ['Rio de Janeiro', 'São Paulo', 'Brasília', 'Goiânia', 'Recife']
# }

print(dict(zip(chaves,valores)))