# Use uma função built-in para obter a primeira e a última letra da lista letras, considerando a ordem alfabética.

letras=['c','k','w','x','m','r','j','l','n','v']
# Resultado esperado:

# Primeiro letra: c
# Última letra: x
nova=[x for x in sorted(letras)]

print(f"Primeira Letra: {sorted(nova[0])}")
print(f"Ultima Letra: {sorted(nova[-1])}")


letras=['c','k','w','x','m','r','j','l','n','v']
print('Primeiro letra: '+min(letras))
print('Última letra: '+max(letras))