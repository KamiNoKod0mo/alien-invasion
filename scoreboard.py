import pygame.font
from pygame.sprite import Group
from ship import Ship
# Faz o placar
class Scoreboard():
    def __init__(self, ai_settings, screen, stats):
        self.screen = screen 
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings 
        self.stats = stats
        self.text_color = (30, 30, 30)  
        self.font = pygame.font.SysFont(None,48)
        #Placar de ponto
        self.prep_score()
        #Placa de maior ponto
        self.prep_high_score()
        # Placar de level
        self.prep_level()
        # Placar de naves
        self.prep_ships()

    # arrendonda, renderiza e colocar na superior direita, score
    def prep_score(self):
        rounded_score = int(round(self.stats.score, -1))
        score_str = "{:,}".format(rounded_score)
        self.score_image = self.font.render(score_str, True, self.text_color,self.ai_settings.bg_color)
        self.score_rect = self.score_image.get_rect()
        
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20
    
    ## Arquivo game_stats
    # Arrendonda renderica o high_score
    def prep_high_score(self):
        high_score = int(round(self.stats.high_score, -1)) 
        high_score_str = "{:,}".format(high_score)
        self.high_score_image = self.font.render(high_score_str, True, self.text_color,self.ai_settings.bg_color)
        # Centraliza a pontuação máxima na parte superior da tela
        self.high_score_rect = self.high_score_image.get_rect()

        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top

    # Pegal o level, renderica o bota em posição
    def prep_level(self):
        self.level_image = self.font.render(str(self.stats.level), True,self.text_color, self.ai_settings.bg_color)
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right =self.score_rect.right
        self.level_rect.top = self.score_rect.bottom +10

    # Pega quantas ships faltam desenha em bota em grupo (ships)
    # Redezenha toda fez que é chamado, assim não preciso excluir
    def prep_ships(self):
        self.ships = Group()
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.ai_settings, self.screen)
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)

    # Desenhas os Placares
    def show_score(self):
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)

        self.ships.draw(self.screen)



