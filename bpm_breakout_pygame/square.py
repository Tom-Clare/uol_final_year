import pygame
import random

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

class Square(pygame.sprite.Sprite):
    def __init__(self, colour, width, height):
        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(WHITE)
        self.image.set_colorkey(BLACK)

        print("Working!!")

        pygame.draw.rect(self.image, colour, [0,0,width, height])

        self.rect = self.image.get_rect()

    def moveRight(self):
        self.rect.x += 5

    def newPos(self):
        new_x_pos = random.randint(0,699)
        self.rect.x = new_x_pos
        
        new_y_pos = random.randint(0,499)
        self.rect.y = new_y_pos

    def moveLeft(self, pixels):
        self.rect.x -= pixels