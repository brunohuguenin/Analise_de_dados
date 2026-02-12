# 4 - Peça dois números e uma operação. Use try-except-else-finally para tratar erros como divisão por zero e operação inválida. Utilize a estrutura match case para decidir com os caracteres abaixo suas  respectivas operações:
def adicao(x:float, y:float):
  op = x + y
  resultado = print(f"{x:.0f} + {y:.0f} = {op:.0f}")
  return resultado

def subtracao(x:float, y:float):
  op = x - y
  resultado = print(f"{x:.0f} - {y:.0f} = {op:.0f}")
  return resultado

def divisao(x:float, y:float):
  try:
    op = x / y
    resultado = print(f"{x:.0f} / {y:.0f} = {op}")
    return resultado
  except ZeroDivisionError:
    print("ERRO: O divisor não pode ser zero!")
  finally:
    ""

def multiplicacao(x:float, y:float):
  op = x * y
  resultado = print(f"{x:.0f} * {y:.0f} = {op:.0f}")
  return resultado


try:
  print("== CALCULADORA ===")
  num1 = float(input("Insira o primeiro valor: "))
  num2 = float(input("Insira o segundo valor: "))
  operacao = input("[+] ADIÇÃO\n[-] SUBTRAÇÃO\n[/] DIVISÃO\n[*] MULTIPLICAÇÃO\nOperação: ")

  match operacao:
    case "+":
      adicao(num1, num2)
    case "-":
      subtracao(num1, num2)
      
    case "/":
      divisao(num1, num2)
      
    case "*":
      multiplicacao(num1, num2)
      
except ValueError:
  print("Valor inserido é inválido!")
finally:
  print("Programa encerrado.")


