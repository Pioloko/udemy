# Crie um programa simples que gere números inteiros aleatórios entre 1-50,
# que peça um número do usuário e verifique se o valor inserido é igual ao aleatório.
# O programa deve ser repetido 15 vezes. Se o usuário digitar um número fora do intervalo válido o programa deverá ser encerrado.
# Se o usuário acertar o número aleatório mostre uma mensagem personalizada na tela, a cada laço de repetição.
# E caso o usuário não acerte, mostre na tela se o número que ele digitou foi maior ou menor que o número aleatório.
# Ao final mostre a quantidade de acertos.

from random import randint
acertos=0
 
for num in range(1,16):
    print(f'Jogada {num}')
    numero=randint(1,50)
    escolha_usuario=int(input('Digite um número entre 1-50: '))
    
    if escolha_usuario in range(1,51):
        if escolha_usuario>numero:
            print('Você Digitou um número maior que o aleatório')
            print(f'Número Aleatório: {numero}')
            
        elif escolha_usuario<numero:
            print('Você digitou um número menor que o aleatório')
            print(f'Número Aleatório: {numero}')
            
        else:
            print('Você acertou!')
            acertos+=1
    
    else:
        print('Fim.')
        break
        
print(f'Número de acertos: {acertos}')
