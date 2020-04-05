import sys

import pygame

from settings import Settings

import game_function as gf

from basket import Basket

from ball import Ball

from pygame.sprite import Group

from game_stats import GameStats

from play_button import Button

from scoreboard import Scoreboard

def run_game():
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
	pygame.display.set_caption("catchtheball")
	basket = Basket(screen)
	balls = Group()
	stats = GameStats(ai_settings)
	play_button = Button(ai_settings, screen, "Play")
	sb = Scoreboard(ai_settings, screen, stats)


	
	while True:

		gf.check_events(basket,stats, play_button)


		

		if stats.game_stats:
			basket.basket_movements(ai_settings)
			gf.update_ball(ai_settings,screen,basket,balls,stats,sb)
		gf.update_screen(ai_settings,screen,stats,sb,basket,balls,play_button)





run_game()
