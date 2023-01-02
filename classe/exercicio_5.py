# Crie uma classe Lampada com os seguintes atributos e métodos:

# Atributos:

# Cor;

# Voltagem;

# Luminosidade;

# Ligada (a lâmpada deve inicializar desligada).

# Métodos:

# Verificar se a lâmpada está ligada/desligada

# Ligar/desligar a lâmpada.

# Todos os atributos devem ser privados.

# Crie um objeto da classe Lampada e teste os métodos criados.

class Lampada():
    def __init__(self,cor,voltagem,luminosidade):
        self.__cor=cor
        self.__voltagem=voltagem
        self.__luminosidade=luminosidade
        self.__ligada=False

    def verificar_ligada(self):
        if self.__ligada == False:
            return("Lampada esta desligada")
        else:
            return("Lampada esta ligada")

    def ligar_desligar(self):
        if self.__ligada:
            self.__ligada=False
            return self.__ligada
        else:
            self.__ligada=True
            return self.__ligada
    

lamp1=Lampada('azul',110,80)

print(lamp1.verificar_ligada())  #Inicializa desligada
print(lamp1.ligar_desligar())  #Ligada
print(lamp1.ligar_desligar())  #Desligada

