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

        self.depl = (0, 0)

    def update(self, deltat):
        x, y = self.position
        dx, dy = self.depl

        # Update the position only if the image stays in borders.
        if (x + dx > 0 and x + dx < window_size[0] and
            y + dy > 0 and y + dy < window_size[1]):
            self.position = (x + dx, y + dy)

        self.rect = self.image.get_rect()
        self.rect.center = self.position


if __name__ == '__main__':

    pygame.init()

    clock = pygame.time.Clock()

    # Init the screen.
    screen = pygame.display.set_mode(window_size, DOUBLEBUF)
    screen.fill(white)

    # Init the background.
    background = pygame.image.load('grass.png')
    background = pygame.transform.scale(background, window_size)
    screen.blit(background, (0, 0))

    # Init the image.
    rect = screen.get_rect()
    sheep = SheepSprite('sheep.png', rect.center)
    sheep_group = pygame.sprite.RenderPlain(sheep)


    running = True
    while running:
        deltat = clock.tick(30)

        # Wait for an event, exit gracefully on close.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if not hasattr(event, 'key'):
                continue

            # Stop moving the sprite when the key is released.
            if event.type == KEYUP:
                sheep.depl = (0, 0)
                continue

            # On key pressed, determine the direction.
            if event.key == K_UP:
                sheep.depl = (0, -10)
            elif event.key == K_DOWN:
                sheep.depl = (0, 10)
            if event.key == K_RIGHT:
                sheep.depl = (10, 0)
            elif event.key == K_LEFT:
                sheep.depl = (-10, 0)

        # Update the sprites group.
        sheep_group.clear(screen, background)
        sheep_group.update(deltat)
        sheep_group.draw(screen)

        pygame.display.flip()

    pygame.quit()