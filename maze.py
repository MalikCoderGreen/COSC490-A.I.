import pygame, sys
import random


pygame.init()

#variables for screen
screen_w = 1000
screen_h = 1000
screen = pygame.display.set_mode((screen_w, screen_h))


font = pygame.font.Font(None, 100)

txt = font.render("#", 1500,  (65, 34, 140))
txt_pos = txt.get_rect()
bg = pygame.Surface(screen.get_size())
bg = bg.convert()

# position symbol in top left of screen.
txt_pos.topleft = bg.get_rect().topleft
bg.fill((80, 80, 80))


#tmp_sq = pygame.draw.rect(screen, [50, 40, 100], [0, 0, 400, 400], 0)




# vertixal axis variable.
x = 0
#generate maze.
for i in range (0, 1500):
    r = random.randint(0, 1000)
    tmp_txt = txt
    tmp_txt = tmp_txt.get_rect()
    bg.blit(txt, tmp_txt.move(x, r))
    screen.blit(bg, (0, 0))

    x += 50



#screen set up.
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    screen.blit(bg, (0, 0))

    pygame.display.flip()

pygame.quit()
