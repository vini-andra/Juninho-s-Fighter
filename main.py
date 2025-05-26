import pygame
from figher import Fighter

pygame.init()

#cria janela
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Juninho's Fighter")

#define a framerate
clock = pygame.time.Clock()
fps = 60

#define as cores
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)


#carrega imagem de fundo
background = pygame.image.load("assets/Background/background1.jpeg").convert_alpha()

#função para desenhar o fundo
def draw_background():
    scaled_background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT)) 
    screen.blit(scaled_background, (0, 0))

#funcao das barras de vida
def draw_health_bar(health, x, y):
    ratio = health / 100
    pygame.draw.rect(screen, WHITE, (x - 2,y - 2, 404, 34))
    pygame.draw.rect(screen, RED, (x, y, 400, 30))
    pygame.draw.rect(screen, YELLOW, (x, y, 400 * ratio, 30))

#cria instâncias de jogador
player_1 = Fighter(200, 310) #posição x e y, para aparecer na tela
player_2 = Fighter(700, 310)

#loop para manter a janela aberta
run = True  
while run:
    
    #define a framerate
    clock.tick(fps)

    #desenha o fundo
    draw_background()
    
    #mostra os status do personagem
    draw_health_bar(player_1.health, 20, 20)
    draw_health_bar(player_2.health, 580, 20)
    

    #move os personagens
    player_1.move(SCREEN_WIDTH, SCREEN_HEIGHT, screen, player_2)
    #player_2.move(SCREEN_WIDTH, SCREEN_HEIGHT, screen, player_1)

    #desenha os lutadores
    player_1.draw(screen)
    player_2.draw(screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False 

    #atualiza a tela
    pygame.display.update()

pygame.quit() 