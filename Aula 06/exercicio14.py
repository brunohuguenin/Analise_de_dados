# riar um programa que leia a altura e o peso de N pessoas e mostre
# seu IMC com a respectiva classificação. O cálculo do IMC deverá ser
# realizado através de uma função que receberá os valores de entrada
# necessários para o cálculo.
# Fórmula --> IMC = PESO / (ALTURA * ALTURA)



def imc(peso, altura):
  calculoIMC = peso / (altura * altura)
  return calculoIMC

def classificacaoImc(nome, calculoIMC):

  if calculoIMC < 16.9:
    return print(f"{nome}, seu IMC é igual a {calculoIMC:.2f} que significa que está MUITO ABAIXO DO PESO")
  elif calculoIMC >= 17 and calculoIMC <= 18.4:
    return print(f"{nome}, seu IMC é igual a {calculoIMC:.2f} que significa que está ABAIXO DO PESO")
  elif calculoIMC >= 18.5 and calculoIMC <= 24.9:
    return print(f"{nome}, seu IMC é igual a {calculoIMC:.2f} que significa que está PESO NORMAL")
  elif calculoIMC >= 25 and calculoIMC <= 29.9:
    return print(f"{nome}, seu IMC é igual a {calculoIMC:.2f} que significa que está ACIMA DO PESO")
  elif calculoIMC >= 30 and calculoIMC <= 34.49:
    return print(f"{nome}, seu IMC é igual a {calculoIMC:.2f} que significa que está OBESIDADE GRAU I")
  elif calculoIMC >= 35 and calculoIMC <= 40:
    return print(f"{nome}, seu IMC é igual a {calculoIMC:.2f} que significa que está OBESIDADE GRAU II")
  elif calculoIMC > 40:
    return print(f"{nome}, seu IMC é igual a {calculoIMC:.2f} que significa que está OBESIDADE GRAU III")



print("=== CÁLCULO DE IMC ===\n")

nome = str(input("Digite seu nome: "))
peso = float(input("Digite seu peso (Kg): "))
altura = float(input("Digite sua altura: "))

valorImc = imc(peso, altura)
classificacaoImc(nome, valorImc)

opcao = int(input("Deseja inserir outra pessoa?\n[1] SIM\n[0] NÃO\nOpção: "))

while opcao == 1:
  nome = str(input("\nDigite seu nome: "))
  peso = float(input("Digite seu peso (Kg): "))
  altura = float(input("Digite sua altura: "))

  valorImc = imc(peso, altura)
  classificacaoImc(nome, valorImc)