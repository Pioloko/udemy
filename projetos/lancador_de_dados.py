# Crie um programa simples para simular o lançamento de um dado, 
# que a cada laço de repetição verifique se o número inserido pelo usuário é igual ao valor aleatório do lançamento.
# O programa deve ser repetido indefinidamente até que o usuário digite 0 ou se o número digitado estiver fora do intervalo [1,6].
# Ao final mostre o número de acertos e a quantidade de jogadas.

class dado():

    def lancar(self):
        from random import randint

        dado = randint(1,6)
        count= 0
        chute = 0
        while chute!= dado:

            chute = int(input("Digite seu chute >> "))
            if chute > 6:
                print("Numero invalido")
            elif chute == dado:
                print(f"Parabens voce acertou o numero do dado em {count} tentativas !!")
                break
            elif chute != dado:
                print(f"Voce nao acertou o numero continue tentando, o numero era {dado}, porem agora foi atualizado")
                count +=1
                dado = randint(1,6)


chute = dado()

chute.lancar()