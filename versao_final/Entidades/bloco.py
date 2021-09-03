import pygame

class Bloco(pygame.sprite.Sprite):
    def __init__(self, altura: int, largura: int, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.__altura = altura
        self.__largura = largura
        self.__x = x
        self.__y = y
        self.__superficie = pygame.Surface((self.__largura, self.__altura))
        self.__superficie.fill('Black')
        self.__rect = self.__superficie.get_rect(bottomleft = (self.__x, self.__y))
        self.__image = self.__superficie
    
    @property
    def rect(self):
        return self.__rect

    @property
    def image(self):
        return self.__image