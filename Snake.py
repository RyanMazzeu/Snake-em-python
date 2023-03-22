import pygame
import sys
import random
# Inicializa o Pygame
pygame.init()
# Define as cores
PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)
VERDE = (0, 255, 0)
VERMELHO = (255, 0, 0)
LARANJA = (255, 165, 0)
# Define as dimensões da tela
largura = 960
altura = 720
tela = pygame.display.set_mode((largura,altura))

# Define a fonte padrão
fonte_padrao = pygame.font.Font(None, 50)
fonte_titulo = pygame.font.Font(None, 80) 
fonte_pequena = pygame.font.Font(None, 30)
velocidade = 0

def menu():
    while True:
        # Trata os eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                elif event.key == pygame.K_j:
                    selecionar_dificuldade()
                elif event.key == pygame.K_c:
                    creditos()
                elif event.key == pygame.K_s:
                    pygame.quit()
                    sys.exit()

        # Desenha a tela do menu
        tela.fill(PRETO)
        
        ImagemFundoMenu = pygame.image.load("Background.png")
        tela.blit(ImagemFundoMenu, (0,0))

        texto_titulo = fonte_titulo.render("Snake Game", True, VERDE)
        tela.blit(texto_titulo, [largura/1.25 - texto_titulo.get_width()/2, 400])

        texto_jogar = fonte_padrao.render("Jogar (j)", True, BRANCO, VERMELHO)
        texto_jogar_rect = tela.blit(texto_jogar, [largura/1.25 - texto_jogar.get_width()/2, 460])

        texto_creditos = fonte_padrao.render("Créditos (c)", True, BRANCO, VERMELHO)
        texto_creditos_rect = tela.blit(texto_creditos, [largura/1.25 - texto_creditos.get_width()/2, 500])

        texto_sair = fonte_padrao.render("Sair (s)", True, BRANCO, VERMELHO)
        texto_sair_rect = tela.blit(texto_sair, [largura/1.25 - texto_sair.get_width()/2, 540])

        pygame.display.update()

def creditos():
    while True:
        # Trata os eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE or event.key == pygame.K_v:
                    menu()

        # Desenha a tela de créditos
        tela.fill(PRETO)
        ImagemFundoMenu = pygame.image.load("Background.png")
        tela.blit(ImagemFundoMenu, (0,0))

        texto_creditos = pygame.font.Font(None, 60) .render("Créditos", True, BRANCO)
        texto_autor = fonte_padrao.render("Autor: Ryan Mazzeu", True, BRANCO)
        texto_data = fonte_padrao.render("Data: 18/03/2023", True, BRANCO)
        texto_voltar = fonte_padrao.render("Voltar (v)", True, BRANCO)

        tela.blit(texto_creditos, [largura/1.25 - texto_creditos.get_width()/2, 400])
        tela.blit(texto_autor, [largura/1.25 - texto_autor.get_width()/2, 460])
        tela.blit(texto_data, [largura/1.25 - texto_data.get_width()/2, 500])
        tela.blit(texto_voltar, [largura/1.25 - texto_voltar.get_width()/2, 600])
        

        pygame.display.update()
    
def selecionar_dificuldade():
    while True:
        # Trata os eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE or event.key == pygame.K_v:
                    menu()
                elif event.key == pygame.K_f:
                    jogo(velocidade = 50)
                elif event.key == pygame.K_m:
                    jogo(velocidade = 25)
                elif event.key == pygame.K_d:
                    jogo(velocidade = 10)


        # Desenha a tela de seleção de dificuldade
        tela.fill(PRETO)
        ImagemFundoMenu = pygame.image.load("Background.png")
        tela.blit(ImagemFundoMenu, (0,0))

        texto_titulo = pygame.font.Font(None, 60) .render("Escolha a dificuldade:", True, BRANCO)
        tela.blit(texto_titulo, [largura/1.30 - texto_titulo.get_width()/2, 395])

        texto_facil = fonte_padrao.render("Fácil (Pressione F)", True, VERDE)
        tela.blit(texto_facil, [largura/1.25 - texto_facil.get_width()/2, 460])

        texto_medio = fonte_padrao.render("Médio (Pressione M)", True, LARANJA)
        tela.blit(texto_medio, [largura/1.25 - texto_medio.get_width()/2, 500])

        texto_dificil = fonte_padrao.render("Difícil (Pressione D)", True, VERMELHO)
        tela.blit(texto_dificil, [largura/1.25 - texto_dificil.get_width()/2, 540])

        pygame.display.update()


# Variáveis da cobra
tamanho_cobra = 20


