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
lixeira_img = pygame.image.load('img/desktop/bin.png')
lixeiraX = 80
lixeiraY = 100

pastaDados_img = pygame.image.load('img/desktop/pasta_dados.png')
pastaDadosX = 80
pastaDadosY = 200

cmd_img = pygame.image.load('img/desktop/cmd.png')
cmdX = 80
cmdY = 300

def pastaDados():
    screen.blit(pastaDados_img, (pastaDadosX, pastaDadosY))

def lixeira():
    screen.blit(lixeira_img, (lixeiraX, lixeiraY))

def cmd():
    screen.blit(cmd_img, (cmdX, cmdY))


# Loop do jogo
running = True

while running:

    # RGB
    screen.fill((200, 200, 255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pastaDados()
    lixeira()
    cmd()

    pygame.display.update()