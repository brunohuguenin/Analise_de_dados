for aluno_num in range(10):
    notas = []

    aluno = input(f"Digite o nome do aluno {aluno_num + 1}: ")

    for nota_num in range(3):
        nota = float(input(f"{nota_num + 1}ª nota: "))
        notas.append(nota)

    media = sum(notas) / len(notas)

    if media >= 7:
        situacao = "Aprovado"
    elif media >= 5:
        situacao = "Recuperação"
    else:
        situacao = "Reprovado"

    print("\n--- Resultado ---")
    print(f"Aluno: {aluno}")

    for i in range(len(notas)):
        print(f"Nota {i + 1}: {notas[i]}")

    print(f"Média: {media:.2f}")
    print(f"Situação final: {situacao}")
    print("----------------\n")
