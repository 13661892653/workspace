#coding=utf-8
import pygame,sys
from pygame.locals import *

#坦克大战的主窗口
class TankMain():
    #开始游戏的方法
    def startGame(self):
        pygame.init()#pygame模块初始化，加载系统资源
        #设置一个窗口屏幕
        #第一个参数是宽高的元组，第二个参数是窗口的特性（可变的，0代表不可变，
        # resizable表示可变大小，FULLSCREEN代表全屏
        # 第三个参数表示使用颜色的位数，32代表32位）
        screen = pygame.display.set_mode((600,500),0,32)
        #给窗口设置一个标题
        pygame.display.set_caption("坦克大战")

        while True:
            #填充颜色RGB（红，绿，蓝），000是黑色，三个255是白色
            screen.fill((0,0,0))
            #显示左上角的文字
            screen.blit(self.write_text(),(0,5))
            #窗口显示重置
            pygame.display.update()

    #结束游戏的方法
    def stopGame(self):
        sys.exit()

    #在屏幕的左上角显示文字
    def write_text(self):
        #定义一个字体
        font = pygame.font.SysFont("simsunextb",10)
        #根据字体创一个文字图像并返回
        text_sf = font.render("敌方坦克数量为：5",True,(255,0,0))
        return text_sf

game = TankMain()
game.startGame()