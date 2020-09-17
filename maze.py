import pygame, sys
import random
import numpy as np
#import df.py as df


#Colors
Black = (0, 0, 0)
White = (255, 255, 255)
Green = (0, 255, 0)
Red = (255, 0, 0)

pygame.init()

#variables for screen
screen_w = 255
screen_h = 255
screen = pygame.display.set_mode((screen_w, screen_h))


font = pygame.font.Font(None, 100)


screen.fill(Black)

#tmp_sq = pygame.draw.rect(screen, [50, 40, 100], [0, 0, 400, 400], 0)
# for grid screen.
W = 20
H = 20
Marg = 5
grid = []

""" This will be the matrix 'grid' that will represent the map. """
for row in range(10):
    # Add an empty array that will hold each cell
    # in this row
    grid.append([])
    for column in range(10):
        grid[row].append(0)  # Append a cell


for row in range(10):
    for col in range(10):

        color = White



        pygame.draw.rect(screen, color, [(Marg + W) * col + Marg,
                              (Marg + H) * row + Marg,
                              W,
                              H])


x = random.randrange(0, 10)
y = random.randrange(0, 10)


pygame.draw.rect(screen, Red, [(Marg + W) * y + Marg,
                      (Marg + H) * x + Marg,
                      W,
                      H])
print(x)
#screen set up.
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        #elif event.type == pygame.MOUSEBUTTONDOWN:





    pygame.display.flip()

pygame.quit()
