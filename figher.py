import pygame

"""
A classe de lutador é sobre um conteúdo do sétimo semestre, 
a programação orientada a objeto.

A programação orientada a objeto serve para criar classes e objetos,
que são instâncias de uma classe.
"""
class Fighter:
    def __init__(self, x, y): #
        self.rect = pygame.Rect((x, y, 80, 180)) #tamanho do retângulo. 80 de largura e 180 de altura
        self.vel_y = 0
        self.jump = False #se não está pulando, False
        self.attacking = False
        self.attack_type = 0

    def move(self, screen_width, screen_height, surface, target):
        SPEED = 5
        GRAVITY =  2
        dx = 0 #direita ou esquerda
        dy = 0 #cima ou baixo
        
        key = pygame.key.get_pressed()  # corrigido aqui

        if key[pygame.K_a]:
            dx = -SPEED #faz o lutador ir para a esquerda  
        if key[pygame.K_d]:
            dx = SPEED #faz o lutador ir para a direita

        # pula
        if key[pygame.K_w] and self.jump == False: #quando pula uma vez, a opção de pulo fica desabilitada
            self.vel_y = -30  #faz o lutador ir para cima
            self.jump = True

        #ataque
        if key[pygame.K_r] or key[pygame.K_t]: 
            self.attack(surface, target)
            #determina qual tipo de ataque foi usado
            if key[pygame.K_r]:
                self.attack_type = 1
            if key[pygame.K_t]:
                self.attack_type = 2

        #coloca a gravidade
        self.vel_y += GRAVITY

        """
        Se colocar apenas o "self.vel_y += GRAVITY", que puxa o objeto para baixo,
        o objeto vai continuar indo para baixo mesmo que o jogador não esteja pressionando.
        Por isso, temps que conseguir um jeito de saber se o objeto está no chão ou não.
        """

        dy += self.vel_y #

        #confirma presenca do player na tela
        if self.rect.left + dx < 0:
            dx = 0 - self.rect.left
        if self.rect.right + dx > screen_width:
            dx = screen_width - self.rect.right
        if self.rect.bottom + dy > screen_height - 110:
            self.vel_y = 0
            self.jump = False #ativa o pulo quando o lutador toca o chão
            dy = screen_height - 110 - self.rect.bottom

        #atualza a posição do jogador
        self.rect.x += dx
        self.rect.y += dy

    def attack(self, surface, target):
        attacking_rect = pygame.Rect(self.rect.centerx, self.rect.y, 2 * self.rect.width, self.rect.height)
        if attacking_rect.colliderect(target.rect):
            print("UAUUUU")

        pygame.draw.rect(surface, (0, 255, 0), attacking_rect)

    def draw(self, surface):    #desenha o personagem
        pygame.draw.rect(surface, (255, 0, 0), self.rect) #(255, 0, 0) é o código da cor
