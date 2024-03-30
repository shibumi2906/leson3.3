import pygame
import random
import sys

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Игра Тир")
icon = pygame.image.load("img/2906.png")
pygame.display.set_icon(icon)
target_img = pygame.image.load("img/1980.png")

def draw_text(surface, text, size, x, y):
    font = pygame.font.Font(None, size)
    text_surface = font.render(text, True, (255, 255, 255))
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surface.blit(text_surface, text_rect)

input_time = ""
instruction = "Введите время в секундах, на которое мишень будет оставаться на месте, и нажмите Enter:"
time_entered = False

while not time_entered:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN and input_time:
                time_entered = True
            elif event.key == pygame.K_BACKSPACE:
                input_time = input_time[:-1]
            else:
                input_time += event.unicode
    screen.fill((0, 0, 0))
    draw_text(screen, instruction, 36, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 4)
    draw_text(screen, input_time, 36, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    pygame.display.flip()

try:
    stay_time = float(input_time)
except ValueError:
    stay_time = 5

target_visible = True
target_x = random.randint(0, SCREEN_WIDTH - target_img.get_width())
target_y = random.randint(0, SCREEN_HEIGHT - target_img.get_height())
hits = 0
time_target_appeared = pygame.time.get_ticks() / 1000.0

running = True
while running:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and target_visible:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if target_x <= mouse_x <= target_x + target_img.get_width() and target_y <= mouse_y <= target_y + target_img.get_height():
                hits += 1
                target_visible = False
    current_time = pygame.time.get_ticks() / 1000.0
    if not target_visible or current_time - time_target_appeared >= stay_time:
        target_x = random.randint(0, SCREEN_WIDTH - target_img.get_width())
        target_y = random.randint(0, SCREEN_HEIGHT - target_img.get_height())
        target_visible = True
        time_target_appeared = current_time
    if target_visible:
        screen.blit(target_img, (target_x, target_y))
    draw_text(screen, f"Попаданий: {hits}", 30, 100, 10)
    pygame.display.flip()

pygame.quit()








