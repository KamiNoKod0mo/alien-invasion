import pygame
from pygame.sprite import Sprite

class Ship(Sprite):# Classe para criação da nave
    def __init__(self, ai_settings,screen):
        super(Ship, self).__init__()
        
        #variavel scren do codigo principal e do settings.py
        self.screen = screen
        self.ai_settings = ai_settings 

        #carrega imagem bmp
        self.image = pygame.image.load("/home/carlos_/Desktop/Projects/Python/Alien-Invasion/imagens/ship.bmp")
        self.image = pygame.transform.scale(self.image, (50, 50))

        # Pega o atributo rec da janela
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # seta a nave para aparecer no centro inferior, e converte em float, pois em settings esta em float
        self.rect.centerx = self.screen_rect.centerx 
        self.center = float(self.rect.centerx)
        self.rect.bottom = self.screen_rect.bottom

        #Variaveis para o movimento continuo
        self.moving_right = False
        self.moving_left = False

    #Função para ser colocado no while principal, para repetir o incremento/decremento enquanto o KEYUP = True, 
    #Executada quando a func check_events muda o valor das variaveis para o movimento continuo
    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        elif self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor
        self.rect.centerx = self.center
    # Função para desenhar a nave
    def blitme(self):
        self.screen.blit(self.image, self.rect)
    
    def center_ship(self):
        self.center = self.screen_rect.centerx
        




