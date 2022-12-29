# a) Use list() e zip() para criar uma nova lista de tuplas a partir da lista1 e lista2.

lista1=[1,2,3,4]
lista2=['Python','JavaScript','Java','HTML']



#result [(1, 'Python'), (2, 'JavaScript'), (3, 'Java'), (4, 'HTML')]

print(list(zip(lista1,lista2)))


# b) Use list() e zip() para criar uma nova lista de tuplas a partir da lista1 e lista2.

lista1=[40,50,60,70,80]
lista2=[-4,2,0,50,1]

print(list(zip(lista1,lista2)))

# result [(40, -4), (50, 2), (60, 0), (70, 50), (80, 1)]