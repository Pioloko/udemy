# Considere a lista abaixo e escreva um programa que multiplique todos os seus elementos.

lista=[10,2,40,50,-2,3,100,21,33,29,123,234,32,88,90,23]
x=0

for i in lista:
    x = i+x

solu2=[ x+i for i in lista]


print(f'Solução usando For comum {x}')
print(max([ x+i for i in lista]))
print(f'Solução usando sum = {sum(lista)}')
