class GameStats():

	def __init__(self, ai_settings):
		self.ai_settings = ai_settings
		self.game_stats = False
		self.score = 0
		self.level = 1
		self.highscore = 0

	def reset_stats(self):
		self.ai_settings.ball_failed = 3
		self.ai_settings.check_ball_caught = 0
		self.ai_settings.ball_drop_speed = 30
		self.level = 1