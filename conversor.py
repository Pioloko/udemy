# Elabore um programa completo que dê ao usuário a possibilidade de converter várias unidades de medida 
# (tempo, volume,massa,dentre outras).
import os


os.system('clear')

def menu():
    print("Menu".center(65,"="))
    opcoes()
    print('='*65)

def opcoes():
    print("\t1 - Operações de tempo")
    print("\t2 - Opções de volumes")
    print("\t3 - Sair")

def opcoes_1():
    print("\t1 - Conversão Horas para min ")
    print("\t2 - Conversão de Min para Segundos")
    print("\t3 - conversão de Sec para Miliseconds")
    print("\t4 - Voltar")

def opcoes_2():
    print("\t1 - Litros para Mililitros ")
    print("\t2 - KM - Para cm ")
    print("\t3 - M³ para Litros")
    print("\t4 - Voltar")

def menu_1():
    n1=0
    while n1 != 5:
        n1 = int(input("escolha uma opção: "))
        if n1 ==1:
            hora = int(input("Digite a hora para ser convertida: "))
            print(f"A {hora} convertida para min são {hora*60} min")
            print()
            print(opcoes_1())
        elif n1 == 2: 
            minutos = int(input("Digite os min a serem convertidos: "))
            print(f'{min} convertidos para segundos são {minutos*60} segundos')
            print()
            print(opcoes_1()) 
        elif n1 == 3:
            sec = int(input("Digite os segundos a serem convertidos: "))
            print(f'{sec} convertido dão {sec/1000} miliseconds')
            print()
            print(opcoes_1()) 
        elif n1 ==4:
            print("Programa encerrado.")
            os.system("clear")
            break

def menu_2():
    n1=0
    while n1 !=4:
        n1 = int(input("escolha uma opção"))
        if n1 ==1:
            litro=int(input("Digite os litros a serem convertidos"))
            print(f"{litro} litro em Ml = {litro*1000}ml")
            print()
            print(opcoes_2()) 
        elif n1 ==2:
            km=int(input("Digite os KMs: "))
            print(f"{km} convertidos em cm são {km*1000*100}cm")
            print()
            print(opcoes_2()) 
        elif n1 ==3:
            m=int(input("digite os metros a serem convertidos: "))
            print(f"{m} em litros {m*1000}")
            print()
            print(opcoes_2()) 
        elif n1 ==4:
            print("Programa encerrado")
            os.system("clear")
            break

def main():
    escolha=''
    
    while escolha!='3':
        
        menu()
        
        escolha=input(">> ")
        
        if escolha in list('12'):
            
            if escolha=='1':
                opcoes_1()
                menu_1()
 
            elif escolha=='2':
                opcoes_2()
                menu_2()
                
                         
        elif escolha=='3':
            print("Fim do programa")
            
        else:
            print("Opção inválida")
        
main()