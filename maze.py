import pygame, sys
import random
import numpy as np
import DecisionFactory as DF
import time

#Colors
Black = (0, 0, 0)
White = (255, 255, 255)
Green = (0, 255, 0)
Red = (255, 0, 0)
Blue = (0, 0, 255)

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

# creates our blank maze, fills in every space as a white tile
for row in range(10):
    for col in range(10):
        color = White
        pygame.draw.rect(screen, color, [(Marg + W) * col + Marg,
                              (Marg + H) * row + Marg,
                              W,
                              H])

# fills in our walls around the perimeter of the maze
for x in range(10):
    color = Blue
    grid[0][x] = "Wall"
    pygame.draw.rect(screen, color, [(Marg + W) * x + Marg,
                          (Marg + H) * 0 + Marg,
                          W,
                          H])
    grid[x][0] = "Wall"
    pygame.draw.rect(screen, color, [(Marg + W) * 0 + Marg,
                          (Marg + H) * x + Marg,
                          W,
                          H])
    grid[9][x] = "Wall"
    pygame.draw.rect(screen, color, [(Marg + W) * x + Marg,
                          (Marg + H) * 9 + Marg,
                          W,
                          H])
    grid[x][9] = "Wall"
    pygame.draw.rect(screen, color, [(Marg + W) * 9 + Marg,
                          (Marg + H) * x + Marg,
                          W,
                          H])

# intializes our portal and agent coordinates to 0
# px, py = Portal (x,y) ax,ay = Agent (x,y)
px = py = ax = ay = 0

# rerolls coordinates until the two are not equal
while px == ax and py == ay:
    px = random.randrange(1, 9)
    py = random.randrange(1, 9)
    ax = random.randrange(1, 9)
    ay = random.randrange(1, 9)

# creates our red portal for our agent
pygame.draw.rect(screen, Red, [(Marg + W) * py + Marg,
                      (Marg + H) * px + Marg,
                      W,
                      H])

# creates our green agent
pygame.draw.rect(screen, Green, [(Marg + W) * ay + Marg,
                      (Marg + H) * ax + Marg,
                      W,
                      H])
#screen set up.

#create our class object
AM = DF.DecisionFactory()

#init step count
step = 0

run = True
while run:
    step = step + 1

    move_status = 'success'

    # AM makes a move
    # AM asks its class to get a random direction
    direction = AM.get_decision()
    # we then use that direction to ensure a valid move for AM
    # if the direction is valid, we graphically update the screen, making the old square white and changing his position
    if direction == 'up':
        if (grid[ay - 1][ax]) != "Wall":
            pygame.draw.rect(screen, White, [(Marg + W) * ay + Marg,
                      (Marg + H) * ax + Marg,
                      W,
                      H])
            ay = ay - 1
        else:
            move_status = 'failure'
    elif direction == 'down':
        if (grid[ay + 1][ax]) != "Wall":
            pygame.draw.rect(screen, White, [(Marg + W) * ay + Marg,
                      (Marg + H) * ax + Marg,
                      W,
                      H])
            ay = ay + 1
        else:
            move_status = 'failure'
    elif direction == 'left':
        if (grid[ay][ax - 1]) != "Wall":
            pygame.draw.rect(screen, White, [(Marg + W) * ay + Marg,
                      (Marg + H) * ax + Marg,
                      W,
                      H])
            ax = ax - 1
        else:
            move_status = 'failure'
    elif direction == 'right':
        if (grid[ay][ax + 1]) != "Wall":
            pygame.draw.rect(screen, White, [(Marg + W) * ay + Marg,
                      (Marg + H) * ax + Marg,
                      W,
                      H])
            ax = ax + 1
        else:
            move_status = 'failure'
    elif direction == 'wait':
        pass
    
    # if our agent moved, we then have to redraw him on the correct hex for the GUI

    if move_status == 'success':
        pygame.draw.rect(screen, Green, [(Marg + W) * ay + Marg,
                      (Marg + H) * ax + Marg,
                      W,
                      H])

    # check win condition
    if ax == px and ay == py:
        run = False
        move_status = 'portal'

    # return move_status to AM
    AM.put_result(move_status)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        #elif event.type == pygame.MOUSEBUTTONDOWN:
    pygame.display.flip()

    #This exists for sake of the GUI's representation
    time.sleep(0.1)
pygame.quit()

#print win
print("It took", step, "# of steps to win.")

#save result to disk
"""
with open('results.txt', 'a') as save:
    save.write(str(step))
    save.write('\n')
"""