import pygame
from bar import *
from bat import *
from balle import *
pygame.init()
pygame.mixer.init()

class Game():
    def __init__(self):
        self.playon = False
        self.victory = False
        self.players = pygame.sprite.Group()
        self.player1 = Bat(20, 250, 7, self)
        self.player2 = Bat(1000, 250, 15,self)
        self.players.add(self.player2)
        self.players.add(self.player1)
        self.bar = Bar()
        self.balles = pygame.sprite.Group()
        self.pressed = {}
        self.font = pygame.font.SysFont("teko", 50)
        self.IA = False
        self.launch_ball()

    def update(self, windows, font):

        score1 = font.render(str(self.player1.score),True,(255,255,255))
        score2 = font.render(str(self.player2.score) ,True,(255,255,255))
    
        windows.blit(self.player1.image, self.player1.rect)
        windows.blit(self.player2.image, self.player2.rect)
        windows.blit(self.bar.image, self.bar.rect)

        if self.player1.score == 15:
            score1 = font.render("winner",True,(255,255,255))
            score2 = font.render("loser",True,(255,255,255))
            replay = self.font.render("Tap enter to replay",True,(255,255,255))
            windows.blit(replay, (30,530))
            self.victory = True
        elif self.player2.score == 15:
            score2 = font.render("winner",True,(255,255,255))
            score1 = font.render("loser",True,(255,255,255))
            replay = self.font.render("Tap enter to replay",True,(255,255,255))
            windows.blit(replay, (30,530))
            self.victory = True

        windows.blit(score1, (150,0))
        windows.blit(score2, (self.bar.rect.x + 300, 0))


        if self.victory == False:
            for balle in self.balles:
                    balle.throw_in1()

            for balle in self.balles:
                if balle.rect.x > 1080 or balle.rect.x < 0:
                    balle.remove()
                    self.launch_ball()
                    if balle.rect.x > 1080:
                        self.player1.score += 1
                    if balle.rect.x < 0:
                        self.player2.score += 1

            self.balles.draw(windows)
        
            if self.IA:
                if self.player1.rect.y + 30 < balle.rect.y and self.player1.rect.y + self.player1.rect.height < windows.get_height() - 20:
                    self.player1.movedown()
                elif self.player1.rect.y + 1 > balle.rect.y:
                    self.player1.moveup()
                elif self.player1.rect.x < balle.rect.x + 2 and balle.rect.x > (windows.get_width()*50)/100 and self.player1.rect.x + self.player1.rect.width < ((windows.get_width()*50)/100) - 70:
                    self.player1.moveright()
                elif balle.rect.x > 1040 or balle.rect.x < 20 and self.player1.rect.x > 40:
                    self.player1.rect.x -= 100
            else:
                self.player1.velocity = 15
                if self.pressed.get(pygame.K_d) and self.player1.rect.x + self.player1.rect.width < ((windows.get_width()*50)/100) - 70:
                    self.player1.moveright()
                elif self.pressed.get(pygame.K_a) and self.player1.rect.x > 40:
                    self.player1.moveleft()
                elif self.pressed.get(pygame.K_w) and self.player1.rect.y > 20:
                    self.player1.moveup()
                elif self.pressed.get(pygame.K_s) and self.player1.rect.y + self.player1.rect.height < windows.get_height() - 20:
                    self.player1.movedown()

            if self.pressed.get(pygame.K_RIGHT) and self.player2.rect.x + self.player2.rect.width < 1020:
                self.player2.moveright()
            elif self.pressed.get(pygame.K_LEFT) and self.player2.rect.x > ((windows.get_width()*50)/100) + 90:
                self.player2.moveleft()
            elif self.pressed.get(pygame.K_UP) and self.player2.rect.y > 20:
                self.player2.moveup()
            elif self.pressed.get(pygame.K_DOWN) and self.player2.rect.y + self.player2.rect.height < windows.get_height() - 20:
                self.player2.movedown()
        if self.pressed.get(pygame.K_RETURN):
            self.playon = False
            self.victory = False
            self.player1.score = 0
            self.player2.score = 0
            self.player1.rect.x = 20
            self.player2.rect.x = 1000
            self.player2.rect.y = 250
            self.player2.rect.y = 250

    def launch_ball(self):
        balle = Balle(self)
        self.balles.add(balle)

    def check_collision(self ,sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)