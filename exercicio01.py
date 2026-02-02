nome = (input("Digite seu nome: "))
salario = float(input("\nDigite seu salário: "))
desconto = (salario * 0.11)
salarioLiquido = float(salario - desconto)

print(f"\nNome do funcionário {nome}\nDesconto do salário R$ {desconto:.2f}\nSalário líquido R$ {salarioLiquido:.2f}")
