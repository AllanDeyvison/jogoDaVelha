def imprimir_tabuleiro(tab):
    for linha in tab:
        print(" | ".join(linha))
        print("-" * 9)

def verificar_vitoria(tab, jogador):
    # Verifica linhas, colunas e diagonais para ver se o jogador atual ganhou
    for i in range(3):
        if all([c == jogador for c in tab[i]]) or all([tab[j][i] == jogador for j in range(3)]):
            return True
    if tab[0][0] == jogador and tab[1][1] == jogador and tab[2][2] == jogador:
        return True
    if tab[0][2] == jogador and tab[1][1] == jogador and tab[2][0] == jogador:
        return True
    return False

def jogo_da_velha():
    tabuleiro = [[" " for _ in range(3)] for _ in range(3)]
    jogadores = ["X", "O"]
    nomes = {}

    # Obtém os nomes dos jogadores
    for jogador in jogadores:
        nomes[jogador] = input(f"Digite o nome do jogador {jogador}: ")

    turno = 0
    while True:
        imprimir_tabuleiro(tabuleiro)
        jogador_atual = jogadores[turno % 2]
        print(f"Vez do(a) {nomes[jogador_atual]} ({jogador_atual})")

        # Jogador escolhe onde jogar
        linha, coluna = map(int, input("Escolha a linha e a coluna para jogar (ex: 1 2): ").split())
        if tabuleiro[linha - 1][coluna - 1] != " ":
            print("Posição já ocupada, escolha outra.")
            continue

        # Atualiza o tabuleiro
        tabuleiro[linha - 1][coluna - 1] = jogador_atual

        # Verifica se o jogador atual ganhou
        if verificar_vitoria(tabuleiro, jogador_atual):
            imprimir_tabuleiro(tabuleiro)
            print(f"Parabéns, {nomes[jogador_atual]}! Você ganhou!")
            break

        # Verifica se o tabuleiro está cheio
        if all(all(c != " " for c in linha) for linha in tabuleiro):
            imprimir_tabuleiro(tabuleiro)
            print("Empate!")
            break

        turno += 1

if __name__ == "__main__":
    jogo_da_velha()
