import pygame
pygame.init()

width = 500
height = 500

surf = pygame.display.set_mode([width,height])

class Player():
    def __init__(self):
        self.image = pygame.image.load("player.png").covert_alpah()
        self.rect = self.image.get_rect()
