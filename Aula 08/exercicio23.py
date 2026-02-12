
class NumeroPositivoErro(Exception):
  pass

try:
  nome = input("Digite seu nome: ")
  idade = int(input("Insira sua idade: "))

  if idade <= 0:
    raise NumeroPositivoErro

  print(f"NOME: {nome}\nIDADE: {idade}")
except ValueError:
  print("ERRO: Valor inválido!")
except NumeroPositivoErro:
  print("ERRO: A idade deve ser maior que zero")
finally:
  print("Programa encerrado.")