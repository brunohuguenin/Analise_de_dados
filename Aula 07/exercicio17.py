def media(nota):
  if nota >= 7:
    return "Você está aprovado."
  elif nota >= 5:
    return "Você está de recuperação."
  else:
    return "Você está reporvado."



nota = float(input("Digite sua nota: "))

print(media(nota))