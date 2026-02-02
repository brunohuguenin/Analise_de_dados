diaSemana = int(input("Digite um número de 1 a 7: "))

while diaSemana < 1 or diaSemana > 7:
  print("Valor invalido!")
  diaSemana = int(input("Digite um número de 1 a 7: "))

match diaSemana:
  case 1:
    print("Domingo")
  case 2:
    print("Segunda-feira")
  case 3:
    print("Terça-feira")
  case 4:
    print("Quarta-feira")
  case 5:
    print("Quinta-feira")
  case 6:
    print("Sexta-feira")
  case 7:
    print("Sábado")

    