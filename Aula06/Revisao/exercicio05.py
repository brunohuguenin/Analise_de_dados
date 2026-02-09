# 5) Faça uma aplicação em que tenha a entrada de um número e que
# produza na tela uma tabuada de multiplicar por esse número. Use a
# estrutura WHILE

print("=== TABUADA ===")
valor = int(input("Digite um valor: "))

repeticao = 0

while repeticao <= 10:
    print(f"{repeticao} x {valor} = {repeticao * valor}")

    repeticao+= 1

