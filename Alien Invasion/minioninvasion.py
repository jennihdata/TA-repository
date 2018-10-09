import sys
import pygame

from pygame.sprite import Group
from settings import Settings
from minion import Minion
import game_functions as gf

def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Minion Invasion")
    minion = Minion(ai_settings, screen)
    bullets = Group()
    bg_color = (148, 227, 246)

    while True:
        gf.check_events(ai_settings,screen, minion, bullets)
        minion.update ()
        gf.update_bullets(bullets)
        gf.update_screen(ai_settings,screen, minion, bullets)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        screen.fill(ai_settings.bg_color)
        minion.blitme()
        pygame.display.flip()

run_game()

