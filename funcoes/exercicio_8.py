# Implemente uma função recursiva para calcular e retornar o fatorial de um número inteiro.
def fatorial(num):
    if num==1 or num==0:
        return 1
    else:
        return fatorial(num-1)*num

print(fatorial(5))