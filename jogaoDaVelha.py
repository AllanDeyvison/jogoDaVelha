def posicoesTabuleiro(tabuleiro):
    altura = len(tabuleiro)
    largura = len(tabuleiro[0]) if altura > 0 else 0

    for i in range(altura):
        for n in range(largura):
            print(f'{i * largura + n + 1}', end=' ')
        print()

def jogada(posicao, tabuleiro, simbolo):
    try:
        x, y = map(int, posicao.split())
        if 1 <= x <= len(tabuleiro) and 1 <= y <= len(tabuleiro[0]):
            tabuleiro[x-1][y-1] = simbolo
            print(f"Jogada realizada em ({x}, {y})")
        else:
            raise ValueError("Posição inválida.")
    except ValueError as e:
        print(e)

def ganhou(tabuleiro, jogador):
    if linha_igual(tabuleiro, jogador):
        print(f"{jogador} ganhou!")
        return True
    elif coluna_igual(tabuleiro, jogador):
        print(f"{jogador} ganhou!")
        return True
    elif diagonais_iguais(tabuleiro, jogador):
        print(f"{jogador} ganhou!")
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

    if len(diagonal_principal) == 1 and diagonal_principal.pop() == jogador:
        return True
    if len(diagonal_secundaria) == 1 and diagonal_secundaria.pop() == jogador:
        return True
    return False

# Exemplo de uso
tabuleiro = [[' ' for _ in range(3)] for _ in range(3)]
print("Escolha o símbolo (X ou O): ", end="")
simbolo = input().upper()
while True:
    print("\nTabuleiro:")
    posicoesTabuleiro(tabuleiro)
    print("\nDigite a posição da sua jogada (ex: 1 2): ", end="")
    jogada(input(), tabuleiro, simbolo)
    if ganhou(tabuleiro, simbolo):
        break
