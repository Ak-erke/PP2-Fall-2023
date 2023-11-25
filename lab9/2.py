import pygame
from pygame.locals import *
from sys import exit

class MusicPlayer:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((500, 200), 0, 32)
        pygame.display.set_caption("Music Player")

        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont("calibri", 40)

        self.playing = False
        self.paused = False

        self.current_song = 0
        self.songs = [
            r'C:\Users\user\PP2\lab9\Swedish House Mafia feat. The Weeknd - Moth To A Flame (Live From Copenhagen).mp3',
            r'C:\Users\user\PP2\lab9\The Weeknd feat. Lily Rose Depp - Dollhouse.mp3',
            r'C:\Users\user\PP2\lab9\The Weeknd,JENNIE,Lily-Rose Depp - One Of The Girls (with JENNIE, Lily Rose Depp).mp3'
        ]

        pygame.mixer.init()
        self.play_music()

        # Load images for buttons
        self.play_image = pygame.image.load("48-483851_play-button-png-icono-gmail-png-clipart.png").convert_alpha()
        self.next_image = pygame.image.load("img_447598.png").convert_alpha()
        self.prev_image = pygame.image.load("img_146921.png").convert_alpha()

    def play_music(self):
        pygame.mixer.music.load(self.songs[self.current_song])
        pygame.mixer.music.play()
        self.playing = True

    def toggle_play_pause(self):
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.pause()
            self.playing = False
        else:
            pygame.mixer.music.unpause()
            self.playing = True

    def next_music(self):
        self.current_song = (self.current_song + 1) % len(self.songs)
        self.play_music()

    def prev_music(self):
        self.current_song = (self.current_song - 1) % len(self.songs)
        self.play_music()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()

                if event.type == KEYDOWN:
                    if event.key == K_SPACE:
                        self.toggle_play_pause()
                    elif event.key == K_RIGHT:
                        self.next_music()
                    elif event.key == K_LEFT:
                        self.prev_music()

            self.screen.fill((255, 255, 255))

            # Display images for buttons
            self.screen.blit(self.play_image, (200, 100))
            self.screen.blit(self.next_image, (350, 50))
            self.screen.blit(self.prev_image, (50, 50))

            pygame.display.update()
            self.clock.tick(10)

if __name__ == "__main__":
    player = MusicPlayer()
    player.run()
