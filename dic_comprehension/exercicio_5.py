# Utilize compreensão de dicionários para construir o dicionário abaixo.



# {'A': 1, 'B': 2, 'C': 6, 'D': 24, 'E': 120}


# Dica: observe que o valor associado a cada chave corresponde ao fatorial de cada número no intervalo [1,5].


from math import factorial
print({chr(64+i):factorial(i)  for i in range(1,6)})