# 2 - Leia duas notas, calcule a média e trate erros de entrada (valor inválido ou divisão incorreta)

try:
  nota1 = float(input("Digite a primeira nota: "))
  nota2 = float(input("Digite a segunda nota: "))
  
  operacao = (nota1 + nota2) / 2

  resultado = print(f"A média final é igual a {operacao:.2f}")
  
except ValueError:
  print("ERRO: O valor das notas devem ser numéricos!")
finally:
  print("Programa encerrado.")




