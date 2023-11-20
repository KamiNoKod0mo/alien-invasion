#sprites, podemos agrupar elementos relacionados no jogo e atuar em todos os elementos agrupados de uma só vez.
from pygame.sprite import Sprite
import pygame

#Setar as caracteristicas do Bullet
class Bullet(Sprite):
    def __init__(self, ai_settings, screen, ship):
        # herdar atributos do Sprite
        super().__init__() 
        self.screen = screen
        self.rect = pygame.Rect(0, 0,ai_settings.bullet_width, ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        self.y = float(self.rect.y)
        self.color = ai_settings.bullet_color 
        self.speed_factor = ai_settings.bullet_speed_factor

    # Movimento do tiro que tem que ser atualizado
    def update(self):
        self.y -= self.speed_factor
        self.rect.y = self.y

    # Desenhar o tiro
    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)