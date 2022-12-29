# copiar lista

lista = [1,2,4,5,"ss","wdas",123,123]

def copiar_lista(lista):
    copia=[]
    if type(lista)==list:
        if len(lista)>0:
            for elemento in lista:
                copia.append(elemento)
            return copia