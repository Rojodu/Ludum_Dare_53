import pygame

FPS = 60
screenWidth = 1280
screenHeight = 720
background = pygame.image.load('Village.png')
window = pygame.display.set_mode((screenWidth, screenHeight))

class player(object):
    hero = pygame.image.load('My project.png')
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = 2
    
    def draw(self, window):
        window.blit(self.hero, (self.x, self.y))

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
        controller(hero, keys)

        drawGameWindow()
        fpsclock.tick(FPS)
    pygame.quit()

def drawGameWindow():
    window.blit(background, (0, 0))
    hero.draw(window)
    pygame.display.update()

def controller(character, keys):
    if keys[pygame.K_LEFT] and character.x > character.speed:
        character.x -= character.speed
    if keys[pygame.K_RIGHT] and character.x < screenWidth - character.width - character.speed:
        character.x += character.speed
    if keys[pygame.K_UP] and character.y > character.speed:
        character.y -= character.speed
    if keys[pygame.K_DOWN] and character.y < screenHeight - character.height - character.speed:
        character.y += character.speed

if __name__ == '__main__':
    main()