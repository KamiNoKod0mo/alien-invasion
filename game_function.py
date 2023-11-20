import pygame,sys
from bullet import Bullet
from alien import Alien
from time import sleep

# Pega os eventos do teclado
def check_events(ai_settings,screen, stats, sb, play_button, ship, aliens, bullets):
    for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                sys.exit()
            # Se uma tacla key foi precionada
            elif event.type == pygame.KEYDOWN:
                check_keydown_events(event,ai_settings, screen, ship, bullets) 

            # Se uma tacla key foi solta  
            elif event.type == pygame.KEYUP:
                check_keyup_events(event,ship)
            # se o botão play foi iniciado
            elif event.type == pygame.MOUSEBUTTONDOWN: 
                mouse_x, mouse_y = pygame.mouse.get_pos()
                check_play_button(ai_settings, screen, stats, sb, play_button, ship,aliens, bullets, mouse_x, mouse_y)
                

#  Faz o update da tela, para aparecer as coisas
def update_screen(ai_settings, screen, stats, sb, ship,aliens, bullets, play_button): 
    screen.fill(ai_settings.bg_color)
    # Desenhar os tiros da lista que foi pasado pro argumento.
    for bullet in bullets.sprites(): 
        bullet.draw_bullet() 
    ship.blitme()
    # DEsenhas todo os sprites de aliens ,pontuação e botão de play
    aliens.draw(screen)
    sb.show_score()
    if not stats.game_active: 
        play_button.draw_button()
    pygame.display.flip() #Deixa a tela mais recente visível

def check_keydown_events(event, ai_settings, screen, ship, bullets):
# Se foi a direita, Incrementa a variavel rect.centerx, e seta como True a varia moving_right no arquivo ship.py
    if event.key == pygame.K_RIGHT: 
        ship.rect.centerx += 1
        ship.moving_right = True

    # Se foi a esquerda, decrementa a variravel rect.centerx, e seta como True a varia moving_left no arquivo ship.py
    elif event.key == pygame.K_LEFT: 
        ship.rect.centerx -= 1
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen,ship, bullets)
        

def check_keyup_events(event, ship):
# Se foi a direita, e seta como False a varia moving_right no arquivo ship.py, quando for solta
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    # Se foi a esquerda, e seta como False a varia moving_left no arquivo ship.py, quando for solta
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets):
    # Apaga os tiros
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0: 
            bullets.remove(bullet)
    check_bullet_alien_collisions(ai_settings, screen, stats, sb, ship,aliens, bullets)

# Função que atira os bullet.py
def fire_bullet(ai_settings, screen, ship, bullets):
    if len(bullets) < ai_settings.bullets_allowed:
            new_bullet = Bullet(ai_settings, screen, ship)
            bullets.add(new_bullet)

#Função para criar as naves em linhas
def create_fleet(ai_settings, screen, ship,aliens):
    alien = Alien(ai_settings, screen)
    
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings, ship.rect.height,alien.rect.height)
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings, screen, aliens,alien_number,row_number)


#Determina o número de alienígenas que cabem em uma linha X
def get_number_aliens_x(ai_settings,alien_width):
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x

#Determina o número de alienígenas que cabem em uma linha Y
def get_number_rows(ai_settings, ship_height, alien_height):
    available_space_y = (ai_settings.screen_height -(3 * alien_height) - ship_height) 
    number_rows = int(available_space_y /(2 * alien_height)) 
    return number_rows

#cria uma frota completa de alienígenas
def create_alien(ai_settings, screen, aliens, alien_number,row_number):
    alien = Alien(ai_settings, screen) 
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number 
    alien.rect.x = alien.x 

    alien.rect.y = alien.rect.height + 2 * alien.rect.height *row_number
    
    aliens.add(alien)

# Para chamar as funções, checa borda muda direção e update a coordenada
def update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets):
    check_aliens_bottom(ai_settings, screen, stats, sb, ship, aliens,bullets)
    check_fleet_edges(ai_settings, aliens)
    aliens.update()
    if pygame.sprite.spritecollideany(ship, aliens): 
        ship_hit(ai_settings,screen, stats, sb, ship, aliens, bullets)
    

# Pega a cordenada de cada spritesm verifica se atingiu a bordar, e chama função
def check_fleet_edges(ai_settings, aliens):
    for alien in aliens.sprites(): 
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens) 
            break
# Função para mudar de direção para baixo e pro lados
def change_fleet_direction(ai_settings, aliens): 
    for alien in aliens.sprites(): 
        alien.rect.y += ai_settings.fleet_drop_speed 
    ai_settings.fleet_direction *= -1
        
# Checar a colisões dos aliens com as balas, e carregar mais
def check_bullet_alien_collisions(ai_settings, screen, stats, sb, ship, aliens,bullets):
    # guada a bullet(key) e quantos alien(value) pegou
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    if collisions:
        #corre o dict
        for aliens in collisions.values():
            #multiplica o numero de aliens atingidos pelos pontos que cada um vale
            stats.score += ai_settings.alien_points * len(aliens)
        # Atualiza o score com base na stats.score
        sb.prep_score()
        #checar que o novo valor e maior que o antigo maior valor
        check_high_score(stats, sb)
        
    # Quando o grupo aliens acabar
    if len(aliens) == 0:
        # limpa
        bullets.empty()
        # aumenta dificuldade em setting e cria frota
        ai_settings.increase_speed()
        create_fleet(ai_settings, screen, ship, aliens)
        # Aumenta um level e renderica ele
        stats.level += 1
        sb.prep_level()

# Função para verificar a colisão das naves com os aliens, sndo chamada em update_aliens
def ship_hit(ai_settings, screen, stats, sb, ship, aliens, bullets):
    if stats.ships_left > 0:#settings
        #diminui um vida
        stats.ships_left -= 1
        # chama para ler ships_left e desenhar navinhas de acordo com a mesma
        sb.prep_ships()
        
    # Variavel que permite a execução do jogo, deixar o mouse visivel
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)
    # Limpa os aliens, balas, criar frota e centraliza ship
    aliens.empty()
    bullets.empty()
    create_fleet(ai_settings, screen, ship, aliens) 
    ship.center_ship()
    sleep(0.5)
# Função para verificar se os alien cheram na borda de baixo usando ship_hit
def check_aliens_bottom(ai_settings, screen, stats, sb, ship, aliens,bullets):
    screen_rect = screen.get_rect() 
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(ai_settings, screen, stats, sb, ship, aliens, bullets)
            break
# Verifica se o botão de play foi clicado e game_active == false
def check_play_button(ai_settings, screen, stats, sb, play_button, ship,aliens, bullets, mouse_x, mouse_y):
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y) 
    if button_clicked and not stats.game_active:
        #curso do mouse invisivel
        pygame.mouse.set_visible(False)
        # reseta tudo
        stats.reset_stats()
        aliens.empty()
        bullets.empty()
        #cria nova tropa
        create_fleet(ai_settings, screen, ship, aliens) 
        # centraliza ship
        ship.center_ship()
        stats.game_active = True
        ai_settings.initialize_dynamic_settings()
        sb.prep_score()
        sb.prep_high_score()
        sb.prep_level()
        sb.prep_ships()

# Checar os valores de score e high_score
def check_high_score(stats, sb):
        if stats.score > stats.high_score: 
            stats.high_score = stats.score
            sb.prep_high_score()