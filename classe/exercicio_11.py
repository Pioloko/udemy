# Crie uma classe Cliente com os seguintes atributos e métodos:

# Atributos (todos privados):

# Nome;

# E-mail;

# Telefone;

# Senha.


# Métodos:

# Mostrar nome;

# Mostrar e-mail;

# Mostrar telefone;

# Alterar nome *;

# Alterar Senha *;

# Resumo (mostra todas as informações do cliente, inclusive a senha).

# *Para alterar essas informações, peça a senha do usuário, e caso a senha seja correta permita a modificação.



# Crie um objeto para testar os métodos e atributos da classe Cliente.

class Cliente():
    def __init__(self,nome,email,telefone,senha):
        self.__nome = nome
        self.__email = email
        self.__telefone = telefone
        self.__senha = senha

    
    def mostrar_nome(self):
        print(self.__nome)
    
    def mostrar_email(self):
        print(self.__email)

    def mostrar_telefone(self):
        print(self.__telefone)
    
    def mostra_senha():
        print(self.__senha)

    def alterar_nome(self):
        teste = input("digite a sua senha: ")
        if teste != self.__senha:
            print("senha errada")
        else:
            novo_nome = input("digite o novo nome: ")
            self.__nome = novo_nome
            return(f'seu novo nome e {self.__nome}')


    def alterar_senha(self):
        teste = input("digite a sua senha: ")
        if teste != self.__senha:
            print("senha errada")
        else:
            nova_senha = input("digite a nova senha : ")
            self.__senha = nova_senha
            return(f'sua nova senha é {self.__senha}')


    def resumo_cliente(self):
        print('Informações cliente')
        print(f'Nome: {self.__nome.strip().title()}')
        print(f'E-mail: {self.__email}')
        print(f'Telefone: {self.__telefone}')
        print(f'Senha: {self.__senha}')


ramon = Cliente("ramon","ramon.piologo@hotmail.com","123456789","batata123")


# print(ramon.alterar_nome())
print(ramon.resumo_cliente())