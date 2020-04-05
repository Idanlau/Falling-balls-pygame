import pygame

from pygame.sprite import Sprite

class Basket(Sprite):

	def __init__(self, screen):

		super(Basket,self).__init__()

		#initialize the basker and set its starting position
		self.screen = screen

		#Load the basket and get its rect
		self.image = pygame.image.load('images/basket.png')
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()


		#start the basket at the bottom center of the screen.
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom

		self.moving_left = False
		self.moving_right = False

		

	def blitme(self):
		#Draw teh ship at its current location
		self.screen.blit(self.image, self.rect)

	def basket_movements(self,ai_settings):
		if self.moving_right and self.rect.right < 1200:
			self.rect.centerx += ai_settings.basket_speed
		
		if self.moving_left and self.rect.left > 0:
			self.rect.centerx -= ai_settings.basket_speed
			