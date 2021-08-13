import pygame
from pygame.constants import BUTTON_LEFT

class Caixa(pygame.sprite.Sprite):
    def __init__(self, altura: int, largura: int, x, y, forca_necessaria):
        pygame.sprite.Sprite.__init__(self)
        self.altura = altura
        self.largura = largura
        self.x = x
        self.y = y
        self.superficie = pygame.Surface((self.largura, self.altura))
        self.superficie.fill('Brown')
        self.rect = self.superficie.get_rect(bottomleft = (self.x, self.y))
        self.image = self.superficie
        self.forca_necessaria = forca_necessaria