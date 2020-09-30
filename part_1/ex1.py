import pygame
from pygame.draw import *
from math import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))
screen.fill((250, 250, 250))
#drawing face
circle(screen, (255, 255, 0), (200, 200), 100)
circle(screen, (0, 0, 0), (200, 200), 100, 1)
#drawing eyes
circle(screen, (255, 0, 0), (150, 170), 20)
circle(screen, (255, 0, 0), (250, 170), 12)
circle(screen, (0, 0, 0), (150, 170), 10)
circle(screen, (0, 0, 0), (250, 170), 7)
circle(screen, (0, 0, 0), (150, 170), 20, 1)
circle(screen, (0, 0, 0), (250, 170), 12, 1)
#drawing eyebrows
line(screen, (0, 0, 0), (190, 170), (100, 107.5), 10)
line(screen, (0, 0, 0), (250-12/tan(pi/12), 165), (280, 165 - (30 + 12/tan(pi/12)) * tan(pi/12) ), 8)
#drawing mouth
polygon(screen, (0, 0, 0), [(160, 250), (160, 270),
                            (240, 270), (240, 250)])

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
