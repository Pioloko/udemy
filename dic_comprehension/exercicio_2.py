
# A partir da lista



linguagens = ['python', 'javascript', 'java', 'php', 'c', 'julia']


# Use Dict Comprehension para construir o dicionário abaixo:   



{'python': 6, 'javascript': 10, 'java': 4, 'php': 3, 'c': 1, 'julia': 5}


# Dica: observe que o valor associado a cada chave corresponde ao tamanho de cada string.

print({l:len(l) for l in linguagens})