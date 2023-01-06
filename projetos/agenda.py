# Crie um Programa Agenda com as seguintes características: ok
# Cada contato deverá ter as seguintes informações: Nome, Sobrenome, Data do registro, Número de Telefone e E-mail (que deverá funcionar como id);ok
# Crie uma lista vazia para armazenar os contatos;ok
# Seu programa deverá ter as seguintes funções:
# adicionar_contato ok
# A função deve receber como input os atributos definidos anteriormente; ok
# alterar contato ok
# A função deve pertimir ao usuário alterar um determinado atributo do contato especificado.
# Certifique-se que o contato exista na lista de usuários e caso contrário mostre uma mensagem personalizada ao usuário.
# procurar_contato
# A função deve percorrer toda a lista de contatos e mostrar todos os atributos do contato especificado.
# Caso o contato não exista mostre uma mensagem personalizada na tela.
# remover_contato
# A função deve percorrer toda a lista de contatos e remover o contato especificado.
# Caso o contato não exista mostre uma mensagem personalizada na tela.
# ver_contatos
# A função deve percorrer toda a lista de contatos e mostrar na tela todos os contatos existentes.
# Mostre uma mensagem personalizada na tela Caso não existam contatos registrados na agenda.
# menu
# O menu deve gerenciar todo o seu programa e apresentar ao usuário as seguintes opções:
# Adicionar contato
# Alterar contato
# Procurar contato
# Remover contato
# Ver contatos
# Sair
# Certifique-se que todo o programa seja executado dentro de uma função principal main().

import os
import time
from datetime import date
data_registro=date.today().strftime('%d/%m/%Y')

contatos=list()

def menu():
    os.system("clear")
    print("Menu".center(65,"="))
    print()
    print("\t1 - Cadastrar novo contato ")
    print("\t2 - Procurar Contato ")
    print("\t3 - Remover Contato ")
    print("\t4 - Alterar Contato ")
    print("\t5 - Ver Contatos ")
    print("\t6 - Sair")
    print()
    print("="*65)


def adicionar_contato():
    print('\tAdicionar contato')
    email=input('Digite o E-mail: ')
    time.sleep(3)
    if len(email)>0:
        for contato in contatos:
            if email==contato['email']:
                print('Este contato já existe.')
                return True
 
    contatos.append({
        'email':email.lower(),
        'nome':input('Nome: ').strip().capitalize(),
        'sobrenome':input('Sobrenome: ').strip().capitalize(),
        'telefone':input('Telefone: ').strip(),
        'data':date.today().strftime('%d/%m/%Y')
    })

    print(contatos)
    time.sleep(5)        

def procurar_contato():
    if len(contatos)>0:
        email=input('Digite o e-mail do contato: ')
        for contato in contatos:
            if contato['email']==email:
                print(f"Nome: {contato['nome']} {contato['sobrenome']}")
                print(f"Telefone: {contato['telefone']}")
                print(f"Data de registro: {contato['data']}")
                return
    print('Não há contatos registrados na agenda.')

def remover_contato():
    if len(contatos)>0:
        email=input('Digite o e-mail do contato que deseja remover: ')
        x=0
        while x<len(contatos):
            if contatos[x]['email']==email:
                contatos.remove(contatos[x])
                return True
            x+=1
            
        print('Contato não encontrado.')
    else:
        print('Não há contatos registrados na agenda.')


def alterar_contato():
    
    if len(contatos)>0:
        email=input('Digite o e-mail do contato que deseja alterar: ')
        for contato in contatos:
            if contato['email']==email:
                print(f"Nome do contato: {contato['nome']}")
                print(f"Telefone: {contato['telefone']}")
                print('1 - Alterar nome')
                print('2 - Alterar telefone')
                print('3 - Voltar')
                escolha=input('>> ')
                if escolha==str(1):
                    novo_nome=input('Digite um novo nome para o contato: ')
                    contato['nome']=novo_nome
                    return
            
                elif escolha==str(2):
                    novo_tel=input('Digite um novo telefone para o contato: ')
                    contato['telefone']=novo_tel
                    return
                    
                elif escolha==str(3):
                    return
                    
                else:
                    print('Opção inválida.')
                    return
                    
        print('Não existe usuário cadastrado com o e-mail informado.')    
    else:
        print('Não há contatos registrados na agenda.')

def ver_contatos():
    if len(contatos)>0:
        contatos_ordenados=sorted(contatos,key=lambda contato:contato['nome']+' '+contato['sobrenome'])
        for indice,contato in enumerate(contatos_ordenados,start=1):
            print(f'Contato {indice}'.center(100,' '))
            print(f"Nome: {contato['nome']} {contato['sobrenome']}")
            print(f"E-mail: {contato['email']}")
            print(f"Telefone: {contato['telefone']}")
            print(f"Data de registro: {contato['data']}")
            print()
    else:
        print('Não há contatos registrados na agenda.')

def main():
    escolha=''
    while escolha!=str(6):
        menu()
        
        escolha=input('>> ')
        
        if escolha==str(1):
            adicionar_contato()
            
        elif escolha==str(2):
            procurar_contato()
            
        elif escolha==str(3):
            remover_contato()
        
        elif escolha ==str(4):
            alterar_dados()
            
        elif escolha==str(5):
            ver_contatos()
            
        else:
            if escolha==str(6):
                print('Fim do Programa.')
            else:
                print('Escolha inválida')
 
if __name__=='__main__':
    main()