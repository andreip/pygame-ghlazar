#!/usr/bin/env python

import pygame
from pygame.locals import *

white = (255, 255, 255)
red = (255, 0, 0)

# TODO: define the green color.
green = (0, 255, 0)


if __name__ == '__main__':

    screen = pygame.display.set_mode((400, 400), DOUBLEBUF)
    screen.fill(white)

    pygame.draw.circle(screen, red, (200, 200), 100, 5)

    # TODO: draw a green triangle over the red circle. You can use either a
    # polygon or 3 lines.
    pygame.draw.polygon(screen, green, [[200, 100], [100, 250], [300, 250]], 5)

    pygame.display.flip()

    running = True
    while running:
        event = pygame.event.wait()

        if event.type == pygame.QUIT:
            running = False

    pygame.quit()
