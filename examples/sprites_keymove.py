#!/usr/bin/env python

import pygame
from pygame.locals import *

white = (255, 255, 255)
window_size = (640, 480)
image_size = (100, 100)


class SheepSprite(pygame.sprite.Sprite):

    def __init__(self, image, position):
        pygame.sprite.Sprite.__init__(self)

        self.position = position
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, image_size)

    def update(self, deltat):
        self.rect = self.image.get_rect()
        self.rect.center = self.position


if __name__ == '__main__':

    pygame.init()

    clock = pygame.time.Clock()

    # Init the screen.
    screen = pygame.display.set_mode(window_size, DOUBLEBUF)
    screen.fill(white)

    # Init the image.
    rect = screen.get_rect()
    sheep = SheepSprite('sheep.png', rect.center)
    sheep_group = pygame.sprite.RenderPlain(sheep)

    # Init the background.
    background = pygame.image.load('grass.png')
    screen.blit(background, (0, 0))


    running = True
    while running:
        deltat = clock.tick(30)

        # Wait for an event, exit gracefully on close.
        event = pygame.event.wait()
        if event.type == pygame.QUIT:
            running = False

        sheep_group.clear(screen, background)
        sheep_group.update(deltat)
        sheep_group.draw(screen)
        pygame.display.flip()

    pygame.quit()
