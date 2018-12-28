import pygame
class Ship():
    def __init__(self,screen):
        #设置在屏幕的初始位置
        self.screen=screen
        #加载飞船图像
        self.image=pygame.image.load('images/ship.bmp')
        self.rect=self.image.get_rect()
        self.screen_rect=screen.get_rect()
        #将每艘新的飞船放在屏幕底部
        self.rect.centerx=self.screen_rect.centerx
        self.rect.bottom=self.screen_rect.bottom
        self.moving_right=False
        self.moving_left=False
    def blitme(self):
        """指定位置绘制飞船"""
        self.screen.blit(self.image,self.rect)
    def update(self):
        if self.moving_right:
            self.rect.centerx+=1
        if self.moving_left:
            self.rect.centerx-=1
