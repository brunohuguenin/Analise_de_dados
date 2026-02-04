valor = input("Entre com uma letra: ")
nota = valor.upper()

match nota:
  case "A":
    print("Excelente")
  case "B":
    print("Bom")
  case "C":
    print("Regular")
  case "D":
    print("Ruim")
  case "F":
    print("Reprovado")