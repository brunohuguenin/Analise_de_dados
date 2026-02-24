numeros = []

quantidade = int(input("Digite a quantos números você quer: "))

for i in range(quantidade):
  numero = int(input(f"Digite o {i + 1}º número: "))
  numeros.append(numero)

print(f"Números digitados: {numeros}")

numeros_pares = [p for p in numeros if p % 2 == 0]
print(f"Os números pares da lista que digitou:\n{numeros_pares}")

numeros_impares = [i for i in numeros if i % 2 != 0]
print(f"Os números ímpares da lista que digitou:\n{numeros_impares}")