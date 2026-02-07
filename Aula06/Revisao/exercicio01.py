# 1) Mostre os números de ímpares entre 1 e 501 utilizando a estrutura WHILE:

print("Os valores de 1 a 501 são:")

for i in range(1, 502):
    if i % 2 != 0:
        print(i)
