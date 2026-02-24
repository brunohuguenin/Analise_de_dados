letras = ("a", "b", "c", "d", "e")
valor = input("Digite uma letra")

if valor in letras:
  print(f"Posição: {letras.index(valor)}")
else:
  print("Letra não encontrada.")