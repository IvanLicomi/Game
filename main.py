import pygame
import sys, time

pygame.init()

run = True
screen = pygame.display.set_mode((640, 480))
r = pygame.Rect(25, 25, 50, 100)
red = 255
green = 0
blue = 0
colors = [red, green, blue]

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    # pygame.draw.rect(screen, (red, green, blue), r, 4)
    pygame.draw.polygon(screen, (red, green, blue), ((30, 25), (0, 100), (90, 100), (60, 25)), width=0)
    pygame.display.flip()
    time.sleep(0.01)
else:
    pygame.quit()
    sys.exit()