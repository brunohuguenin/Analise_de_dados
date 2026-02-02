# Jogo da Velha em Python

tabuleiro = [" " for _ in range(9)]

def mostrar_tabuleiro():
    print()
    print(f" {tabuleiro[0]} | {tabuleiro[1]} | {tabuleiro[2]} ")
    print("---+---+---")
    print(f" {tabuleiro[3]} | {tabuleiro[4]} | {tabuleiro[5]} ")
    print("---+---+---")
    print(f" {tabuleiro[6]} | {tabuleiro[7]} | {tabuleiro[8]} ")
    print()

def verificar_vitoria(jogador):
    combinacoes = [
        (0,1,2), (3,4,5), (6,7,8),  # linhas
        (0,3,6), (1,4,7), (2,5,8),  # colunas
        (0,4,8), (2,4,6)           # diagonais
    ]
    for a, b, c in combinacoes:
        if tabuleiro[a] == tabuleiro[b] == tabuleiro[c] == jogador:
            return True
    return False

def verificar_empate():
    return " " not in tabuleiro

jogador_atual = "X"

while True:
    mostrar_tabuleiro()
    try:
        jogada = int(input(f"Jogador {jogador_atual}, escolha uma posição (1-9): ")) - 1
        if jogada < 0 or jogada > 8:
            print("Posição inválida. Escolha de 1 a 9.")
            continue
        if tabuleiro[jogada] != " ":
            print("Essa posição já está ocupada!")
            continue
    except ValueError:
        print("Digite apenas números!")
        continue

    tabuleiro[jogada] = jogador_atual

    if verificar_vitoria(jogador_atual):
        mostrar_tabuleiro()
        print(f"🎉 Jogador {jogador_atual} venceu!")
        break

    if verificar_empate():
        mostrar_tabuleiro()
        print("😐 Empate!")
        break

    jogador_atual = "O" if jogador_atual == "X" else "X"
