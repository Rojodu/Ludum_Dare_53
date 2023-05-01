import pygame.image as img

class player(object):
    hero_images = [img.load('resources/H'+ str(i) +'.png') for i in range(10)]
    hero_images_dict = {
        'front':hero_images[0],
        'down':hero_images[1],
        'up':hero_images[2],
        'left':hero_images[3],
        'right':hero_images[4],
        'sword_down':hero_images[5],
        'sword_up':hero_images[6],
        'sword_left':hero_images[7],
        'sword_right':hero_images[8],
        'sword_front':hero_images[9]
    }
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = 2
        self.facing = 'front'
        self.armed = False
    
    def draw(self, window):
        if self.armed == True:
            if self.facing == 'front':
                self.facing = 'sword_front'
            elif self.facing == 'down':
                self.facing = 'sword_down'
            elif self.facing == 'up':
                self.facing = 'sword_up'
            elif self.facing == 'right':
                self.facing = 'sword_right'
            elif self.facing == 'left':
                self.facing = 'sword_left'
        facing = self.facing
        window.blit(self.hero_images_dict[facing], (self.x, self.y))
    