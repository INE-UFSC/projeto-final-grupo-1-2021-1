import pygame
from abc import ABC, abstractmethod

class Inimigo(ABC, pygame.sprite.Sprite):
    def __init__(self, cor, velocidade, largura, altura, x, y, distancia_maxima):
        pygame.sprite.Sprite.__init__(self)
        self.cor = cor
        self.velocidade = velocidade
        self.largura = largura
        self.altura = altura
        self.distancia_maxima = distancia_maxima
        self.x = x
        self.y = y
        self.superficie = pygame.Surface((self.largura, self.altura))
        self.superficie.fill(self.cor)
        self.rect = self.superficie.get_rect(bottomleft = (self.x, self.y))
        self.image = self.superficie
        self.distancia = 0

    @abstractmethod
    def update(self):
        pass

