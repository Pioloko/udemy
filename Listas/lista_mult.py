lista = []
vez=0
numero = int(input("numero "))

for i in range(1,numero+1):
    lista.append(i)


for num in lista:
    vez=vez+num
print(vez)