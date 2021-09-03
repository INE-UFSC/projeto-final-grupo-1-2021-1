import pygame
from abc import ABC, abstractmethod

class Inimigo(ABC, pygame.sprite.Sprite):
    def __init__(self, cor, velocidade, largura, altura, x, y, distancia_maxima):
        pygame.sprite.Sprite.__init__(self)
        self.__cor = cor
        self.__velocidade = velocidade
        self.__largura = largura
        self.__altura = altura
        self.__distancia_maxima = distancia_maxima
        self.__x = x
        self.__y = y
        self.__superficie = pygame.Surface((self.__largura, self.__altura))
        self.__superficie.fill(self.__cor)
        self.__rect = self.__superficie.get_rect(bottomleft = (self.__x, self.__y))
        self.__image = self.__superficie
        self.__distancia = 0
    
    @property
    def y(self):
        return self.__y
    
    @property
    def altura(self):
        return self.__altura
    
    @property
    def image(self):
        return self.__image

    @property
    def rect(self):
        return self.__rect
    
    @rect.setter
    def rect(self, valor):
        self.__rect = valor
    
    @property
    def distancia(self):
        return self.__distancia
    
    @distancia.setter
    def distancia(self, valor):
        self.__distancia = valor
    
    @property
    def distancia_maxima(self):
        return self.__distancia_maxima
    
    @property
    def velocidade(self):
        return self.__velocidade
    
    @velocidade.setter
    def velocidade(self, valor):
        self.__velocidade = valor

    @abstractmethod
    def update(self):
        pass

