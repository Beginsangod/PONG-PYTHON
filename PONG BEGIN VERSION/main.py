import pygame
from game import Game


pygame.init()
pygame.font.init()


pygame.display.set_caption("PONG BEGIN VERSION")
windows = pygame.display.set_mode((1080,640))
clock = pygame.time.Clock()
FPS = 60

background = pygame.image.load('assets/D_decor.png')   
banner = pygame.image.load('assets/D-02.png')
banner = pygame.transform.scale(banner, (600,600))
cpu_button = pygame.image.load('assets/D-03.png')
cpu_button = pygame.transform.scale(cpu_button, (300, 200))
cpu_button_rect = cpu_button.get_rect()
cpu_button_rect.x = 160
cpu_button_rect.y = 390
player2_button = pygame.image.load('assets/D-04.png')
player2_button = pygame.transform.scale(player2_button, (300,200))
player2_button_rect = player2_button.get_rect()
player2_button_rect.x = 500
player2_button_rect.y = 390
font = pygame.font.SysFont("teko", 100)
game = Game()

running = True

while running:
    windows.blit(background, (0,0))

    if game.playon:
        game.update(windows, font)
    else:
        windows.blit(banner, (235,0))
        windows.blit(cpu_button, cpu_button_rect)
        windows.blit(player2_button, player2_button_rect)

    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
                game.pressed[event.key] = True        
        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if cpu_button_rect.collidepoint(event.pos):
                game.playon = True
                game.IA = True
            elif player2_button_rect.collidepoint(event.pos):
                game.playon = True
    clock.tick(FPS)