import pygame
import random

pygame.init()
#размер экрана
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
#прописываем экран
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
#название заголовка
pygame.display.set_caption("игра ТИР")
#загружаем иконку
icon = pygame.image.load("img/2906.png")
pygame.display.set_icon(icon)
#  создаём мишень
target_image = pygame.image.load("img/1973")
#даём размер мишени
target_width = 80
target_height = 80
target_x = ()
# задаём рандомный цвет фона
color = (random.randint(0,255), random.randint(0,255), random.randint(0,255))

ruining = True
while_ruining :
    pass

pygame.quit()
