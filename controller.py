import pygame

def keyPressed(keysPressed, inputKey):
    if keysPressed[inputKey]:
        return True
    else:
        return False
        
def controller(character, screenWidth, screenHeight, keys):
    if keys[pygame.K_LEFT] and character.x > character.speed:
        character.facing = 'left'
        character.x -= character.speed
    if keys[pygame.K_RIGHT] and character.x < screenWidth - character.width - character.speed:
        character.facing = 'right'
        character.x += character.speed
    if keys[pygame.K_UP] and character.y > character.speed:
        character.facing = 'up'
        character.y -= character.speed
    if keys[pygame.K_DOWN] and character.y < screenHeight - character.height - character.speed:
        character.facing = 'down'
        character.y += character.speed
    if keyPressed(keys, pygame.K_SPACE):
        character.armed = True
    if keyPressed(keys,pygame.K_SPACE) == False:
        character.armed = False
