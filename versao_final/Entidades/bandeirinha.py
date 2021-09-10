import pygame

class Bandeirinha(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.__altura = 120
        self.__largura = 70
        self.__x = x
        self.__y = y
        
        self.__index_imagem = 0
        self.__imgs = []
        for i in range(0,5):
            self.__imgs.append(
                pygame.transform.smoothscale(
                    pygame.image.load(f'images/bandeirinha-{i}.png').convert_alpha(), 
                    (self.__largura, self.__altura))
            )
        self.__image = pygame.transform.smoothscale(self.__imgs[self.__index_imagem], (self.__largura, self.__altura))
        self.__rect = self.__image.get_rect()
        self.__rect.bottomleft = (x, y)
    
    @property
    def rect(self):
        return self.__rect
    
    @property
    def image(self):
        return self.__image

    def update(self):
        self.__index_imagem += 0.2
        if self.__index_imagem >= len(self.__imgs):
            self.__index_imagem = 0
        self.__image = pygame.transform.smoothscale(self.__imgs[int(self.__index_imagem)], (self.__largura, self.__altura))