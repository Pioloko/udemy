# Crie um programa para controlar listas, com as seguintes funções:

# Adicionar elemento no início;

# Adicionar elemento no fim;

# Remover elemento;

# Tamanho da lista;

# Imprimir elementos da lista;

# Esvaziar lista;

# Execute o seu programa em uma função principal.

lista=[]

def menu():
    print("Menu".center(65))
    print("*"*65)
    print("\t1 - Adicionar um elemento no inicio da Lista")
    print("\t2 - Adicionar um elemento no final da lista")
    print("\t3 - Remover um elemento da lista")
    print("\t4 - Tamanho da lista")
    print("\t5 - Imprimir elementos da lista")
    print("\t6 - Esvaziar lista")
    print("\t7 - Sair")
    print("*"*65)


def adcionar_final():
    x = input("Digite o que voce quer adcionar na lista: ")
    lista.append(x)
    print(lista)

def adcionar_comeco():
    x = input("Digite o que voce quer adcionar na lista: ")
    lista.insert(0,x)
    print(lista)

def remover():
    x = input("Qual dado voce quer remover ? ")
    if x in list:
        lista.remove(x)
        print(lista)
        
def tamanho():
    print(len(lista))

def imprimir():
    for i in lista:
        print(i)

def esvaziar():
    lista.clear()
    print(lista)



def main():
    escolha = ""
    menu()
    while True:

        escolha = int(input(">> "))

        if escolha == 1:
            adcionar_final()
            menu()


        elif escolha == 2:
            adcionar_comeco()
            menu()

        elif escolha == 3:
            remover()
            menu()
        elif escolha == 4:
            tamanho()
            menu()

        elif escolha == 5:
            imprimir()
            menu()

        elif escolha == 6:
            esvaziar()
            menu()

        elif escolha == 7:
            break
        
        else:
            print("Opção invalida")
            menu()
main()