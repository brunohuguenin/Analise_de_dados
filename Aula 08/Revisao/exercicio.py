def dividir(a, b):
  operacao = a / b
  return operacao

numerador = float(input("Insira o valor do numerador: "))
divisor = float(input("Insira o valor do divisor: "))

while divisor == 0:
  print("\nDIVISOR NÃO PODE SER ZERO!")
  divisor = float(input("Insira o valor do divisor: "))

resultado = dividir(numerador, divisor)

print(f"{numerador:.0f} ÷ {divisor:.0f} = {resultado:.0f}")
