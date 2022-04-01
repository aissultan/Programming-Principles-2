import pygame, os

pygame.init()
screen = pygame.display.set_mode((400, 500))

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

songs = ['music//garmoniya.mp3', 'music//mimimi.mp3', 'music//monako.mp3', 'music//whenever.mp3', 'music//net_lubvi.mp3', 'music//net.mp3']

pygame.display.set_caption('MP3 Player')

current_song = 0

def play_next_song(next):
    if next == True:
        global songs
        global current_song
        current_song += 1
        if current_song >= len(songs):
            current_song = 0
        pygame.mixer.music.load(songs[current_song])
        pygame.mixer.music.play()
    else:
        if current_song >= 1:
            current_song -= 1
            pygame.mixer.music.load(songs[current_song])
            pygame.mixer.music.play()
        else:
            current_song = 5
            pygame.mixer.music.load(songs[current_song])
            pygame.mixer.music.play()

volume = 1
line_volume = 325
x = 0.1 # для убавления и добавления громкости музыки 
running = True
current_song_ok = False

pygame.mixer.music.load(songs[0])
pygame.mixer.music.play() 

while running:
    screen.fill('yellow')
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                play_next_song(True)
                current_song_ok = True
            if event.key == pygame.K_z:
                play_next_song(False)
            if event.key == pygame.K_1:
                if volume >= x:
                    volume = volume - x
                    pygame.mixer.music.set_volume(volume)
                    line_volume -= 25
            elif event.key == pygame.K_2:
                if volume != 1:
                    volume = volume + x
                    pygame.mixer.music.set_volume(volume)
                    line_volume += 25
            elif event.key == pygame.K_3:
                pygame.mixer.music.pause()
            elif event.key == pygame.K_4:
                pygame.mixer.music.unpause()
                checking_unpause = True
        song_image = pygame.transform.scale(pygame.image.load('images\\' + str(current_song) + '.jpg'), (300, 300))
        screen.blit(song_image, (50, 70))

        pygame.draw.line(screen, BLACK, (75, 400), (325, 400), 3)
        pygame.draw.line(screen, BLUE, (75, 400), (line_volume, 400), 5)
        
        pygame.display.flip()