# Escreva uma função que verifique se duas listas possuem ao menos um elemento em comum, retornando True em caso positivo.


lista1=[1,2,4,5,6,4,3]
lista2=[2,5,6,4,3,4,2]

def verifica(lista_1,lista_2):
    for i in lista_1:
        for j in lista_2:
            if i==j:
                return True
    return False


print(verifica(lista1,lista2))