# Crie uma função que recebe um número e verifique se este é primo.
# Posteriormente, use a função filter() para criar uma lista com todos os números pares de 1 a 50.







def checa_primo(numero):
    if numero>1:
        for i in range(2,numero):
            if numero%i==0:
                return False
        else:
            return True
    else:
        return False
    
lista_primo=list(filter(lambda numero:checa_primo(numero),range(1,51)))