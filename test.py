import pygame
import random

pygame.init()
# Размер экрана
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
# Создаем экран
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
# Название заголовка
pygame.display.set_caption("Игра Тир")
# Загружаем иконку
icon = pygame.image.load("img/2906.png")
pygame.display.set_icon(icon)
# Создаем мишень
target_img = pygame.image.load("img/1980.png")
# Размеры мишени
target_width = 80
target_height = 80
# Рандомные координаты мишени
target_x = random.randint(0, SCREEN_WIDTH - target_width)
target_y = random.randint(0, SCREEN_HEIGHT - target_height)
# Рандомный цвет фона
color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

running = True
# Игровой цикл
while running:
    screen.fill(color)  # Заливка рандомным цветом

    for event in pygame.event.get():  # Обработка событий
        if event.type == pygame.QUIT:  # Условия завершения игры
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:  # Если кнопка мыши нажата
            mouse_x, mouse_y = pygame.mouse.get_pos()  # Определение позиции курсора
            # Условие попадания в мишень
            if target_x < mouse_x < target_x + target_width and target_y < mouse_y < target_y + target_height:
                target_x = random.randint(0, SCREEN_WIDTH - target_width)
                target_y = random.randint(0, SCREEN_HEIGHT - target_height)

    screen.blit(target_img, (target_x, target_y))  # Отрисовка мишени
    pygame.display.update()  # Обновление экрана

pygame.quit()  # Завершение работы Pygame
