# Escreva um programa que pesquise um determinado valor em uma lista. 
# Sua função deve ter como parâmetros a lista e o valor a ser verificado.
# Caso o valor faça parte da lista informada retorne True e False, caso contrário.


def verifica(n,lista):
    count=0
    for i in lista:
        if i == n:
            count += 1
            
    return(f"o numero: {n} aparece {count} vezes na lista ")



print(verifica(1,[1,2,3,4,5,1,1,1]))