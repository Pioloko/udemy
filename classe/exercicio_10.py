# Crie uma classe Pessoa com os atributos nome,
# idade e telefone (privado) e um método resumo,
# para mostrar na tela todos os atributos.
# Em seguida crie uma classe PessoaUniversidade que herde todos os métodos e atributos da classe Pessoa,
# mas que implemente o atributo universidade e sobrescreva o método resumo.


class Pessoa():
    def __init__(self,nome,idade,telefone):
        self.nome = nome
        self.idade = idade
        self.__telefone = telefone

    def resumo(self):
        print(self.nome)
        print(self.idade)
        print(self.__telefone)

class PessoasUniversidade(Pessoa):
    def __init__(self, nome, idade, telefone, universidade):
        super().__init__(nome, idade, telefone)
        self.universidade = universidade
    
    def resumo(self):
        super().resumo()
        print(f'Universidade: {self.universidade}')