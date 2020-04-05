import pygame.font

from basket import Basket

from pygame.sprite import Group


class Scoreboard():
	# A class to report scoring info

	def __init__(self, ai_settings, screen, stats):
		#Initialize scorekeeping attributes
		self.screen = screen
		self.screen_rect = screen.get_rect()
		self.ai_settings = ai_settings
		self.stats = stats

		#font settings for scoring info
		self.text_color = (30,30,30)
		self.font = pygame.font.SysFont(None, 48)

		#prepare the initial score image
		self.prep_score()
		self.prep_level(stats)


	def prep_score(self):
		#Turn the score into a rendered image
		score_str = str(self.stats.score)
		self.score_image = self.font.render(score_str, True, self.text_color, self.ai_settings.bg_color)

		#display the score at the top right of the screen
		self.score_rect = self.score_image.get_rect()
		self.score_rect.right = self.screen_rect.right - 20
		self.score_rect.top = 20



	def prep_level(self,stats):
		self.level_image = self.font.render(str(self.stats.level), True, self.text_color, self.ai_settings.bg_color)

		self.level_rect = self.level_image.get_rect()
		self.level_rect.right = self.score_rect.right
		self.level_rect.top = self.score_rect.bottom + 10

	def high_score(self,stats,screen):
		self.highscore_image = self.font.render(str(self.stats.highscore), True, self.text_color, self.ai_settings.bg_color)

		self.highscore_rect= self.highscore_image.get_rect()
		self.highscore_rect.center = self.screen_rect.center
		self.highscore_rect.top = self.screen_rect.top + 10

	def show_score(self):
		#Draw score to the screen
		self.screen.blit(self.score_image,self.score_rect)
		self.screen.blit(self.level_image,self.level_rect)
		self.screen.blit(self.highscore_image,self.highscore_rect)
