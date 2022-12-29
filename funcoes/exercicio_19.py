# Considere a lista nomes a seguir e responda:



nomes=['','Roberto Carlos','Tom Jobim','Jorge Amado','Machado de Assis','Zé Ramalho','Elba Ramalho','','',[],()]
 

# a) obtenha uma nova lista sem os objetos vazios.

# output:
# filtro1=list(filter(lambda nome:len(nome)>0,nomes))
# filtro1=list(filter(None,nomes))
# print(filtro1)

['Roberto Carlos', 'Tom Jobim', 'Jorge Amado', 'Machado de Assis', 'Zé Ramalho', 'Elba Ramalho']


# b) obtenha uma nova lista que tenha apenas os nomes com o sobrenome Ramalho.

# output:

# filtro2=list(filter(lambda x : len(x)>0 and x.split()[-1] =="Ramalho",nomes ))


filtro2=list(filter(lambda x : x.split()[-1] == "Ramalho", nomes ))
print(filtro2)

['Zé Ramalho', 'Elba Ramalho']