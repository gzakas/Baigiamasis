import pygame, os
from settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = pygame.image.load(os.path.join('graphics', 'player.png')).convert_alpha()
        self.image_rect = self.image.get_rect()
        self.rect = self.image.get_rect(topleft = pos)