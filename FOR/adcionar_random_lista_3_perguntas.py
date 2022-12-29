# Escreva um programa que gere 100 números reais aleatórios entre 0 e 1 e armazene-os em uma lista.
#  Ao final seu programa deverá mostrar na tela as seguintes informações:

# Maior número;

# Menor número;

# Soma de todos os números gerados;

# Média e desvio padrão.

import random
from random import randint
from statistics import mean,stdev

lista=[]
soma=0
for num in range(1,101):
    lista.append(randint(1,1000))


print(f"O maior numero é {max(lista)}")
print(f"O menor numero é {min(lista)}")
print(f"A soma total é {sum(lista)}")
print(f"A media  é  {mean(lista)}")
print(f"O desvio é {stdev(lista)}")