import pandas as pd

cargos = []
salarios = []

qtde = int(input("Quantos funcionários quer testar?: "))

for i in range(qtde):
  print(f"Cadastro nº{i + 1}")
  cargo = input("Cargo: ")
  salario = float(input("Salário: "))
  cargos.append(cargo)
  salarios.append(salario)

dados = {'cargos': cargos, 'salário': salarios}

df = pd.DataFrame(dados)

print(f"\nTabela de cargos e salários\n")
print(df)