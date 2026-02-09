# Criar um algoritmo em Python que tenha a entrada de nome e salário bruto.
# Com função, resolve as situações abaixo:
# INSS:
# Se o salário bruto >= 1800 desconte 11%
# Se o salário bruto < 1800 desconte 9%
# Vale transporte
# Se o salário bruto >= 1500 desconte 6%
# Se o salário bruto < 1500 desconte 5%
# Bônus:
# Se o salário bruto >= 1240 some com mais 700 reais
# Se o salário bruto < 1240 some com mais 500 reais
# Cargo:
# Se o salário bruto >= 3000 = “Acionista”
# Se o salário bruto >= 2000 = “Gerente”
# Se o salário bruto < 2000 = “Vendedor”
# Salário Líquido:
# Salário Líquido = salário bruto – (inss + vale) + bônus

def inss(salarioBruto):
  
  if salarioBruto >= 1800:
    desconto = salarioBruto * 0.11
    return desconto
  else:
    desconto = salarioBruto * 0.09
    return desconto

def valeTransp(salarioBruto):
  if salarioBruto >= 1500:
    desconto = salarioBruto * 0.06
    return desconto
  else:
    desconto = salarioBruto * 0.05
    return desconto

def acrescimoBonus(salarioBruto):
  if salarioBruto >= 1240:
    bonus = 700
    return bonus
  else:
    bonus = 500
    return bonus

def funCargo(salarioBruto):
  if salarioBruto >= 3000:
    return "Acionista"
  elif salarioBruto >= 2000:
    return "Gerente"
  else:
    return "Vendedor"
  
def salarioLiq(salarioBruto, descIss, descVT, bonus):
  salarioLiq = salarioBruto - descIss - descVT + bonus
  return salarioLiq


nome = input("Digite seu nome: ")
salarioBruto = float(input("Digite o valor do seu salário: R$ "))

descontoInss = inss(salarioBruto)
descontoVT = valeTransp(salarioBruto)
bonus = acrescimoBonus(salarioBruto)
cargo = funCargo(salarioBruto)
salarioLiquido = salarioLiq(salarioBruto, descontoInss, descontoVT, bonus)

print(f"{nome}\nCARGO: {cargo}\nSALÁRIO BRUTO: R${salarioBruto:.2f}\nDESCONTO INSS: R$ {descontoInss:.2f}\nDESCONTO VALE TRANSPORTE: R$ {descontoVT:.2f}\nBÔNUS: R$ {bonus:.2f}\nSALÁRIO LÍQUIDO: R$ {salarioLiquido:.2f}")