class Cliente:
    
    def __init__(self,nome,email,telefone,senha):
        self.__nome=nome
        self.__email=email
        self.__telefone=telefone
        self.__senha=senha
        
    def nome(self):
        return self.__nome
    
    def email(self):
        return self.__email
    
    def telefone(self):
        return self.__telefone
    
    def senha(self):
        return self.__senha
    
    def checar(self,senha):
        if senha==self.__senha:
            return True
        else:
            return False
    
    def alterar_nome(self,senha):
        if self.checar(senha):
            nome=input('Digite o novo nome: ')
            self.__nome=nome
            return 'Nome alterado.'
        return 'Senha inválida.'
        
    def alterar_senha(self,senha):
        if self.checar(senha):
            senha=input('Digite a nova senha: ')
            self.__senha=senha
            return 'Senha alterada'
        return 'Senha inválida.'
    
    def alterar_email(self,senha):
        if self.checar(senha):
            email=input('Digite o novo E-mail: ')
            return 'E-mail alterado.'
        return 'Senha inválida'
    
    def resumo_cliente(self):
        print('Informações cliente')
        print(f'Nome: {self.__nome.strip().title()}')
        print(f'E-mail: {self.__email}')
        print(f'Telefone: {self.__telefone}')
        print(f'Senha: {self.__senha}')
        
    
cliente1=Cliente('User','user@email.com','99132-7345','123456')
print(cliente1.alterar_senha('123456'))
print(cliente1.alterar_senha('123'))
cliente1.resumo_cliente()