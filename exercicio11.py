# 1) Mostre os números ímpares entre 1 e 31:
'''
for i in range(31):
  if i % 2 != 0:
    print(i)
'''

# 2) Mostrar os números pares entre 500 e 800:
'''
for i in range(500, 800):
  if i % 2 == 0:
    print(i)
'''

# 3) Faça uma tabuada de multiplicar com um número escolhido
# pelo usuário com while:
'''
valor = int(input("Insira um valor: "))
parada = 0

while parada < 11:
    print(f"{valor} x {parada} = {valor * parada}")
    parada += 1
'''


# 4
parada = 0

while parada < 5:
  nomeAluno = str(input(f"Insira o nome do {parada + 1}º aluno(a): "))

  nota1 = float(input("Insira a primeira nota da primeira prova: "))
  nota2 = float(input("Insira a segunda nota da primeira prova: "))
  nota3 = float(input("Insira a terceira nota da primeira prova: "))

  media = (nota1 + nota2 + nota3) / 3

  if media >= 7:
    print(f"Aluno(a) foi aprovado com a média {media:.2f}")
  elif media >= 5:
    print(f"Aluno(a) está em recuperação com a média {media:.2f}")
  else:
    print(f"Aluno(a) está reprovado com a média {media:.2f}")

  parada += 1