import sys
import pygame

from pygame.sprite import Group
from settings import Settings
from game_stats import Gamestats
from scoreboard import Scoreboard
from button import Button
from minion import Minion
from evilminion import Evilminion

import game_functions as gf

def run_game():

    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Minion Invasion")

    play_button = Button(ai_settings, screen, "Play")
    stats = Gamestats(ai_settings)
    sb = Scoreboard(ai_settings, screen , stats)
    minion = Minion(ai_settings, screen)
    evilminion = Evilminion(ai_settings, screen)
    bullets = Group()
    evilminions = Group()
    gf.create_fleet(ai_settings, screen, minion, evilminions)
    bg_color = (148, 227, 246)
    pygame.mixer.music.load("images/minionsmarch.mp3")
    pygame.mixer.music.play(-1,0.0)

    while True:
        gf.check_events(ai_settings,screen,stats, sb, play_button, minion, evilminions, bullets)
        if stats.game_active:
            minion.update()
            gf.update_bullets(ai_settings, screen, stats, sb, minion, evilminions, bullets)
            gf.update_evilminions(ai_settings,screen, stats, sb, minion, evilminions, bullets)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        gf.update_screen(ai_settings, screen, stats, sb, minion, evilminions, bullets, play_button)


run_game()

