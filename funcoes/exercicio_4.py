# Escreva uma função que verifique se um número é múltiplo do outro e retorne um valor lógico.


def verifica(n,m):
    if n%m==0:
        resultado=n*m
        return(f'{n} é multiplo de {m} é o resultado é {resultado}')


print(verifica(10,5))

