num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
opcao = int(input("Digite a operação que deseja realizar:\n[1] Adição\n[2] Subtração\n[3] Multiplicação\n[4] Divisão\nOpção: "))

'''while opcao < 1 or opcao > 4: 
  print("Operação inválida. Tente novamente.")
  opcao = str(input("Digite a operação que deseja realizar:\n[1] Adição\n[2] Subtração\n[3] Multiplicação\n[4] Divisão\nOpção: "))'''

match opcao:
  case 1:
    resultado = num1 + num2
    print(resultado)
  case 2:
    resultado = num1 - num2
    print(resultado)
  case 3:
    resultado = num1 * num2
    print(resultado)
  case 4:
    resultado = num1 / num2
    print(resultado)
