#!/usr/bin/env python

import pygame
from pygame.locals import *

white = (255, 255, 255)

# TODO: define ALL the colors.


if __name__ == '__main__':

    screen = pygame.display.set_mode((800, 400), DOUBLEBUF)
    screen.fill(white)


    # TODO: draw the olyimpic circles logo. You can search for a picture
    # online.


    pygame.display.flip()

    running = True
    while running:
        event = pygame.event.wait()

        if event.type == pygame.QUIT:
            running = False

    pygame.quit()