# Função para desenhar a cobra
def desenhar_cobra(lista_cobra):
    for unidade in lista_cobra:
        pygame.draw.rect(tela, VERDE, [unidade[0], unidade[1], tamanho_cobra, tamanho_cobra])

def menu2(velocidade):
    # Variáveis do menu2

    fonte_grande = pygame.font.Font(None, 80)

    texto_titulo = fonte_grande.render("Jogo da Cobrinha", True, BRANCO)
    texto_instrucoes = fonte_pequena.render("Pressione qualquer tecla para começar", True, BRANCO)
   
    if(velocidade == 10):
        texto_dificuldade = fonte_pequena.render("Dificil", True, VERMELHO)  
    elif(velocidade == 25):
        texto_dificuldade = fonte_pequena.render("Medio", True, LARANJA) 
    else:
        texto_dificuldade = fonte_pequena.render("Facil", True, VERDE) 
    # Desenha o menu2 na tela
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                return

        tela.fill(PRETO)
        ImagemFundoMenu = pygame.image.load("Background.png")
        tela.blit(ImagemFundoMenu, (0,0))
        tela.blit(texto_titulo, [largura/2 - texto_titulo.get_width()/2, altura/2 - texto_titulo.get_height()])
        tela.blit(texto_dificuldade, [largura/2 - texto_dificuldade.get_width()/2, altura/2 + texto_dificuldade.get_height()])
        tela.blit(texto_instrucoes, [largura/2 - texto_instrucoes.get_width()/2, altura/2 + texto_titulo.get_height()])
        
        pygame.display.update()



# Função principal do jogo
def jogo(velocidade):
    menu2(velocidade)
    # Variáveis da cobra
    cobra_pos = [320, 240]
    cobra_corpo = [[320, 240], [310, 240], [300, 240]]
    direcao = "direita"

    # Variáveis da comida
    comida_pos = [random.randrange(1, largura/tamanho_cobra)*tamanho_cobra,
                  random.randrange(1, altura/tamanho_cobra)*tamanho_cobra]

    # Variáveis do jogo
    rodando = True

    # Loop principal do jogo
    while rodando:
        # Eventos do jogo
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                rodando = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and direcao != "direita":
                    direcao = "esquerda"
                elif event.key == pygame.K_RIGHT and direcao != "esquerda":
                    direcao = "direita"
                elif event.key == pygame.K_UP and direcao != "baixo":
                    direcao = "cima"
                elif event.key == pygame.K_DOWN and direcao != "cima":
                    direcao = "baixo"

        # Movimentação da cobra
        if direcao == "direita":
            cobra_pos[0] += tamanho_cobra
        elif direcao == "esquerda":
            cobra_pos[0] -= tamanho_cobra
        elif direcao == "cima":
            cobra_pos[1] -= tamanho_cobra
        elif direcao == "baixo":
            cobra_pos[1] += tamanho_cobra

        # Atualização da tela
        tela.fill(PRETO)
        desenhar_cobra(cobra_corpo)
        pygame.draw.rect(tela, VERMELHO, [comida_pos[0], comida_pos[1], tamanho_cobra, tamanho_cobra])
        pygame.display.update()

        # Verifica se a cobra comeu a comid
        if cobra_pos == comida_pos:
            comida_pos = [random.randrange(1, largura/tamanho_cobra)*tamanho_cobra,
                          random.randrange(1, altura/tamanho_cobra)*tamanho_cobra]
            cobra_corpo.append(list(cobra_pos))

        # Remove a cauda da cobra
# Move a cobra
        cobra_cauda = cobra_corpo.pop()
        cobra_cauda[0] = cobra_pos[0]
        cobra_cauda[1] = cobra_pos[1]
        cobra_corpo.insert(0, list(cobra_pos))

# Verifica colisão com as paredes
#       if cobra_pos[0] < 0 or cobra_pos[0] > largura-tamanho_cobra or cobra_pos[1] < 0 or cobra_pos[1] > altura-tamanho_cobra:
#         rodando = False
        if cobra_pos[0] < 0:
            cobra_pos[0] = largura-tamanho_cobra
        elif cobra_pos[0] > largura-tamanho_cobra:
            cobra_pos[0] = 0
        
        if cobra_pos[1] < 0:
            cobra_pos[1] = altura-tamanho_cobra
        elif cobra_pos[1] > altura-tamanho_cobra:
            cobra_pos[1] = 0
            
# Verifica colisão da cobra com o próprio corpo
        for parte in cobra_corpo[1:]:
            if cobra_pos == parte:
                rodando = False

# Delay do jogo
        pygame.time.delay(velocidade)

# Encerra o Pygame
    pygame.quit()

# Inicia o jogo
menu()

