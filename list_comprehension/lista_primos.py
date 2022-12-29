# Utilize Compreensão em Lista (List Comprehension) para criar a lista a seguir.

# [1, 3, 5, 7, 9]



print([i for i in range(1,11) if i%2!=0])

lista = []
for i in range(1,11):
    if i%2==0:
        pass
    else:
        lista.append(i)

print(lista)



