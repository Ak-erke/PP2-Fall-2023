import pygame
import sys
import datetime

pygame.init()
w, h = 900, 900
window = pygame.display.set_mode((w, h))
pygame.display.set_caption('Mickey Mouse Clock')

righthand = pygame.image.load('right-hand.png').convert_alpha()
lefthand = pygame.image.load('left-hand.png').convert_alpha()
clockface = pygame.image.load('main-clock.png').convert_alpha()

center = (w // 2, h // 2)
radius = 150

def rotate_hand(image, angle):
    return pygame.transform.rotate(image, -angle)

running = True
clock = pygame.time.Clock()

while running:
    window.fill((255, 255, 255)) 

    current_time = datetime.datetime.now()
    currentmin = current_time.minute
    currentsec = current_time.second

    minangle = (360 * currentmin) // 60
    secangle = (360 * currentsec) // 60

    rotrighthand = rotate_hand(righthand, minangle)
    rotlefthand = rotate_hand(lefthand, secangle)

    righthandpositive = (center[0] - rotrighthand.get_width() // 2,
                      center[1] - rotrighthand.get_height() // 2)
    lefthandpositive = (center[0] - rotlefthand.get_width() // 2,
                     center[1] - rotlefthand.get_height() // 2)

    window.blit(clockface, (w // 2 - clockface.get_width() // 2, h // 2 - clockface.get_height() // 2))
    window.blit(rotrighthand, righthandpositive)
    window.blit(rotlefthand, lefthandpositive)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()