# Considere as variáveis



var1=['Hello World!']
var2=True and all([True or False,()])
var3=('10',) if 10>4 else 1
var4=('Hello World!')
var5=('Python is love!',)


# a) Verifique e imprima o tipo destas variáveis na tela.

# ['Hello World!'] <class 'list'>
# False <class 'bool'>
# ('10',) <class 'tuple'>
# Hello World! <class 'str'>
# ('Python is love!',) <class 'tuple'>

# print(var1,type(var1))
# print(var2,type(var2))
# print(var3,type(var3))
# print(var4,type(var4))
# print(var5,type(var5))

# b) Verifique se essas variáveis são objetos do tipo tupla, isto é, instâncias da classe tupla.

variaveis=var1,var2,var3,var4,var5

for i in variaveis:
    if type(i) == tuple:
        print(f"{i} é uma tupla")
    elif type(i)!= tuple:
        print(f"{i} não é uma tupla")
        