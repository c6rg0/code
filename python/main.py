import pygame
import sys
import time

pygame.init()
window = pygame.display.set_mode((1080, 720))
clock = pygame.time.Clock()
run = True
color = (255, 255, 255)

def circle_mouse():
    pos = pygame.draw.circle(window, color = (0, 0, 0), center = (-5,0), radius = 10)
    print(pos)
    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
        mouse_pos = pygame.mouse.get_pos()
        if -5 < pos(0) < 5:
            if -5 < pos(1) < 5:
                print("click")



while run == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    circle_mouse()
                    
    window.fill(color)
    pygame.display.update()
    clock.tick(180)

