import pygame
from pygame.locals import *


class Pilula(pygame.sprite.Sprite):
    def __init__(self, cor, efeito, reseta_tamanho, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.cor = cor 
        self.efeito = efeito
        self.reseta_tamanho = reseta_tamanho
        self.x = x
        self.y = y
        self.superficie = pygame.Surface((20, 20))
        self.superficie.fill(self.cor)
        self.rect = self.superficie.get_rect(bottomleft = (self.x, self.y))
        img = pygame.image.load('images/pilula_verm.png')
        self.image = pygame.transform.scale(img, (28 , 34))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

