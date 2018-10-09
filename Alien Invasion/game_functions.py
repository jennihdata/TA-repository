import sys
from time import sleep
import pygame
from bullet import Bullet
from evilminion import Evilminion
import math

def check_keydown_events(event, ai_settings,screen, minion, bullets):
    if event.key == pygame.K_RIGHT:
        minion.moving_right = True
    elif event.key == pygame.K_LEFT:
        minion.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, minion, bullets)
    elif event.key == pygame.K_q:
        sys.exit()

def fire_bullet(ai_settings, screen, minion, bullets):
        if len(bullets) < ai_settings.bullets_allowed:
            new_bullet = Bullet(ai_settings, screen, minion)
            bullets.add(new_bullet)

def check_keyup_events(event, minion):
    if event.key == pygame.K_RIGHT:
        minion.moving_right = False
    elif event.key == pygame.K_LEFT:
        minion.moving_left = False

def check_events(ai_settings, screen, minion, bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings,screen, minion, bullets)

        elif event.type == pygame.KEYUP:
            check_keyup_events(event, minion)


def update_screen(ai_settings, screen, minion, evilminions, bullets):
    screen.fill(ai_settings.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    minion.blitme()

    evilminions.draw(screen)
    pygame.display.flip()

def update_bullets(ai_settings, screen, minion, evilminions, bullets):
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

    check_bullet_evilminion_collisions(ai_settings, screen , minion, evilminions, bullets)

def check_bullet_evilminion_collisions(ai_settings, screen, minion, evilminions, bullets):
    collisions = pygame.sprite.groupcollide(bullets, evilminions, True, True)

    if len(evilminions) == 0:
        bullets.empty()
        create_fleet(ai_settings, screen, minion, evilminions)


def get_number_evilminions_x(ai_settings, evilminion_width):
    available_space_x = ai_settings.screen_width - 2 * evilminion_width
    number_evilminions_x = int(available_space_x / (2*evilminion_width))
    return number_evilminions_x

def get_number_rows(ai_settings, minion_height, evilminion_height):
    available_space_y = (ai_settings.screen_height - (3 * evilminion_height) - minion_height)
    #math.ceil function is to round up the number of rows(0.87979 = 1)
    number_rows = int(math.ceil(available_space_y / (2 * evilminion_height)))
    return number_rows

def create_evilminion(ai_settings, screen, evilminions, evilminion_number, row_number):
    evilminion = Evilminion(ai_settings, screen)
    evilminion_width = evilminion.rect.width
    evilminion.x = evilminion_width + 2 * evilminion_width * evilminion_number
    evilminion.rect.x = evilminion.x
    evilminion.rect.y = evilminion.rect.height + 2 * evilminion.rect.height * row_number
    evilminions.add(evilminion)

def create_fleet(ai_settings, screen, minion, evilminions):
    evilminion = Evilminion(ai_settings, screen)
    evilminion_width = evilminion.rect.width
    available_space_x = ai_settings.screen_width - 2 * evilminion_width
    # number_evilminions_x = int(available_space_x / (2 * evilminion_width))
    number_evilminions_X = get_number_evilminions_x(ai_settings, evilminion.rect.width)
    number_rows = get_number_rows(ai_settings, minion.rect.height, evilminion.rect.height)


    for row_number in range(number_rows):
        for evilminion_number in range(number_evilminions_X):
            create_evilminion(ai_settings, screen, evilminions, evilminion_number, row_number)
            evilminion = Evilminion(ai_settings, screen)
            evilminion.x = evilminion_width + 2 * evilminion_width * evilminion_number
            evilminion.rect.x = evilminion.x
            evilminions.add(evilminion)

def minion_hit(ai_settings, stats, screen, minion, evilminions, bullets):
    if stats.minions_left > 0:
        stats.minions_left -= 1
        evilminions.empty()
        bullets.empty()
        create_fleet(ai_settings, screen, minion, evilminions)
        minion.center_minion()
        sleep(0.5)

    else:
        stats.game_active = False

def check_evilminions_bottom(ai_settings, stats, screen, minion, evilminions, bullets):
    screen_rect = screen.get_rect()
    for evilminion in evilminions.sprites():
        if evilminion.rect.bottom >= screen_rect.bottom:
            minion_hit(ai_settings, stats, screen, minion, evilminions, bullets)
            break

def update_evilminions(ai_settings, stats, screen, minion, evilminions, bullets):
    check_fleet_edges(ai_settings, evilminions)
    evilminions.update()
    check_evilminions_bottom(ai_settings, stats, screen, minion, evilminions, bullets)

    if pygame.sprite.spritecollideany(minion, evilminions):
        minion_hit(ai_settings, stats, screen, minion, evilminions, bullets)
        print("Evil Minion hit!!!")

def check_fleet_edges(ai_settings, evilminions):
    for evilminion in evilminions.sprites():
        if evilminion.check_edges():
            change_fleet_direction(ai_settings, evilminions)
        break

def change_fleet_direction(ai_settings, evilminions):
    for evilminion in evilminions.sprites():
        evilminion.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1





