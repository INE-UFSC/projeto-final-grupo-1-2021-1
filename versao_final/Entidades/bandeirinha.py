import pygame

class Bandeirinha(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.__altura = 100
        self.__largura = 30
        self.__x = x
        self.__y = y
        self.__superficie = pygame.Surface((self.__largura, self.__altura))
        self.__superficie.fill('Green')
        self.__rect = self.__superficie.get_rect(bottomleft = (self.__x, self.__y))
        self.__image = self.__superficie
    
    @property
    def rect(self):
        return self.__rect
    
    @property
    def image(self):
        return self.__image