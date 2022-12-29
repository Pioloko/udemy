# a) Utilize a função map() para criar uma lista com o quadrado de cada número par e o cubo de cada número ímpar.
#  Considere o intervalo [1,20].



resultado2=[(1, 1), (2, 4), (3, 27), (4, 16), (5, 125), (6, 36), (7, 343), (8, 64), (9, 729), (10, 100), (11, 1331), (12, 144), (13, 2197), (14, 196), (15, 3375), (16, 256), (17, 4913), (18, 324), (19, 6859), (20, 400)]

# print(list(map(lambda x: (x,x*x) if x%2==0 else (x,x**3),range(1,21))))



# b) Utilize a função map() para criar uma lista com o os números divisíveis por 3 ou 5, no intervalo [1,50].
#  Se o número não for divisível calcule sua raiz quadrada.



resultado1=[1.0, 1.41, 3, 2.0, 5, 6, 2.65, 2.83, 9]

# print(list(map(lambda x:x if x%5==0 or x%3==0 else round(x**0.5,2),range(1,51))))



