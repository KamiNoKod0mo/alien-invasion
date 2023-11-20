import pygame, game_function
from settings import Settings
from ship import Ship
from pygame.sprite import Group
#from aliens import Alien
from game_stats import GameStats
from button import button
from scoreboard import Scoreboard

def run_game():
# Inicializa o jogo e cria um objeto para a tela, objeto nave
    pygame.init()
    ai_settings = Settings() 
    screen =pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Butão de Play, status, ship
    play_button = button(ai_settings, screen,"Play")
    
    stats = GameStats(ai_settings) 
    ship = Ship(ai_settings, screen)
    # Grupos para receber mais de 1 sprite
    bullets = Group()
    aliens = Group()
    sb = Scoreboard(ai_settings,screen, stats)

    #Função para criar as naves em linhas no arquivo g_f.py
    game_function.create_fleet(ai_settings, screen,ship,aliens)
    sb.prep_ships()
# Inicia o laço principal do jogo 
    while True:
        # Game function
        #checar eventos
        game_function.check_events(ai_settings,screen, stats, sb, play_button, ship, aliens, bullets)
        # Apaga os tiros
        game_function.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
        # Carrega o visual
        game_function.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets,play_button)
        # Carregar a nave e tiro e aliens
        if stats.game_active == True:
            ship.update()
            bullets.update() 
            game_function.update_aliens(ai_settings,screen, stats, sb, ship, aliens, bullets)
        
# Chamada da função
run_game()
