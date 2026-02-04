print("Escolha uma opção:\n[1] Teste PAR ou ÍMPAR\n[2] Verifique (maior ou menor)\n[3] O dobro")

continuar = "s"

while continuar == "s":
  opcao = int(input("Digite a opção desejada: "))
  match opcao:
    case 1:
      print("[1] Teste PAR ou ÍMPAR")
      numero = int(input("Digite o número desejado: "))
      if numero % 2 == 0:
        print(f"O número {numero} é PAR")
      else:
        print(f"O número {numero} é ÍMPAR")
    case 2:
       print("[2] Verifique (maior ou menor)")
       valor1 = int(input("Digite o primeiro número inteiro: "))
       valor2 = int(input("Digite o segundo número inteiro: "))
       if valor1 > valor2:
         print(f"O número {valor1} é maior que o número {valor2}")
       else:
        print(f"O número {valor2} é maior que o número {valor1}")
    case 3:
      print("[3] O dobro")
      valor = int(input("Digite um número para saber o seu dobro: "))
      print(f"O dobro do número {valor} é igual a {valor*2}")

  continuar = input("Deseja continuar? (s/n): ").strip().lower()
  if continuar != "s":
    print("Programa encerrado.")
    break
