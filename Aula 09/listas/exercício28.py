nomes = []

for i in range(5):
  nome = input(f"Digite o {i + 1}º nome: ")
  nomes.append(nome)

print(f"Os nomes digitados foram: {nomes}")

nomes_em_ordem = sorted(nomes)

print(f"A lista com os nomes em ordem alfabética: {nomes_em_ordem}")