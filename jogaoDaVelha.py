def posicoesTabuleiro(tabuleiro):
    altura = len(tabuleiro)
    largura = len(tabuleiro[0]) if altura > 0 else 0

    for i in range(altura):
        for n in range(largura):
            if tabuleiro[i][n] == ' ':
                print(f'{i * largura + n + 1}', end=' ')
            else:
                print(tabuleiro[i][n], end=' ')
        print()
    # altura = len(tabuleiro)
    # largura = len(tabuleiro[0]) if altura > 0 else 0

    # for i in range(altura):
    #     for n in range(largura):
    #         print(f'{i * largura + n + 1}', end=' ')
    #     print()
    

def coordenadas(numUnico, largura):
    x = (numUnico - 1) // largura
    y = (numUnico - 1) % largura
    return x, y

def jogada(posicao, tabuleiro, simbolo):
    try:
        posicao = int(posicao)  # Converte a posição para inteiro
        largura = len(tabuleiro[0])
        x, y = coordenadas(posicao, largura)
        
        if 0 <= x < len(tabuleiro) and 0 <= y < len(tabuleiro[0]) and tabuleiro[x][y] == ' ':
            tabuleiro[x][y] = simbolo
            print(f"Jogada realizada em ({x + 1}, {y + 1})")
        else:
            raise ValueError("Posição inválida ou já ocupada.")
    except ValueError as e:
        print(e)

def ganhou(tabuleiro, jogador):
    if linha_igual(tabuleiro, jogador):
        print(f"{nomes[jogador]} ganhou!")
        return True
    elif coluna_igual(tabuleiro, jogador):
        print(f"{nomes[jogador]} ganhou!")
        return True
    elif diagonais_iguais(tabuleiro, jogador):
        print(f"{nomes[jogador]} ganhou!")
        return True
    return False

def linha_igual(tabuleiro, jogador):
    for linha in tabuleiro:
        if len(set(linha)) == 1 and linha[0] == jogador:
            return True
    return False

def coluna_igual(tabuleiro, jogador):
    for coluna in range(len(tabuleiro[0])):
        if len(set(tabuleiro[i][coluna] for i in range(len(tabuleiro)))) == 1 and tabuleiro[0][coluna] == jogador:
            return True
    return False

def diagonais_iguais(tabuleiro, jogador):
    diagonal_principal = set(tabuleiro[i][i] for i in range(len(tabuleiro)))
    diagonal_secundaria = set(tabuleiro[i][len(tabuleiro)-i-1] for i in range(len(tabuleiro)))

    if len(diagonal_principal) == 1 and jogador in diagonal_principal:
        return True
    if len(diagonal_secundaria) == 1 and jogador in diagonal_secundaria:
        return True
    return False

# Exemplo de uso
tabuleiro = [[' ' for _ in range(3)] for _ in range(3)]


jogadores = ["X", "O"]
nomes = {}

    # Obtém os nomes dos jogadores
for jogador in jogadores:
    nomes[jogador] = input(f"Digite o nome do jogador {jogador}: ")

turno = 0

while True:
    print("\nTabuleiro:")
    posicoesTabuleiro(tabuleiro)
    jogador_atual = jogadores[turno % 2]
    print(f"\nJogador {nomes[jogador_atual]} ({jogador_atual}) digite a posição da sua jogada (1-9): ", end="")
    jogada(input(), tabuleiro, jogador_atual)
    if ganhou(tabuleiro, jogador_atual):
        break

    turno += 1