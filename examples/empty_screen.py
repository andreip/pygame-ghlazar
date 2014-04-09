#!/usr/bin/env python

import pygame
from pygame.locals import *


if __name__ == '__main__':

    screen = pygame.display.set_mode((600, 400))

    running = True
    while running:
        event = pygame.event.wait()

        if event.type == pygame.QUIT:
            running = False

    pygame.quit()
