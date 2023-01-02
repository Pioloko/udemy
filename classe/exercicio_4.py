# Crie uma classe Produto com as seguintes características:

# Atributos:

# Nome;

# Estoque;

# Descrição;

# Preço.

# Métodos:

# Mostrar nome;

# Mostrar estoque;

# Mostrar preço;

# Mudar nome;

# Mudar estoque;

# Mudar descrição;

# Mudar preço;

# Sumário (mostrar na tela todos os atributos de instância).

class Produto():
    def __init__(self,nome,estoque,descricao,preco):
        self.nome = nome
        self.estoque = estoque
        self.descricao = descricao
        self.preco = preco

    def mostrar_nome(self):
        return(f'O produto é um {self.nome}')


    def mostrar_estoque(self):
        return(f'A quantidade em estoque é {self.estoque}')


    def mostrar_preco(self):
        return(f'O preço do produto é : {self.preco}')

    
    def mostrar_descricao(self):
        return(f'Descrição: {self.descricao}')


    def mudar_nome(self,novo_nome):
        self.nome = novo_nome
    
    def mudar_estoque(self,novo_estoque):
        self.estoque = novo_estoque

    def mudar_preco(self,novo_preco):
        self.preco = novo_preco

    def mudar_descricao(self,nova_descricao):
        self.descricao = nova_descricao

    def sumario(self):
        print('Sumário do produto')
        print(f'Produto: {self.nome}')
        print(f'Estoque: {self.estoque}')
        print(f'Descrição: {self.descricao}')
        print(f'Preço: {self.preco}')


produto1=Produto('Produto 1',10,'Produto 1 - Categoria A',20.5)

produto1.mudar_nome('Produto 2')
produto1.mudar_estoque(20)
produto1.mudar_preco(50.2)
produto1.mudar_descricao('Nova descrição')

produto1.sumario()


