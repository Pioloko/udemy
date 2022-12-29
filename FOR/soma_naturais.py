num=int(input("digite um numero final: "))
soma = 0

for i in range(0,num):
    if num<0:
        print("numero invalido")
    else:
        for i in range(num+1):
            soma +=i
    

print(soma)
