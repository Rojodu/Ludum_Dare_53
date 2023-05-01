import pygame
import pygame.image as img
from player import *
from controller import *

FPS = 60
screenWidth = 1280
screenHeight = 720
background = img.load('resources/Village.png')
window = pygame.display.set_mode((screenWidth, screenHeight))

hero = player(40,180,16,32)
def main():
    pygame.init()
    fpsclock = pygame.time.Clock()
    pygame.display.set_caption("Ludum Dare 53")
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        keys = pygame.key.get_pressed()
        controller(hero, screenWidth, screenHeight,keys)

        drawGameWindow()
        fpsclock.tick(FPS)
    pygame.quit()

def drawGameWindow():
    window.blit(background, (0, 0))
    hero.draw(window)
    pygame.display.update()

if __name__ == '__main__':
    main()