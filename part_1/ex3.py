import pygame
from pygame.draw import *

pygame.init()

def draw_fish(position_x, position_y, size):
	Blue = (173, 216, 230)
	Black = (0, 0, 0)
	Salmon = (250, 128, 114)
	Navy= (0, 0, 128)
	#draw fins
	pygame.draw.polygon(screen, Salmon, [(position_x + int(0.1*size), position_y + int (0.2*size)),
	                                     (position_x - int(0.3*size), position_y + int(0.1*size)),
	                                     (position_x - int(0.3*size), position_y + int(0.3*size))
	                                     ])
	pygame.draw.polygon(screen, Black, [(position_x + int(0.1*size), position_y + int (0.2*size)),
	                                     (position_x - int(0.3*size), position_y + int(0.1*size)),
	                                     (position_x - int(0.3*size), position_y + int(0.3*size))
	                                     ],1)
	pygame.draw.polygon(screen, Salmon, [(position_x + int(0.4*size), position_y - int (0.2*size)),
	                                     (position_x + int(0.4*size), position_y + int(0.1*size)),
	                                     (position_x + int(0.8*size), position_y + int(0.2*size))])
	pygame.draw.polygon(screen, Black, [(position_x + int(0.4*size), position_y - int (0.2*size)),
	                                     (position_x + int(0.4*size), position_y + int(0.1*size)),
	                                     (position_x + int(0.8*size), position_y + int(0.2*size))
	                                     ],1)
	pygame.draw.polygon(screen, Salmon, [(position_x + int(0.45*size), position_y + int (0.6*size)),
	                                     (position_x + int(0.25*size), position_y + int(0.1*size)),
	                                     (position_x + int(0.75*size), position_y + int(0.2*size))])
	pygame.draw.polygon(screen, Black, [(position_x + int(0.45*size), position_y + int (0.6*size)),
	                                     (position_x + int(0.25*size), position_y + int(0.1*size)),
	                                     (position_x + int(0.75*size), position_y + int(0.2*size))],1)                                     
	#draw body
	pygame.draw.ellipse(screen, Blue, (position_x, position_y, size, int(0.4*size)))
	pygame.draw.ellipse(screen, Black, (position_x, position_y, size, int(0.4*size)), 1)
	#draw eye
	pygame.draw.ellipse(screen, Navy, (position_x + int(0.8*size), position_y + int(0.1*size), int(0.1*size), int(0.1*size)))
	pygame.draw.ellipse(screen, Black, (position_x + int(0.8*size), position_y + int(0.1*size), int(0.1*size), int(0.1*size)), 1)
	
	
	
def draw_hole(position_x, position_y, size):
	pygame.draw.ellipse(screen, (100, 100, 100), (position_x - int(size/2), position_y - int(size/4), size, int(size/2)))
	pygame.draw.ellipse(screen, (0, 0, 0), (position_x - int(size/2), position_y - int(size/4), size, int(size/2)), 1)	
	pygame.draw.ellipse(screen, (0, 128, 128), (position_x - int(0.4*size), position_y - int(0.15*size), int(0.8*size), int(0.4*size)))
	pygame.draw.ellipse(screen, (0, 0, 0), (position_x - int(0.4*size), position_y - int(0.15*size), int(0.8*size), int(0.4*size)), 1)

