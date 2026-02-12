# Crie um programa que leia um número digitado pelo usuário e converta 
# para int. Se o valor não for numérico, mostre uma mensagem de erro

valor = input("Insira um valor númerico: ")
print(f"\nO valor '{valor}' foi inserido com o tipo: {type(valor)}.")
try:
  valorInt = int(valor)
  print(f"Após a conversão, o valor {valor} é um tipo {type(valorInt)}.\n")
except ValueError:
  print("ERRO: Valor inserido não é numérico.\n")
