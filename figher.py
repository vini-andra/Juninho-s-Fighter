import pygame

"""
A classe de lutador é sobre um conteúdo do sétimo semestre, 
a programação orientada a objeto.

A programação orientada a objeto serve para criar classes e objetos,
que são instâncias de uma classe.
"""
class Fighter:
    def __init__(self, x, y, flip, data, sprite_sheet, animation_steps): #
        self.size = data[0]
        self.image_scale = data[1]
        self.offset = data[2]
        self.flip = flip
        self.animation_list = self.load_images(sprite_sheet, animation_steps)
        self.action = 0 #0:idle #1:run #2:jump #3:attack1 #4: attack2 #5:hit #6:death
        self.frame_index = 0
        self.image = self.animation_list[self.action][self.frame_index]
        self.update_time =pygame.time.get_ticks()
        self.rect = pygame.Rect((x, y, 80, 180)) #tamanho do retângulo. 80 de largura e 180 de altura
        self.vel_y = 0
        self.jump = False #se não está pulando, False
        self.attacking = False
        self.attack_type = 0
        self.health = 100
        
    def load_images(self, sprite_sheet, animation_steps):
        #extrai as imagens do spritesheet
        animation_list = []
        for y, animation in enumerate(animation_steps):
            temp_img_list = []
            for x in range(animation):
                temp_img = sprite_sheet.subsurface(x * self.size, y * self.size, self.size, self.size)
                pygame.transform.scale(temp_img, (self.size * self.image_scale, self.size * self.image_scale))
                temp_img_list.append(pygame.transform.scale(temp_img, (self.size * self.image_scale, self.size * self.image_scale)))
            animation_list.append(temp_img_list)
        return animation_list
    
    def move(self, screen_width, screen_height, surface, target):
        SPEED = 5
        GRAVITY =  2
        dx = 0 #direita ou esquerda
        dy = 0 #cima ou baixo

        key = pygame.key.get_pressed()  # corrigido aqui
        
        #pode fazer outras acoes se nao estiver atacando
        if self.attacking == False:
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
        if self.rect.bottom + dy > screen_height - 40:
            self.vel_y = 0
            self.jump = False #ativa o pulo quando o lutador toca o chão
            dy = screen_height - 40 - self.rect.bottom

        #certifica que os players olhem um para o outro
        if target.rect.centerx > self.rect.centerx:
            self.flip = False
        else:
            self.flip = True

        #atualza a posição do jogador
        self.rect.x += dx
        self.rect.y += dy 
        
    #organiza as mudancas de animacao
    def update(self):
        animation_cooldown = 500
        #atualiza as imagens
        self.image = self.animation_list[self.action][self.frame_index]
        #analisa se passou tempo suficiente desde o ultimo update
        if pygame.time.get_ticks() - self.update_time > animation_cooldown:
            self.frame_index += 1
            self.update_time = pygame.time.get_ticks()

    def attack(self, surface, target):
        self.attacking = True
        attacking_rect = pygame.Rect(self.rect.centerx - (2 * self.rect.width * self.flip), self.rect.y, 2 * self.rect.width, self.rect.height)
        if attacking_rect.colliderect(target.rect):
            target.health -= 10

        pygame.draw.rect(surface, (0, 255, 0), attacking_rect)

    def draw(self, surface):    #desenha o personagem
        img = pygame.transform.flip(self.image, self.flip, False)
        pygame.draw.rect(surface, (255, 0, 0), self.rect) #(255, 0, 0) é o código da cor
        surface.blit(img, (self.rect.x - (self.offset[0] * self.image_scale), self.rect.y - (self.offset[1] * self.image_scale)))
