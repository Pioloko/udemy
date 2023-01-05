#  Crie um Programa Agenda com as seguintes características:

# Cada contato deverá ter as seguintes informações: Nome, Sobrenome, Data do registro, Número de Telefone e E-mail (que deverá funcionar como id);

# Crie uma lista vazia para armazenar os contatos;

# Seu programa deverá ter as seguintes funções:

# adicionar_contato

# A função deve receber como input os atributos definidos anteriormente;

# alterar contato

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
from datetime import date
data_registro=date.today().strftime('%d/%m/%Y')


def menu():
    os.system("clear")
    print("Menu".center(65,"="))
    print()
    print("\t1 - Cadastrar novo contato ")
    print("\t2 - Procurar Contato ")
    print("\t3 - Remover Contato ")
    print("\t4 - Ver Contatos ")
    print("\t5 - Sair")
    print()
    print("="*65)


menu()
