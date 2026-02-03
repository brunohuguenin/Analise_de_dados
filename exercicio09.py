# Revisar o assunto da aula passada
opcao = int(input("Escolha uma opção:\n[1] Saber se o número é PAR ou ÍMPAR\n[2] Saber qual valor é o maior entre dois\n[3] Saber o dobro do valor inserido\nOpção: "))

while opcao < 1 or opcao > 3:
  print("Opção inválida. Tente novamente.")
  opcao = int(input("Escolha uma opção:\n[1] Saber se o número é PAR ou ÍMPAR\n[2] Saber qual valor é o maior entre dois\n[3] Saber o dobro do valor inserido\nOpção: "))

match opcao:
  case 1:
    valor = int(input("Insira o valor: "))
    if valor % 2 == 0:
      print(f"O valor inserido é PAR")
    else:
      print(f"O valor inserido é ÍMPAR")
  case 2:
    valor1 = int(input("Insira o primeiro valor: "))
    valor2 = int(input("Insira o segundo valor: "))

    if valor1 > valor2:
      print(f"O número {valor1} é maior que o número {valor2}")
    else:
      print(f"O número {valor2} é maior que p número {valor1}")

  case 3:
    valor = int(input("Insira o valor: "))
    valorDobrado = valor * 2
    print(f"O dobro de {valor} é igual a {valorDobrado}")












'''
import random

# Exercício 01
valor1 = random.randint(1, 100)

print(valor)

if valor % 2 ==0:
  print(f"O número {valor1} é PAR")
else:
  print(f"O número {valor1} é ÍMPAR")



# Exercício 02
valor1 = random.randint(1,100)
valor2 = random.randint(1,100)

if valor1 > valor2:
  print(f"O número {valor1} é maior que o número {valor2}")
elif valor2 > valor1:
  print(f"O número {valor2} é maior que o número {valor1}")
else:
  print(f"O número {valor1} e o número {valor2} são iguais.")


# Exercício 03

valor = random.randint(1, 100)

valorDobrado = valor * 2

print(f"O dobro de {valor} é igual a {valorDobrado}")
'''