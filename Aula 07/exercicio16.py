def verificarNum(num):
  if num > 0:
    return "positivo"
  elif num < 0:
    return "negativo"
  else:
    return "zero"
  
valor = int(input("Digite um número: "))

print(f"O número {valor} é {verificarNum(valor)}")