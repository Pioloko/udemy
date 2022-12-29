# Do dicionário abaixo:

dados = {12.85: 'ABEV3', 22.55: 'AZUL4', 115.08: 'BTOW3', 49.03: 'RENT3', 24.41: 'JBSS3'}


# Utilize compreensão de dicionários e obtenha:



# {'ABEV3': 12.85, 'AZUL4': 22.55, 'BTOW3': 115.08, 'RENT3': 49.03, 'JBSS3': 24.41}


dic={x:y for y,x in dados.items()}

print(dic)