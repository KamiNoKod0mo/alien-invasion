# Classe para guardas configurações
class Settings():
    def __init__(self):
        
        # Config janela
        self.screen_width = 1200
        self.screen_height = 700
        self.bg_color = (230, 230, 230)

        # config nave
        
        self.ship_limit = 3
        
        # Configurações do tiro
        
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3

        # Confidurações do inimigo
        
        self.fleet_drop_speed = 10
        
        # configura de taxa de aumento de velecidade e pontos
        self.speedup_scale = 1.1
        self.score_scale = 1.5

        # seta os valores inicias
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        self.ship_speed_factor = 1.5 
        self.bullet_speed_factor = 3

        self.alien_speed_factor = 1
        self.fleet_direction = 1

        self.alien_points = 50
    # aumenta a dificuldade ,multiplicando pela taxa de aumento
    def increase_speed(self): 
        self.ship_speed_factor *= self.speedup_scale 
        self.bullet_speed_factor*= self.speedup_scale 
        self.alien_speed_factor *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)



