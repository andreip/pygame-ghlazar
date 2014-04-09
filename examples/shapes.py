#!/usr/bin/env python

import pygame
from pygame.locals import *

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)


if __name__ == '__main__':

    screen = pygame.display.set_mode((600, 400), DOUBLEBUF)
    screen.fill(black)

    box = pygame.Rect(100, 100, 200, 150)
    pygame.draw.rect(screen, white, box, 5)

    pygame.draw.circle(screen, red, (450, 250), 50, 3)

    pygame.display.flip()

    running = True
    while running:
        event = pygame.event.wait()

        if event.type == pygame.QUIT:
            running = False

    pygame.quit()
