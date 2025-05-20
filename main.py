import pygame
from figher import Fighter

pygame.init()

#cria janela
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Juninho's Fighter")

#carrega imagem de fundo
background = pygame.image.load("assets/Background/background1.png").convert_alpha()

#função para desenhar o fundo
def draw_background():
    scaled_background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT)) 
    screen.blit(scaled_background, (0, 0))

#cria instâncias de jogador
player_1 = Fighter(200, 310) #posição x e y, para aparecer na tela
player_2 = Fighter(700, 310)

#loop para manter a janela aberta
run = True
while run:

    #desenha o fundo
    draw_background()

    #move os personagens
    player_1.move()
    player_2.move()

    #desenha os lutadores
    player_1.draw()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False 

    #atualiza a tela
    pygame.display.update()

#sai do pygame
pygame.quit()