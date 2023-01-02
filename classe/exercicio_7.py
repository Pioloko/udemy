# Elabore e implemente uma classe Vetor, com 3 dimensões, que possua os métodos:

# Soma;

# Subtração;

# Multiplicação;

# Norma;

# Igualdade entre dois vetores;

# Diferença entre dois vetores.

# Utilize métodos mágicos em sua implementação. Crie dois objetos da classe Vetor para testar os métodos criados.

import math
 
class Vetor(object):
    
    def __init__(self,x,y,z):
        self.x,self.y,self.z=x,y,z
 
    def __str__(self):
        return f'({self.x},{self.y},{self.z})'
 
    def __rpr__(self):
        return f'(x,y,z)=({self.x},{self.y},{self.z})'
 
    def __add__(self,outro):
        x=self.x+outro.x
        y=self.y+outro.y
        z=self.z+outro.z
        return Vetor(x,y,z)
 
    def __sub__(self,outro):
        x=self.x-outro.x
        y=self.y-outro.y
        z=self.z-outro.z
        return Vetor(x,y,z)
 
    def __mul__(self,outro):
        x=self.x*outro.x
        y=self.y*outro.y
        z=self.z*outro.z
        soma=x+y+z
        return soma
 
    def __abs__(self):
        return math.sqrt(self.x**2+self.y**2+self.z**2)
 
    def __eq__(self,outro):
        return self.x==outro.x and self.y==outro.y and self.z==outro.z
 
    def __ne__(self,outro):
        return self.x!=outro.x or self.y!=outro.y or self.z!=outro.z   
 
if __name__=='__main__':
    v1=Vetor(1,2,3)
    v2=Vetor(1,1,1)
    v3=Vetor(1,2,3)
    print(f'{v1}+{v2}={v1+v2}')
    print(f'{v1}-{v2}={v1-v2}')
    print(f'{v1}*{v2}={v1*v2}')
    print(v1==v2)
    print(v1==v3)
    print(v1!=v2)