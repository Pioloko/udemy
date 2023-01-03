import math
 
def dividir(num1,num2):
    try:
        return f'Resultado da divisão de {num1} / {num2} = {num1/num2}'
    except ZeroDivisionError:
        return 'O denominador deve ser diferente de zero.'
    except TypeError:
        return 'Insira um valor válido.'
 
def menu_principal():
    print("Calculadora".center(65,'='))
    opcoes()
    print('='*65)
 
def opcoes():
    print("\t1 - Operações aritiméticas")
    print("\t2 - Funções Logarítimicas e Potência")
    print("\t3 - Funções trigonométricas")
    print("\t4 - Outras opções")
    print("\t5 - Sair")
    
def opcoes_1():
    print("\t1 - Soma")
    print("\t2 - Subtração")
    print("\t3 - Multiplicação")
    print("\t4 - Divisão")
    print("\t5 - Voltar")
    
    
def opcoes_2():
    print("\t1 - Quadrado")
    print("\t2 - Cubo")
    print("\t3 - Potência")
    print("\t4- Log10")
    print("\t5 - Log")
    print("\t6 - Voltar")
 
def opcoes_3():
    print("\t1 - Seno")
    print("\t2 - Cosseno")
    print("\t3 - Tangente")
    print("\t4 - Voltar")
 
def opcoes_4():
    print("\t1 - Fatorial")
    print("\t2 - Voltar")
 
def menu_1():
    opcao=0
    while opcao!=5:
        opcao=int(input(">> "))
        if opcao in range(1,5):
            num1=float(input("Número 1: "))
            num2=float(input("Número 2: "))
            if opcao==1:
                print(f'Resultado da soma de {num1} + {num2} = {num1+num2}')
                print()
                print(opcoes_1())
            elif opcao==2:
                print(f'Resultado da subitração de {num1} - {num2} = {num1-num2}')
                print()
                print(opcoes_1())
            elif opcao==3:
                print()
                print(opcoes_1())
                print(f'Resultado da multiplicação de {num1} x {num2} = {num1*num2}')
            else:
                print(dividir(num1,num2))
                
        else:
            if opcao!=5:
                print('Opção inválida.')
 
                
def menu_2():
    opcao=0
    while opcao!=6:
        opcao=int(input(">> "))
        if opcao in range(1,6):
            
            if opcao==1 or opcao==2 or opcao==4:
                num1=float(input('Número: '))
                
                if opcao==1:
                    print(f'O numero {num1}² ao quadrado é = {num1**2}')
                elif opcao==2:
                    print(f'O numero {num1}³ ao cubo é = {num1**3}')
                else:
                    print(f'O log de {num1} na base 10 é {math.log10(num1)}')
            else:
                if opcao==3:
                    base=float(input("Base da potência: "))
                    exp=float(input("Expoente: "))
                    print(f'{base}^{exp}={base**exp}')
                if opcao==5:
                    base=float(input("Base do log: "))
                    num=float(input("Número: "))
                    print(f'O log de {num} na base {base} é :{math.log(num,base)}')
 
        else:
            if opcao!=6:
                print('Opção inválida.')
                
def menu_3():
    opcao=0
    while opcao!=4:
        opcao=int(input(">> "))
        if opcao in range(1,4):
            num=float(input("Número: "))
            if opcao==1:
                print(f"sen({num})={math.sin(num)}")
            elif opcao==2:
                print(f"cos({num})={math.cos(num)}")
            else:
                print(f"tan({num})={math.tan(num)}")
        else:
            if opcao!=4:
                print('Opção inválida.')
 
def menu_4():
    opcao=0
    while opcao!=2:
        opcao=int(input(">> "))
        if opcao==1:
            num=int(input("Digite o número inteiro: "))
            print(f"{num}!={math.factorial(num)}")
        else:
            if opcao!=2:
                print('Opção inválida.')
 
def main():
    escolha=''
    
    while escolha!='5':
        
        menu_principal()
        
        escolha=input(">> ")
        
        if escolha in list('1234'):
            
            if escolha=='1':
                opcoes_1()
                menu_1()
 
            elif escolha=='2':
                opcoes_2()
                menu_2()
                
            
            elif escolha=='3':
                opcoes_3()
                menu_3()
                
            elif escolha=='4':
                opcoes_4()
                menu_4()
                
        elif escolha=='5':
            print("Fim do programa")
            
        else:
            print("Opção inválida")
            
 
main()