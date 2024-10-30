import pygame

class Bar():
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('assets/D_bar.png')
        self.rect = self.image.get_rect()
        self.rect.x = 460