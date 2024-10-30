import pygame
import random
import math
pygame.mixer.init()

class Balle(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()
        self.game = game
        self.image = pygame.image.load('assets/D_balle.png')
        self.image = pygame.transform.scale(self.image, (40, 30))
        self.velocity = pygame.Vector2(random.choice([10, 5, 8, -10, -5, -8]), random.choice([10, 7, 9]))
        self.radius = 20
        self.rebond = 0
        self.rect = self.image.get_rect()
        self.rect.x = 525
        self.rect.y = random.choice([15,39,100,50,60,20])
        self.son = pygame.mixer.Sound("sound/impact.wav")

    def throw_in1(self):
        self.rect.x += self.velocity.x
        self.rect.y += self.velocity.y
        if self.rect.y - self.radius < 0 or self.rect.y + self.radius > 630 or self.rect.top >= self.game.player1.rect.top + self.rect.height and self.rect.bottom == self.game.player1.rect.top or self.rect.top >= self.game.player2.rect.top + self.rect.height and self.rect.bottom == self.game.player2.rect.top:
            self.velocity.y = -self.velocity.y
        elif self.game.check_collision(self, self.game.players):
            
            for collide in self.game.check_collision(self, self.game.players):
                # Réajuster la position du joueur en dehors de l'ennemi
                if self.game.player1.rect.right > self.rect.left and self.game.player1.rect.left < self.rect.left:
                   self.rect.left = self.game.player1.rect.right  
                if self.game.player1.rect.left < self.rect.right and self.game.player1.rect.right > self.rect.right:
                    self.rect.right = self.game.player1.rect.left
                if self.game.player2.rect.right > self.rect.left and self.game.player2.rect.left <self.rect.left:
                    self.rect.left =  self.game.player2.rect.right 
                if self.game.player2.rect.left < self.rect.right and self.game.player2.rect.right > self.rect.right:
                    self.rect.right =self.game.player2.rect.left
            self.son.play(maxtime = 300)
            self.velocity.x = -self.velocity.x
            self.rebond += 1   
            if self.rebond < 5:
                if self.velocity.x < 0:
                    self.velocity.x += random.choice([-2,-4])
                elif self.velocity.x > 0:
                    self.velocity.x += random.choice([2,4])
            elif self.rebond > 5:
                if self.velocity.x < 0:
                    self.velocity.x += random.choice([8,10,9])
                elif self.velocity.x > 0:
                    self.velocity.x += random.choice([-9,-8,-10])
                self.rebond = 0    
                        
    def remove(self):
        self.game.balles.remove(self)

#Essayer de creer une formule mathemaqtique ou une fonction, une suite numerique qui te simule laugmentation de la vitesse au cour du temps et du nmobre de contatc de la balle 