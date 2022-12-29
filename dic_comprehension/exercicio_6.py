# A partir das listas



empresa = ['ABEV3', 'AZUL4', 'BTOW3', 'RENT3', 'JBSS3']
precos = [12.85, 22.55, 115.08, 49.03, 24.41] 


# Utilize compreensão de dicionários e obtenha:


# {'ABEV3': 12.85, 'AZUL4': 22.55, 'BTOW3': 115.08, 'RENT3': 49.03, 'JBSS3': 24.41}



print({x:y for x,y in zip(empresa,precos)})
