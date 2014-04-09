"""
Steps in building this:
1. pygame.display.set_mode returns a surface, play w/ the surface, fill it
2. pygame.image, checkout its methods, use load
3. image is 2000 x 1000, scale it to 100 x 50 for our screen,
   pygame.transform ; play with scale, rotate
4. put image on screen, check help(screen) for methods; screen.blit (block
   image transfer)
   ; need to do a pygame.display.flip() to show it
5. do animations? use fill + blit in a for loop
6. pygame.time.Clock() ; want to change the default tick
"""

import pygame
from pygame.locals import *

clock = pygame.time.Clock()

def get_car(car_path, scale=(100,50)):
    """2"""
    car = pygame.image.load(car_path)
    """3"""
    car = pygame.transform.scale(car, (100,50))
    return car

def animate_car(car, times=3):
    for j in range(times):
        for i in range(screen.get_width() + car.get_width()):
            """6 need to change fps every time; nush de ce"""
            change_fps(10)
            """5"""
            screen.fill((0,0,0))
            screen.blit(car, (screen.get_width() - i, 50))
            pygame.display.flip()

def change_fps(fps=30):
    deltat = clock.tick(fps)
    print deltat

if __name__ == "__main__":
    """1"""
    screen = pygame.display.set_mode((768,300))
    """2"""
    car = get_car('car.png')
    """4"""
    screen.blit(car, (50,100))
    pygame.display.flip()
    """5"""
    animate_car(car)
    # So screen stays longer.
    pygame.time.delay(3000)
