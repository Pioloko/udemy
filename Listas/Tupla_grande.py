tupla1=('A','B','A','Z','Z','X','A','E','K','G','H')



# a) mostre na tela o tamanho desta tupla;

# b) ordene a tupla e mostre o resultado na tela;

# c) mostre na tela o número de ocorrências da string 'A';

# d) mostre na tela o número de ocorrências da string 'B';

# e) mostre na tela o índice da string 'X';

# f) mostre na tela o último elemento da tupla1.

a = len(tupla1)

b = sorted(tupla1)

contador_A = 0
for i in tupla1:
    if i =="A":
        contador_A +=1

# c = print(contador_A)

contador_B = 0
for i in tupla1:
    if i =="B":
        contador_B +=1

# d = print(contador_B)

e = print(tupla1.index('X'))

f = print(tupla1[-1])

# "solução do exercicio para os counts"

# print("Número de ocorrências de 'A' ",tupla1.count('A'))

# print("Número de ocorrências de 'B' ",tupla1.count('B'))