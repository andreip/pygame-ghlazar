#!/usr/bin/env python

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
    sheep = pygame.image.load('sheep.png')
    sheep = pygame.transform.scale(sheep, image_size)

    x, y = (0, 0)
    dx, dy = (10, 10)

    running = True
    while running:
        clock.tick(30)

        # Wait for an event, exit gracefully on close.
        event = pygame.event.wait()
        if event.type == pygame.QUIT:
            running = False

        # Display the image.
        screen.fill(white)
        screen.blit(sheep, (x, y))
        pygame.display.flip()

        # Update the delta for each coordinate.
        if x + image_size[0] > window_size[0] or x < 0:
            dx *= -1
        if y + image_size[1] > window_size[1] or y < 0:
            dy *= -1

        # Update the position.
        x += dx
        y += dy

    pygame.quit()
