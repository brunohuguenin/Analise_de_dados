numeros = []

quantidade = int(input("Digite a quantos números você quer: "))

for i in range(quantidade):
  numero = int(input(f"Digite o {i + 1}º número: "))
  numeros.append(numero)

print(f"Números digitados: {numeros}\n")

numeros_pares = [p for p in numeros if p % 2 == 0]
print(f"Os números pares da lista que digitou: {numeros_pares}\n")

numeros_impares = [i for i in numeros if i % 2 != 0]
print(f"Os números ímpares da lista que digitou: {numeros_impares}\n")

print(f"O maior número digitado é o: {max(numeros)}\n")
print(f"O menor número digitado é o: {min(numeros)}\n")
print(f"A soma dos números digitados é igual a: {sum(numeros)}\n")
print(f"A quantidade de números digitados é igual a: {len(numeros)}\n")
