import pygame
from abc import ABC, abstractmethod

class Inimigo(ABC, pygame.sprite.Sprite):
    def __init__(self, cor, velocidade, largura, altura, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.cor = cor
        self.velocidade = velocidade
        self.largura = largura
        self.altura = altura
        self.x = x
        self.y = y
        self.superficie = pygame.Surface((self.largura, self.altura))
        self.superficie.fill(self.cor)
        self.rect = self.superficie.get_rect(bottomleft = (self.x, self.y))
        self.image = self.superficie

    @abstractmethod
    def andar(self):
        pass

