

# # Considere a lista a seguir.
# # com pares respectivos as capitais brasileiras e as temperaturas registradas para um determinado dia em 2020.
# # Use a função map() para converter as temperaturas de °C para K e F.





lista=[

    ('Boa Vista',32.4),

    ('Brasília',26.6),

    ('Campo Grande',28.8),

    ('Cuiabá',38.6),

    ('Salvador',37.1),

    ('São Paulo',38.8),

    ('Rio de Janeiro',34.7)

]
import math

temperatura_F=map(lambda x:(x[0],round(x[1]*(9/5)+32,1)),lista)
temperatura_K=map(lambda x:(x[0],round(x[1]+273)),lista)
print(list(temperatura_F))
print(list(temperatura_K))
# ====================================================

novo=map(lambda x:(x[0],round(x[1]*25)),lista)


print(list(novo))