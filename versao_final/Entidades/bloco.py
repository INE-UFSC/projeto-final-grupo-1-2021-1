import pygame

class Bloco(pygame.sprite.Sprite):
    def __init__(self, x, y, altura: int = 50, largura: int = 50):
        pygame.sprite.Sprite.__init__(self)
        self.__altura = altura
        self.__largura = largura
        self.__x = x
        self.__y = y
        self.__img = pygame.image.load(f'images/bloco.png')
        self.__image = pygame.transform.scale(self.__img, (self.__largura, self.__altura))
        self.__rect = self.__image.get_rect()
        self.__rect.topleft = (x, y)
    
    @property
    def rect(self):
        return self.__rect

    @property
    def image(self):
        return self.__image