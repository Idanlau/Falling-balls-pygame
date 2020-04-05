import pygame

from pygame.sprite import Sprite

import random

class Ball(Sprite):
	# A class to manage balls

	def __init__(self, screen, ai_settings):

		super(Ball,self).__init__()
		#initialize the ball and set its starting position
		self.screen = screen
		self.ai_settings = ai_settings

		#Load the ball and get its rect
		self.image = pygame.image.load('images/ball.png')
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()
		ball_width = self.image.get_width()


		
		self.rect.x = random.randrange(0, ai_settings.screen_width - ball_width)
		self.rect.y = self.rect.height
		self.x = float(self.rect.x)
		self.y = float(self.rect.y)


		

		
		


			
	def blitme(self):

		#Draw ball at its current location
		self.screen.blit(self.image, self.rect)

	def update(self, ai_settings, screen):

		self.rect.y = self.y
		self.y += ai_settings.ball_drop_speed
		self.screen = screen








