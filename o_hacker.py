import pygame

# Inicialização
pygame.init()

# tela e resolução
screen = pygame.display.set_mode((1200, 900))

# Título e ícone (atribuir créditos do ícone?)
pygame.display.set_caption("O Hacker")
icon = pygame.image.load("img/icone/man.png")
pygame.display.set_icon(icon)

# Desktop
pasta1_img = pygame.image.load('img/desktop/pasta.png')
pasta1_X = 600
pasta1_Y = 450

def desktop():
    screen.blit(pasta1_img, (pasta1_X, pasta1_Y))

# Loop do jogo
running = True

while running:

    # RGB
    screen.fill((0, 0, 90))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    desktop()

    pygame.display.update()