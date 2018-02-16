import pygame as pygame

class Cell(pygame.sprite.Sprite):
    def __init__(self, i, j, solid, image, doorway=None):
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)

        self.solid = solid
        self.doorway = doorway
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = i*self.rect.width
        self.rect.y = j*self.rect.height
        # Position in the map matrix
        self.i = i
        self.j = j

    def setPosition(self, x, y):
        self.rect[0] = x*self.rect[2]
        self.rect[1] = y*self.rect[3]