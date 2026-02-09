# 3) Utilize a estrutura FOR na aplicação abaixo:
# O Usuário entra com um número de x de quantidade de testes da aplicação.
# Teremos a entrada de um nome e do salário bruto. Calcule os descontos
# abaixo com uma variável para armazenar a informação dos cálculos:
# Salário Bruto >= 5000 = 14 % de desconto
# Salário Bruto >= 4000 = 12 % de desconto
# Salário Bruto >= 2000 = 11 % desconto
# Salário < 2000 = 9 % de desconto
# Calcule no final o salário final = salário bruto – desconto.
# Mostre todas informações do algoritmo no final da aplicação:

qtdTestes = int(input("Digite a quantidade de teste a ser aplicado: "))

if qtdTestes <= 0:
    print("Programa finalizado.")
else:
    for i in range(1, qtdTestes + 1):
        print()
        nome = str(input("Digite seu nome: "))
        salarioBruto = float(input("Digite o valor do seu salário: R$ "))

        if salarioBruto >= 5000:
            desconto = salarioBruto * 0.14
            salarioLiquido = salarioBruto - desconto
            print(f"NOME: {nome}\nSALÁRIO BRUTO: R$ {salarioBruto:.2f}\nDESCONTO DE 14%: R${desconto:.2f}\nSALÁRIO LÍQUIDO: R${salarioLiquido:.2f}")
        elif salarioBruto >= 4000:
            desconto = salarioBruto * 0.12
            salarioLiquido = salarioBruto - desconto
            print(f"NOME: {nome}\nSALÁRIO BRUTO: R$ {salarioBruto:.2f}\nDESCONTO DE 12%: R${desconto:.2f}\nSALÁRIO LÍQUIDO: R${salarioLiquido:.2f}")
        elif salarioBruto >= 2000:
            desconto = salarioBruto * 0.11
            salarioLiquido = salarioBruto - desconto
            print(f"NOME: {nome}\nSALÁRIO BRUTO: R$ {salarioBruto:.2f}\nDESCONTO DE 11%: R${desconto:.2f}\nSALÁRIO LÍQUIDO: R${salarioLiquido:.2f}")  
        else:
            desconto = salarioBruto * 0.09
            salarioLiquido = salarioBruto - desconto
            print(f"NOME: {nome}\nSALÁRIO BRUTO: R$ {salarioBruto:.2f}\nDESCONTO DE 9%: R${desconto:.2f}\nSALÁRIO LÍQUIDO: R${salarioLiquido:.2f}")
            print()