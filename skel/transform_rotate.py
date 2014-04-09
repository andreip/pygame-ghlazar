#!/usr/bin/env python

import pygame
from pygame.locals import *

white = (255, 255, 255)
window_size = (400, 400)


if __name__ == '__main__':

    pygame.init()

    screen = pygame.display.set_mode(window_size, DOUBLEBUF)
    screen.fill(white)

    tux = pygame.image.load('tux.png')
    tux = pygame.transform.scale(tux, window_size)

    # TODO: rotate the image with 90 degrees.

    screen.blit(tux, (0, 0))
    pygame.display.flip()

    running = True
    while running:
        event = pygame.event.wait()

        if event.type == pygame.QUIT:
            running = False

    pygame.quit()
