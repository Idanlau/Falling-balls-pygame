import pygame

import sys

from ball import Ball

from basket import Basket

from time import sleep




def check_events(basket,stats, play_button):

	for event in pygame.event.get():
		if event.type  == pygame.QUIT:
			sys.exit()
	
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_RIGHT:
				basket.moving_right = True

			if event.key == pygame.K_LEFT:
				basket.moving_left = True

		elif event.type == pygame.KEYUP:
			if event.key == pygame.K_RIGHT:
				basket.moving_right = False

			if event.key == pygame.K_LEFT:
				basket.moving_left = False

		elif event.type == pygame.MOUSEBUTTONDOWN:
			mouse_x, mouse_y = pygame.mouse.get_pos()
			check_play_button(stats, play_button, mouse_x, mouse_y)



def update_screen(ai_settings,screen,stats,sb,basket,balls,play_button):

	screen.fill(ai_settings.bg_color)
	balls.draw(screen)
	basket.blitme()

	if stats.game_stats == False:
		play_button.draw_button()
		stats.reset_stats()

	check_high_score(stats,sb,screen)

	sb.prep_level(stats)

	sb.high_score(stats,screen)





	sb.show_score()

	


	pygame.display.flip()




def update_ball(ai_settings,screen,basket,balls,stats,sb):

	ball = Ball(screen, ai_settings)

	balls.update(ai_settings,screen)

	check_ball_bottom(ai_settings,screen,basket,balls,stats,sb)

	create_ball(ai_settings,screen,balls)

	check_level_up(ai_settings,stats,sb)







def check_ball_bottom(ai_settings,screen,basket,balls,stats,sb):


	screen_rect = screen.get_rect()
	for ball in balls.sprites():
		if ball.rect.bottom >= screen_rect.bottom:
			balls.remove(ball)
			ai_settings.ball_failed -= 1
			check_ball_failed(ai_settings,screen,basket,balls,stats,sb)
		if pygame.sprite.spritecollideany(basket, balls):
			balls.remove(ball)
			stats.score += ai_settings.points
			sb.prep_score()
			ai_settings.check_ball_caught += 1
		if ai_settings.check_ball_caught == 3:
			ai_settings.next_level = True
			ai_settings.check_ball_caught = 0




def create_ball(ai_settings, screen, balls):

	ball = Ball(screen, ai_settings)
	 

	if len(balls) < 1:
		ball = Ball(screen, ai_settings)
		balls.add(ball)


def check_ball_failed(ai_settings,screen,basket,balls, stats,sb):

	balls.empty()
	sleep(0.5)
	update_ball(ai_settings, screen, basket, balls, stats,sb)

	
	if ai_settings.ball_failed == 0:

		stats.game_stats = False
		stats.score = 0
		sb.prep_score()


def check_play_button(stats, play_button, mouse_x, mouse_y):
	#starts a new game when the player plays
	if play_button.rect.collidepoint(mouse_x, mouse_y):
		stats.game_stats = True
		stats.reset_stats()

def check_level_up(ai_settings,stats,sb):
	if ai_settings.next_level == True:
		ai_settings.ball_drop_speed *= ai_settings.speedup_scale
		ai_settings.basket_speed *= ai_settings.speedup_scale
		stats.level += 1
		sb.prep_level(stats)
		ai_settings.next_level = False

def check_high_score(stats,sb,screen):

	if stats.score > stats.highscore:
		stats.highscore = stats.score
		sb.high_score(stats,screen)


