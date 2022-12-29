alvo=int(input("digite o ultimo numero do range: "))

for numero in range(2,alvo+1):
    primo=True
    for i in range(2,numero//2):
        if numero%i==0:
            primo = False
            break
    if primo:
        print(numero)
