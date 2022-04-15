import random, sys, pygame, time
pygame.init()
FPS = 60

# размеры окна 
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
 
STEP = 5 # шаг игрока 
ENEMTY_STEP = 10 # шаг врага 

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

SCORE  = 0 # cчетсчик для машин
NUM_OF_COINS = 0 # cчетсчик очков 

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # установление экрана
pygame.display.set_caption("Aisultan's racer game") # название экрана

clock = pygame.time.Clock()

# шрифты и тексты
score_font = pygame.font.SysFont("Verdana", 20) # шрифт для счетчиков
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)

background = pygame.image.load("Resources//AnimatedStreet.png") # фон игры

# фоновая музыка игры (можно поставить на паузу)
pygame.mixer.music.load('Resources//tokyo drift.mp3')
pygame.mixer.music.play(-1)

# класс врага
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Resources//Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0) 

    def update(self):
        global SCORE
        self.rect.move_ip(0, ENEMTY_STEP)
        if(self.rect.bottom > SCREEN_HEIGHT):
            SCORE += 1 # если энеми проехал всю высоту экрана, это плюс к скору
            self.top = 0
            self.rect.center = (random.randint(30, 350), 0)

    def draw(self, screenace):
        screenace.blit(self.image, self.rect)

# класс игрока
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Resources//Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)

    def update(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 0:
            if pressed_keys[pygame.K_LEFT]:
                self.rect.move_ip(-STEP, 0)

        if self.rect.right < SCREEN_WIDTH:
            if pressed_keys[pygame.K_RIGHT]:
                self.rect.move_ip(STEP, 0)

    def draw(self, screenace):
        screenace.blit(self.image, self.rect)

# класс монеты 
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('Resources//Coin.png')
        self.image = pygame.transform.scale(self.image,(25,25))
        self.rect=self.image.get_rect()
        self.rect.center = (random.randint(40,SCREEN_WIDTH-40),0)

    def update(self):
        self.rect.move_ip(0, 5)
        if(self.rect.bottom > SCREEN_HEIGHT):
            self.top = 0
            self.rect.center = (random.randint(30, 350), 0)

    def spawn(self):
        self.rect.center = (random.randint(30, 350), 0)

    def draw(self,screenace):
        screenace.blit(self.image,self.rect)

# создание Sprite groups
P1 = Player()
E1 = Enemy()
C1 = Coin()
enemies = pygame.sprite.Group()
enemies.add(E1)
coins = pygame.sprite.Group()
coins.add(C1)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
all_sprites.add(C1)

# основной цикл 
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                pygame.mixer_music.pause()
            if event.key == pygame.K_w:
                pygame.mixer_music.unpause()

    P1.update()
    E1.update()
    C1.update()

    if pygame.sprite.spritecollideany(P1, coins):
        NUM_OF_COINS += 1
        pygame.mixer.Sound('Resources//coin.wav').play()
        if NUM_OF_COINS % 15 == 0:
            ENEMTY_STEP += 1
        C1.spawn() # как только игрок тронул монету, нужно создать новую

    if pygame.sprite.spritecollideany(P1, enemies):
        pygame.mixer.Sound('Resources//crash.wav').play()
        time.sleep(0.5)
                
        screen.fill(RED)
        screen.blit(game_over, (30, 250))

        pygame.display.update()
        for entity in all_sprites:
            entity.kill()
        time.sleep(2)
        pygame.quit()
        sys.exit()      

    screen.blit(background, (0, 0))
    score_img = score_font.render('Number of passing cars: ' + str(SCORE), True, BLACK)
    coin_score_img = score_font.render('Number of collected coins: '+ str(NUM_OF_COINS), True, BLACK)
    speed_img = score_font.render('Speed of enemy: ' + str(ENEMTY_STEP), True, BLACK)
    screen.blit(score_img, (10, 10)) # позиция счетчика машин
    screen.blit(coin_score_img, (10, 30)) # позиция счетчика монет
    screen.blit(speed_img, (10, 50)) # скорость вражеской машины

    E1.draw(screen)
    P1.draw(screen)
    C1.draw(screen)
    pygame.display.update()
    clock.tick(FPS)