idade = int(input("Entre com sua idade: "))
categoria = int(input("Escolha a categoria\n[1] Natação\n[2] Corrida\n[3] Ciclismo\nOpeção: "))

while categoria < 1 or categoria > 3:
  print("Opção inválida. Tente novamente!")
  categoria = input("Escolha a categoria\n[1] Natação\n[2] Corrida\n[3] Ciclismo\nOpeção: ")

match categoria:
  case 1:
    if idade < 10:
      print("Você pertence a Categoria Mirim")
    elif idade <= 14:
      print("Você pertence a Categoria Infantil")
    else:
      print("Você pertence a Categoria Juvenil")
  case 2:
    if idade < 16:
      print("Você pertence a Categoria Júnior")
    else:
      print("Você pertence a Categoria Adulto")
  case 3:
    if idade >= 16:
      print("Você pertence a Categoria Profissional")
    else:
      print("Você pertence a Categoria Amador")