def maiorValor(val1, val2, val3):
  maior = val1

  if val1 < val2:
    if val2 > val3:
      maior = val2
      return maior
    else:
      maior = val3
      return maior
  elif val1 < val3:
    if val3 > val2:
      maior = val3
      return maior
    else:
      maior = val2
      return maior
  else:
    maior
    return maior



valor1 = int(input("Digite o primeiro valor: "))
valor2 = int(input("Digite o segundo valor: "))
valor3 = int(input("Digite o terceiro valor: "))

print(f"O maior valor inserido é o {maiorValor(valor1, valor2, valor3)}")
