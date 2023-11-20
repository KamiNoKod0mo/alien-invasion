# Inicio e recomeço, status do jogo
class GameStats():    
    def __init__(self, ai_settings):
        #instancia
        self.ai_settings = ai_settings 
        self.reset_stats()
        # maior valor não pode resetar
        self.high_score = 0
        
        # Flag de ativação
        self.game_active = False
    # setas vidas, score, level para o inicial
    def reset_stats(self):
        self.ships_left = self.ai_settings.ship_limit 
        self.score = 0
        self.level = 1

