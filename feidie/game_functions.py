import sys
import pygame
"""响应键盘事件"""
def check_events(ship):
    for event in pygame.event.get():
        if(event.type==pygame.QUIT):
            sys.exit()
        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_RIGHT:
                ship.moving_right=True
            if event.key==pygame.K_LEFT:
                ship.moving_left=True
        elif event.type==pygame.KEYUP:
            if event.key==pygame.K_RIGHT:
                ship.moving_right=False
            if event.key==pygame.K_LEFT:
                ship.moving_left=False
        
def update_screen(et_settings,screen,ship):
    """更新图像"""
    screen.fill(et_settings.bg_color)
    ship.blitme()
    pygame.display.flip()