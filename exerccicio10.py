import random

# 1) Mostrar os números pares entre 0 e 100:
'''
print("Os números pares entre 0 e 100 são:")
for i in range(0, 101):
  if  i % 2 == 0:
    print(i)
'''


# 2) Mostrar os números ímpares entre 1 e 111:
'''
print("Os números ímpares de 1 a 111 são:")
for i in range(1, 111):
  if i % 2 != 0:
    print(i)
'''


# 3) Teste 5 números e verifica se é par ou ímpar:

print("Testando 5 números aleatórios pra ver quais são pares e quais são ímpares:")
'''
for i in range(1, 6):
  valor = random.randint(1, 100)
  if valor % 2 == 0:
    print(f"Valor {valor} é par")
  else:
    print(f"O valor {valor} é ímpar")
'''

# 4) Faça uma tabuada de multiplicar com um número escolhido pelo usuário:
'''
print(" ==== TABUADA ====")

valor = int(input("Insira um valor: "))

for i in range(1, 11):
  print(f"{valor} x {i} = {valor * i}")

'''

# 5) Teste 5 entradas de novas, prova01, prova02 e prova03.
# Faça a média entre as provas e mostre a situação onde:
# Média >= 7 aprovado
# Média >= 5 recuperação
# Média < 5 reprovado

notaArray = []
for i in range(1, 6):
  nomeAluno = str(input("Insira o nome do aluno(a): "))

  prova1 = float(input(f"Insira  nota da prova 1: "))
  prova2 = float(input(f"Insira a nota da prova 2: "))
  prova3 = float(input(f"Insira a nota da prova 3: "))

  media = float((prova1 + prova2 + prova3) / 3)

  if media >= 7:
    print(f"Aluno(a) {nomeAluno} está aprovado com a média {media:.2f}")
  elif media >= 5:
    print(f"Aluno(a) {nomeAluno} está em recuperação com a média {media:.2f}")
  else:
    print(f"Aluno(a) {nomeAluno} está reprovado com a média {media:.2f}")

  