def draw_bear(position_x, position_y, size):
	Gray = (211, 211, 211)
	Black = (0, 0, 0)
	
	pygame.draw.ellipse(screen, (Gray), (position_x - int(0.25*size), position_y - int(0.5*size), int(0.5*size), size))
	pygame.draw.ellipse(screen, (Black), (position_x - int(0.25*size), position_y - int(0.5*size), int(0.5*size), size), 1)
	pygame.draw.ellipse(screen, (Gray), (position_x, position_y + int(size/4), int(0.4*size), int(0.3*size)))
	pygame.draw.ellipse(screen, (Black), (position_x, position_y + int(size/4), int(0.4*size), (0.3*size)), 1)
	pygame.draw.ellipse(screen, (Gray), ( position_x + int(0.25*size), position_y + int(0.45*size), int(0.35*size), int(0.15*size)))
	pygame.draw.ellipse(screen, (Black), ( position_x + int(0.25*size), position_y + int(0.45*size), int(0.35*size), int(0.15*size)), 1)
	#draw hand
	pygame.draw.ellipse(screen, (Gray), (position_x + int(0.15*size), position_y - int(0.3*size), int(0.3*size), int(0.15*size)))
	pygame.draw.ellipse(screen, (Black), (position_x + int(0.15*size), position_y - int(0.3*size), int(0.3*size), int(0.15*size)), 1)
	#drawing head
	pygame.draw.ellipse(screen, (Gray), (position_x - int(0.05*size), position_y - int(0.65*size), int (0.45*size), int(0.25*size)))
	pygame.draw.ellipse(screen, (Black), (position_x - int(0.05*size), position_y - int(0.65*size), int(0.45*size), int(0.25*size)), 1)
	pygame.draw.ellipse(screen, (Black), (position_x + int(0.15*size), position_y - int(0.58* size), int(0.04*size), int(0.04*size)))
	pygame.draw.ellipse(screen, (Black), (position_x - int(0.065*size) + int(0.44*size), position_y - int(0.55* size), int(0.04*size), int(0.04*size)))
	pygame.draw.arc(screen, (Black), (position_x, position_y - int(0.7*size), int (0.45*size), int(0.25*size)), 4.5, 5.58)
	pygame.draw.ellipse(screen, (Gray), (position_x - int(0.05*size), position_y - int(0.65*size), int (0.08*size), int(0.08*size)))
	pygame.draw.ellipse(screen, (Black), (position_x - int(0.05*size), position_y - int(0.65*size), int (0.08*size), int(0.08*size)), 1)
	#draw hole
	draw_hole(position_x + int(0.8*size), position_y + int(0.2*size), int(0.4*size))
	#draw rod
	pygame.draw.lines(screen, (Black), False, [(position_x + int(0.32*size), position_y), 
	                                             (position_x + int(0.36*size), position_y - int(0.16*size))],
	                                             5)
	pygame.draw.lines(screen, (Black), False, [(position_x + int(0.4*size), position_y - int(0.275*size)),
	                                            (position_x + int(0.48*size), position_y - int( 0.4*size)),
	                                            (position_x + int(0.8*size), position_y - int(0.8*size))],
	                                            5)
	pygame.draw.lines(screen, (0, 0, 0), False, [(position_x + int(0.8*size), position_y - int(0.8*size)), (position_x + int(0.8*size), position_y + int(0.2*size))], 1)
	
	#draw catch
	draw_fish(position_x + int( 0.8*size), position_y + int(0.35*size), int(0.2*size))
	draw_fish(position_x + int(1.1*size), position_y + int(0.1*size), int(0.2*size))
	draw_fish(position_x + int(1*size), position_y + int(0.23*size), int(0.2*size))		
	
		


FPS = 30
screen = pygame.display.set_mode((1000, 1000))
screen.set_alpha(0)
screen.fill((250, 250, 250))
s = pygame.Surface((1000,1000))  # the size of your rect
s.set_alpha(30)
s.fill((255,255,255, 0))                # alpha level

#draw sun
Yellow=(255, 255, 0)
pygame.draw.ellipse(s, Yellow, (300, 10, 450, 450), 20)
pygame.draw.line(s, Yellow, (300, 235), (750, 235),20)
pygame.draw.line(s, Yellow, (525, 10), (525, 460),20)
#draw world
pygame.draw.rect(screen,(211, 211, 211, 0),(0, 500, 1000, 500))
pygame.draw.rect(screen,(135, 206, 235, 0),(0, 0, 1000, 500))
pygame.draw.line(screen, (0, 0, 0, 0), (0, 500), (1000, 500), 1)
#draw picture
draw_bear(200, 800, 200)
draw_bear(400, 600, 150)
draw_bear(700, 500, 120)
draw_hole(800, 700, 100)
draw_hole(200, 600, 50)
draw_fish(870, 700, 30)
draw_fish(830, 660, 40)
draw_fish(750, 740, 100)
screen.blit(s, (0,0))    




pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.display.quit()
exit()
pygame.quit()
