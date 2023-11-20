import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    def __init__(self, ai_settings, screen):
        super().__init__() 
        
        self.screen = screen 
        self.ai_settings =ai_settings

        self.image = pygame.image.load('/home/carlos_/Desktop/Projects/Python/Alien-Invasion/imagens/alien.bmp')
        
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width 
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    # Verifica se a nave atingiu a borda
    def check_edges(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right: 
            return True 
        elif self.rect.left <= 0: 
            return True
        
        
    # Update da posição da nave
    def update(self):
        self.x += (self.ai_settings.alien_speed_factor *self.ai_settings.fleet_direction) 
        self.rect.x = self.x
        

   

import pygame,sys

def check(confs,screen):
    for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                sys.exit()
def create(screeni): # arruamr dps
    y,x,l=0,0,0
    c = 0
    color = (0, 0, 0)
    while True:
        rects = pygame.draw.rect(screeni, color, (x, y, 75+x, 75+y))
        
        x += 75
        l += 1
        if c %2 == 0:
            
            color = (0, 0, 0)
        elif c % 2 != 1:
            color = (0, 255, 0)   
        
        c = c + 1
        print(c)
        if l == 8:
            y += 75
            x, l = 0, 0
            if c %2 == 0:
                c= c-1
            elif c % 2 == 1:
                c = c+1
        
        
                
        elif c == 65:
            break;
        # Verifica se o usuário pressionou a tecla Q
        # Altera a cor do quadrado
        if c % 2 == 0:
            color = (0, 0, 0)
        else:
            color = (0, 255, 0)

