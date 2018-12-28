import pygame
import game_functions
from settings import settings
from ship import Ship
def run_game():
    #初始化游戏设置标题和屏幕
    pygame.init()
    et_settings=settings()
    screen=pygame.display.set_mode((et_settings.screen_width,et_settings.screen_height))
    bg_color=et_settings.bg_color
    pygame.display.set_caption("Alien Invasion_Author:QQ 1149809644")

    #创建一个飞船
    ship=Ship(screen)
    while True:
        #循环监听键盘和鼠标事件
        game_functions.check_events(ship)
        ship.update()
        game_functions.update_screen(et_settings,screen,ship)
run_game()