import pygame
import sys
pygame.init()

screenw, screenh = 800, 600
screen = pygame.display.set_mode((screenw, screenh))
pygame.display.set_caption("Moving Ball")

ballr = 25
ballcolor = (255, 0, 0)  
ballx, bally = screenw // 2, screenh // 2  



clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and bally - 20 >= ballr:
        bally -= 20
    if keys[pygame.K_DOWN] and bally + 20 <= screenh - ballr:
        bally += 20
    if keys[pygame.K_LEFT] and ballx - 20 >= ballr:
        ballx -= 20
    if keys[pygame.K_RIGHT] and ballx + 20 <= screenw - ballr:
        ballx += 20

    screen.fill((255, 255, 255)) 
    pygame.draw.circle(screen, ballcolor, (ballx, bally), ballr)
    pygame.display.flip()
    clock.tick(60)