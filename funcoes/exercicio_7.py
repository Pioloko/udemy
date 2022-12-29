# Elabore uma função que receba um número inteiro e retorne o fatorial deste número.


def fatorial(a):
    resultado=1
    for n in range(1,a+1):
        resultado *= n

    return(resultado)
        
print(fatorial(5))