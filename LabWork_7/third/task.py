import pygame

# Initialize all configs
pygame.init()

# Creating main window
width, length = 600, 600
screen = pygame.display.set_mode((width, length))
running = True

WHITE = (255, 255, 255)
RED = (255, 0, 0)
radius = 25
x, y = 300, 300
FPS = 60
clock = pygame.time.Clock()
# Main loop
while running:
    # Getting all the events from OS
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # Game logic
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP]: y -= 20
    if pressed[pygame.K_DOWN]: y += 20
    if pressed[pygame.K_LEFT]: x -= 20
    if pressed[pygame.K_RIGHT]: x += 20
    if x > 580: x -= 20
    if y > 580: y -= 20
    if x < 20: x += 20
    if y < 20: y += 20

    screen.fill(WHITE)
    pygame.draw.circle(screen, RED, (x, y), radius)
    # Screen updating
    pygame.display.flip()
    clock.tick(FPS)