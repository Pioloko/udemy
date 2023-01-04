# Gerenciador de Produtos


# Crie um programa para gerenciar estoque de produtos. Armazene informações referentes ao preço, estoque, descrição do produto e data de registro. Use uma produtos para salvar essas informações.
# Elabore um menu para seu programa. 
# Exemplo:



# 1 - Cadastrar produto
# 2 - Remover produto
# 3 - Procurar produto
# 4 - Ver produtos
# 5 - Sair


# Algumas sugestões:

# Elabore funções para as opções de 1-4;

# Crie uma função principal para executar todo o programa;

# Cada produto poderá ser armazenado em uma produtos ou dicionário;

# Todos os produtos podem ser armazenados em uma produtos.

from datetime import datetime

produtos = []

def menu():
    print("menu".center(65,"="))
    print(opcao())
    print("="*65)

def opcao():
    print("Qual operação deseja fazer ")
    print("\t1 - Cadastrar")
    print("\t2 - Remover")
    print("\t3 - Procurar")
    print("\t4 - Ver Produto")
    return("\t5 - Sair")


 
def cadastrar():
    print("Quantos produtos deseja adicionar? ")
    num=int(input('>> '))
    for i in range(1,num+1):
        data=datetime.now().strftime("%d/%m/%Y")
        nome=input("Nome: ")
        estoque=int(input("Quantidade em estoque: "))
        preco=float(input("Preço: "))
        descricao=input("Descrição do produto: ")
        produtos.append([nome,estoque,preco,data,descricao])



def remover():
    if len(produtos)>0:
        nome=input("Digite o nome do produto que deseja remover: ")
        for produto in produtos:
            if nome==produto[0]:
                produtos.remove(produto)
                print(f'O produto {nome.lower()} foi removido.')
                return True
        print('Produto não encontrado.')
    else:
        print("Não há produtos cadastrados.")

def procurar():
    if len(produtos)>0:
        nome=input("Qual produto deseja pesquisar?")
        for produto in produtos:
            if nome==produto[0]:
                print(f'Nome: {produto[0]}')
                print(f'Preço: $ {produto[2]}')
                print(f'Estoque: {produto[1]}')
                return True
        print('Produto não encontrado.')
    else:
        print("Não há produtos cadastrados.")


def main():
    
    escolha=''
    while escolha!='5':
        menu()
        escolha=input('>> ')
        if escolha in list('1234'):
            if escolha=='1':
                cadastrar()
                
            elif escolha=='2':
                remover()
                
            elif escolha=='3':
                procurar() 
                
            else:
                procurar()
                
        else:
            if escolha!='5':
                print("Opção inválida")
            
 
if __name__=="__main__":
    main()