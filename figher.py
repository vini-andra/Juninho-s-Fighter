import pygame 

"""
A classe de lutador é sobre um conteúdo do sétimo semestre, 
a programaçao orientada a objeto.

A programação orientada a objeto serve para criar classes e objetos,
que são instâncias de uma classe.
"""
class Fighter:
    def __init__(self, x, y): #
        self.rect = pygame.Rect((x, y, 80, 180)) #tamanho do retângulo. 80 de largura e 180 de altura

def move(self):
    SPEED = 10
    dx = 0 #direita ou esquerda
    dy = 0 #cima ou baixo
    
    key = pygame.kye.get_pressed()

    if key[pygame.K_a]:
        dx = -SPEED #faz o lutador ir para a esquerda  
    if key[pygame.K_d]:
        dx = SPEED #faz o lutador ir para a direita

    #atualza a posição do jogador
    self.rect.x += dx
    self.rect.y += dy

def draw(self, surface):    #desenha o personagem
    pygame.draw.rect(surface, (255, 0, 0), self.rect) #(255, 0, 0) é o vódigo da cor