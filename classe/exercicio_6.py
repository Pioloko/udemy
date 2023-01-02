# Elabore e implemente uma classe Vetor, com 2 dimensões, que possua os métodos:

# Soma;

# Subtração;

# Produto interno;

# Norma;

# Igualdade entre dois vetores;

# Diferença entre dois vetores.

# Utilize métodos mágicos em sua implementação. Crie dois objetos da classe Vetor para testar os métodos criados.
import math
 
class Vetor:
 
    def __init__(self,x,y):
        self.x=x
        self.y=y
 
    def __str__(self):
        return f'({self.x},{self.y})'
 
    def __rpr__(self):
        return f'(x,y)=({self.x},{self.y})'
 
    def __add__(self,outro):
        x=self.x+outro.x
        y=self.y+outro.y
        return Vetor(x,y)
 
    def __sub__(self,outro):
        x=self.x-outro.x
        y=self.y-outro.y
        return Vetor(x,y)
 
    def __mul__(self,outro):
        x=self.x*outro.x
        y=self.y*outro.y
        soma=x+y
        return soma
 
    def __abs__(self):
        return math.sqrt(self.x**2+self.y**2)
 
    def __eq__(self,outro):
        return self.x==outro.x and self.y==outro.y
 
    def __ne__(self,outro):
        return self.x!=outro.x or self.y!=outro.y
 
vetor1=Vetor(3,4)
vetor2=Vetor(1,1)
print(vetor1+vetor2)
print(vetor1-vetor2)
print(vetor1*vetor2)
print(abs(vetor1))
print(vetor1==vetor2)
print(vetor1!=vetor2)
