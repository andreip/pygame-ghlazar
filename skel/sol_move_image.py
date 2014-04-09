#!/usr/bin/env python

import random
import pygame
from pygame.locals import *

white = (255, 255, 255)
window_size = (400, 400)
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
    x, y = (0, 150)
    dx = 10

    running = True
    while running:
        clock.tick(30)

        # Wait for an event, exit gracefully on close.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break

        # TODO: update the x and dx so that the image moves to the left, and
        # when it hits the margine, it moved to the right.
        if x + dx < 0 or x + dx + image_size[0] > window_size[0]:
            dx *= -1
        x += dx

        # Display the image.
        screen.fill(white)
        screen.blit(note, (x, y))
        pygame.display.flip()

    pygame.quit()
