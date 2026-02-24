import random

numeros = [random.randint(1, 100) for _ in range(50)]

numeros_pares = [n for n in range(50) if n % 2 == 0]

print("Os números pares de 0 a 49 são:")
print(numeros_pares)