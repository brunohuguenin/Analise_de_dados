def dividir(a, b):
  try:
    resultado = float(a) / float(b)
  except ZeroDivisionError:
    print("Erro: divisão por zero não é permitida!")
  except ValueError:
    print("Erro: valor inválido informado!")
  else:
    print(f"Resultado da divisão: {resultado}")
  finally:
    print("Operação finalizada (com ou sem erro).")


num1 = input("Digite o numerador:")
num2 = input("Digite o divisor: ")

dividir(num1, num2)

