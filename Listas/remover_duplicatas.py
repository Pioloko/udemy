lista=[
    'a','a','a',
    'b','c','k',
    'a',1,2,3,4,
    'j','l','m',
]

lista_nova = []
for i in lista:
    if i in lista_nova:
        pass
    else:
        lista_nova.append(i)

print(lista_nova)



lista=list(set(lista))
print(lista)