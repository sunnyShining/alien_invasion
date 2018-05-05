import sys
import pygame
from settings import Setting
from ship import Ship
import game_functions as gf
from pygame.sprite import Group

def run_game():
	# 初始化游戏并创建一个屏幕对象
	pygame.init()
	ai_setting = Setting()
	screen = pygame.display.set_mode((ai_setting.screen_width, ai_setting.screen_height))
	pygame.display.set_caption("Alien Invesion")
	# 创建一艘飞船
	ship = Ship(ai_setting, screen)
	# 创建一个用于存储子弹的编组
	bullets = Group()
	# 开始游戏主循环
	while True:
		gf.check_events(ai_setting, screen, ship, bullets)
		ship.update()
		gf.update_bullets(bullets)
		gf.update_screen(ai_setting, screen, ship, bullets)
		# 让最近绘制的屏幕可见
		pygame.display.flip()
run_game()