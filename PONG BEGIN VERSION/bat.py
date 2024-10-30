import pygame

class Bat(pygame.sprite.Sprite):
    def __init__(self, rectx, recty, velocity, game):
        super().__init__()
        self.game = game
        self.image = pygame.image.load('assets/D_bat.png')
        self.image = pygame.transform.scale(self.image, (20, 130))
        self.velocity = velocity
        self.score = 0
        self.max_score = 15
        self.rect = self.image.get_rect()
        self.rect.x = rectx
        self.rect.y = recty

    def moveright(self):
        if not self.game.check_collision(self, self.game.balles):
            self.rect.x += self.velocity

    def moveleft(self):
        if not self.game.check_collision(self, self.game.balles):
            self.rect.x -= self.velocity

    def moveup(self):
        if not self.game.check_collision(self, self.game.balles):
            self.rect.y -= self.velocity

    def movedown(self):
        if not self.game.check_collision(self, self.game.balles):
            self.rect.y += self.velocity