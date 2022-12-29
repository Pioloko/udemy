


# Utilize compreensão de dicionários para construir o dicionário abaixo.



# {'chave1': 1, 'chave2': 4, 'chave3': 9, 'chave4': 16, 'chave5': 25, 'chave6': 36, 'chave7': 49, 'chave8': 64, 'chave9': 81}


print(sorted({f"chave{i}:{i*i}" for i in range(1,10)})) #faz dict virar lista

print({"chave"+str(i):x*x for i,x in enumerate(range(1,10),start=1)})

