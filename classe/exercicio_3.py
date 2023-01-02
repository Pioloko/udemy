# Crie uma classe Pessoa com as seguintes características:

# Atributos:

# Nome (atributo público);

# E-mail (atributo público);

# Senha (atributo privado).

# Métodos:

# Mostrar nome;

# Mostrar E-mail;

# Mostrar senha.



# Crie um objeto da classe Pessoa para testar suas propriedades e métodos.

class Pessoa:
    def __init__(self,nome,email,senha):
        self.nome = nome
        self.email = email
        self.__senha = senha

    
    def mostrar_nome(self):
        return(self.nome)

    def mostrar_email(self):
        return(self.email)
    
    def mostrar_senha(self):
        return(self.__senha)


user=Pessoa('User','user@email.com','x54a_Zkp79c')
print()
print(f'Nome: {user.mostrar_nome()}')
print(f'E-mail: {user.mostrar_email()}')
print(f'Senha: {user.mostrar_senha()}')