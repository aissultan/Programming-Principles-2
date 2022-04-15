import pygame
from random import randrange

size = width, height = 1050, 650
block = 25

x, y = randrange(0, width, block), randrange(0, height, block)
apple = randrange(0, width, block), randrange(0, height, block)
dirs = {'W': True, 'S': True, 'A': True, 'D': True}
length = 1
score = 0
level = 0
snake = [(x, y)]
dx, dy = 0, 0
fps = 10
walls = []

pygame.init()
screen = pygame.display.set_mode([width, height])
clock = pygame.time.Clock()
font_score = pygame.font.SysFont('Arial', 26, bold=True)
font_level = pygame.font.SysFont('Arial', 26, bold=True)
font_fps = pygame.font.SysFont('Arial', 26, bold=True)
font_end = pygame.font.SysFont('Arial', 66, bold=True)
font_menu = pygame.font.Font('Resources//font.ttf', 85)
game_background = pygame.image.load('Resources//game_background.jpg').convert()
menu_background = pygame.image.load('Resources//menu_background.jpg').convert()

pygame.mixer.music.load('Resources//menu_sound.mp3')
pygame.mixer.music.play()

def main_menu():
    menu = True
    while menu:
        screen.blit(menu_background, (0, 0))

        # menu text
        render_menu = font_menu.render('CLICK', True, pygame.Color('black'))
        screen.blit(render_menu, (430, 550))

        for event in pygame.event.get():
            mx, my = pygame.mouse.get_pos()

            if event.type == pygame.QUIT:
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN and 430 <= mx <= 550 and 570 <= my <= 600:
                menu = False

        pygame.display.flip()

        key = pygame.key.get_pressed()
        if key[pygame.K_RETURN]: # K_RETURN - нажатие на Enter
            break

main_menu()

while True:
    screen.blit(game_background, (0, 0))

    # drawing snake, apple, walls
    for i, j in snake:
        pygame.draw.rect(screen, pygame.Color('green'), (i, j, block - 1, block - 1))
    pygame.draw.rect(screen, pygame.Color('red'), (*apple, block, block))
    for i, j in walls:
        pygame.draw.rect(screen, pygame.Color('black'), (i, j, block - 1, block - 1))

    # show score, level and fps
    render_score = font_score.render(f'SCORE: {score}', True, pygame.Color('orange'))
    render_level = font_level.render(f'LEVEL: {level}', True, pygame.Color('orange'))
    render_fps = font_fps.render(f'FPS: {fps}', True, pygame.Color('orange'))
    screen.blit(render_score, (5, 5))    
    screen.blit(render_level, (5, 35))
    screen.blit(render_fps, (5, 65))

    # snake movement
    x += dx * block
    y += dy * block
    snake.append((x, y))
    snake = snake[-length:]

    # game over
    if x < 0 or x > width - block or y < 0 or y > height - block\
    or len(snake) > len(set(snake)) or snake in walls:
        while True:
            render_end = font_end.render('GAME OVER', True, pygame.Color('orange'))
            screen.blit(render_end, (335, 300))
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()

    # eating apple
    if snake[-1] == apple:
        while apple in snake or apple in walls:
            apple = randrange(0, width, block), randrange(0, height, block)
        length += 1
        score += 1
        pygame.mixer.music.load('Resources//score_sound.wav')
        pygame.mixer.music.play()
        if not score % 4:
            fps += 1
            level += 1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    pygame.display.flip()
    clock.tick(fps)

    # control
    key = pygame.key.get_pressed()
    if key[pygame.K_w] and dirs['W']:
        dx, dy = 0, -1
        dirs = {'W': True, 'S': False, 'A': True, 'D': True}
    if key[pygame.K_s] and dirs['S']:
        dx, dy = 0, 1
        dirs = {'W': False, 'S': True, 'A': True, 'D': True}
    if key[pygame.K_a] and dirs['A']:
        dx, dy = -1, 0
        dirs = {'W': True, 'S': True, 'A': True, 'D': False}
    if key[pygame.K_d] and dirs['D']:
        dx, dy = 1, 0
        dirs = {'W': True, 'S': True, 'A': False, 'D': True}