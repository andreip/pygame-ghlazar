#!/usr/bin/env python

import random
import pygame
from pygame.locals import *

white = (255, 255, 255)
window_size = (640, 480)
image_size = (100, 100)


if __name__ == '__main__':

    pygame.init()

    clock = pygame.time.Clock()

    # Init the screen.
    screen = pygame.display.set_mode(window_size, DOUBLEBUF)
    screen.fill(white)

    # Init the image.
    note = pygame.image.load('note.png')
    note = pygame.transform.scale(note, image_size)

    # Place the image in the top left corner.
    x, y = (0, 0)

    running = True
    while running:
        clock.tick(30)

        # Wait for an event, exit gracefully on close.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break

            # TODO: when SPACE key is pressed, choose a random position for
            # the image to be placed at.
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    x = random.randint(0, window_size[0] - image_size[0])
                    y = random.randint(0, window_size[1] - image_size[1])

        # Display the image.
        screen.fill(white)
        screen.blit(note, (x, y))
        pygame.display.flip()

    pygame.quit()
