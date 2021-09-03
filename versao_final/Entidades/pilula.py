import pygame

class Pilula(pygame.sprite.Sprite):
    def __init__(self, cor, efeito, reseta_tamanho, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.__cor = cor 
        self.__efeito = efeito
        self.__reseta_tamanho = reseta_tamanho
        self.__x = x
        self.__y = y
        img = pygame.image.load(f'images/pilula_{self.__cor}.png')
        self.__image = pygame.transform.scale(img, (29 , 34))
        self.__rect = self.__image.get_rect()
        self.__rect.center = (x, y)
    
    @property
    def rect(self):
        return self.__rect
    
    @property
    def image(self):
        return self.__image
    
    @property
    def efeito(self):
        return self.__efeito
    
    @property
    def reseta_tamanho(self):
        return self.__reseta_tamanho