nome = input("Digite seu nome: ")
salarioBruto = float(input(f"Digite seu salário, Sr(a) {nome}: R$ "))

salarioComDescontoINSS = 0
salarioComDescontoVT = 0
salarioComBonus = 0
cargo = ""

if salarioBruto >= 3000:
  descontoINSS = salarioBruto * 0.11
elif  salarioBruto >= 2000 and salarioBruto < 3000:
  descontoINSS =   salarioBruto * 0.09
else:
  descontoINSS =  salarioBruto * 0.8

if salarioBruto >= 2000:
  descontoVT =  salarioBruto * 0.06
else:
  descontoVT =  salarioBruto * 0.05

if salarioBruto >= 3000:
  bonus = 300
else:
  bonus = 200

if salarioBruto >= 3000:
  cargo = "Acionista"
elif salarioBruto >= 2000 and salarioBruto < 3000:
  cargo = "Gerente"
else:
  cargo = "Vendedor"

salarioLiquido = salarioBruto - (descontoINSS + descontoVT) + bonus

print(f"NOME DO FUNCIONÁRIO: {nome}\nCARGO: {cargo}\nSALÁRIO BRUTO: R$ {salarioBruto:.2f}\nDESCONTO INSS: - R$ {descontoINSS:.2f}\nDESCONTO VALE TRANSPORTE: - R$ {descontoVT:.2f}\nSALÁRIO LÍQUIDO: R$ {salarioLiquido:.2f}")
