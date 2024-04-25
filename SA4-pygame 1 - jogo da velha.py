import pygame
import sys

#inicializar o pygame
pygame.init()

#definir o tamanho da tela
TAMANHO_TELA = (300, 300)

# definir as cores
PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)
VERMELHO = (255, 0,0)
VERDE = (0, 255, 0)

#inicializar a tela
tela = pygame.display.set_mode(TAMANHO_TELA)
pygame.display.set_caption('Jogo da Velha')

#definir o tamanho do quadro e a largura da linha
TAMANHO_QUADRO = 100
LARGURA_LINHA = 5

# Inicializar variáveis
tabuleiro = [[""] * 3 for _ in range(3)]
jogador = "X"
fonte = pygame.font.Font(None, 60)

#função para desenhar o quadro
def desenhar_tabuleiro():
    tela.fill(BRANCO)
    # Linhas horizontais
    for linha in range(1, 3):
        pygame.draw.line(tela, PRETO, (0, linha * TAMANHO_QUADRO), (TAMANHO_TELA[0], linha * TAMANHO_QUADRO), LARGURA_LINHA)
    # Linhas verticais
    for coluna in range(1, 3):
        pygame.draw.line(tela, PRETO, (coluna * TAMANHO_QUADRO, 0), (coluna * TAMANHO_QUADRO, TAMANHO_TELA[1]), LARGURA_LINHA)

#função para verificar se alguém venceu
def checar_vencedor(tabuleiro):
    for linha in tabuleiro:
        if all(casa == jogador for casa in linha):
            return True
    for coluna in range(3):
        if all(tabuleiro[linha][coluna] == jogador for linha in range(3)):
            return True
    if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2]  == jogador:
        return True
    if tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] == jogador:
        return True
    return False

def exibir_mensagem(mensagem):
    texto = fonte.render(mensagem, True, PRETO)
    tela.blit(texto, (50, 130))

#função para desenhar X ou O
def desenhar_simbolo(jogador, linha, coluna):
    if jogador == 'X':
        cor = VERMELHO
    else:
        cor = VERDE
    x = coluna * TAMANHO_QUADRO + TAMANHO_QUADRO // 2
    y = linha * TAMANHO_QUADRO + TAMANHO_QUADRO // 2
    if jogador == 'X':
        pygame.draw.line(tela, cor, (x - 30, y - 30), (x + 30, y + 30), LARGURA_LINHA)
        pygame.draw.line(tela, cor, (x + 30, y + 30), (x - 30, y - 30), LARGURA_LINHA)
    else:
        pygame.draw.circle(tela, cor, (x, y), 30, LARGURA_LINHA)

#função principal
running = True
while running:
    desenhar_tabuleiro()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            linha = y // (TAMANHO_TELA[1] // 3)
            coluna = x // (TAMANHO_TELA[0] // 3)

            if tabuleiro[linha][coluna] == "":
                tabuleiro[linha][coluna] = jogador
                if checar_vencedor(tabuleiro):
                    exibir_mensagem(f"Jogador {jogador} venceu!")
                    running = False
                elif all(all(casa != "" for casa in linha) for linha in tabuleiro):
                    exibir_mensagem("Empate!")
                    running = False
                jogador = "O" if jogador == "X" else "X"
                desenhar_simbolo(jogador,linha,coluna)


    pygame.display.flip()

#sair do pygame
pygame.quit()
sys.exit()






