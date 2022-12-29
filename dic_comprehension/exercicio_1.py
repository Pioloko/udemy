# Nos exercícios anteriores utilizamos compreensão de listas para construir listas de uma forma rápida e 'pythônica' 
# utilizando uma notação simples.
# Os dicionários também suportam a mesma operação, 
# possibilitando uma construção simples e compacta combinando loops e estruturas condicionais.
# Nestes termos, podemos aplicar esse conceito para criar DataFrames com pandas, uma aplicação muito comum em Data Science.

# Sendo assim, utilize compreensão de dicionários para construir os dicionários abaixo.

# a) Crie um dicionário em que suas chaves serão os números 1, 4, 5, 6, 7, 9 (que podem ser armazenados em uma lista) e seus valores correspondem ao quadrado destes números.



# {1: 1, 4: 16, 5: 25, 6: 36, 7: 49, 9: 81}


# b) Crie um dicionário em que suas chaves correspondem a números inteiros entre [1,10] e cada valor associado é o número ao quadrado.

# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}


# c) Crie um dicionário em que suas chaves correspondem a números de 10 a 1 e seus respectivos valores denotam o cubo de cada chave.



# {10: 1000, 9: 729, 8: 512, 7: 343, 6: 216, 5: 125, 4: 64, 3: 27, 2: 8, 1: 1}


#a)
print({numero:numero**2 for numero in [1, 4, 5, 6, 7, 9]})
 
#b)
print({numero:numero**2 for numero in range(1,11)})
 
#c)
print({numero:numero**3 for numero in range(10,0,-1)})

