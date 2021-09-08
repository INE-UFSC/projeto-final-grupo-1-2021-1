import pygame

class Caixa(pygame.sprite.Sprite):
    def __init__(self, altura: int, largura: int, x, y, forca_necessaria):
        pygame.sprite.Sprite.__init__(self)
        self.__altura = altura
        self.__largura = largura
        self.__forca_necessaria = forca_necessaria
        self.__x = x
        self.__y = y

        self.__index_imagem = 0
        self.__imgs = []
        for i in range(0, 9):
            self.__imgs.append(
                pygame.transform.smoothscale(
                    pygame.image.load(f'images/caixa-{i}.png').convert_alpha(), 
                    (self.__largura, self.__altura))
            )

        self.__image = pygame.transform.smoothscale(self.__imgs[self.__index_imagem], (self.__largura, self.__altura))
        self.__rect = self.__image.get_rect()
        self.__rect.bottomleft = (x, y)
        self.__quebrada = False

        self.__ultimo_update = pygame.time.get_ticks()
        self.__taxa_atualizacao = 60
    
    @property
    def rect(self):
        return self.__rect
    
    @property
    def forca_necessaria(self):
        return self.__forca_necessaria

    @property
    def image(self):
        return self.__image
    
    def quebrar(self):
        self.__quebrada = True
    
    def estado_inicial(self):
        self.__quebrada = False
        self.__index_imagem = 0
    
    def animacao_quebrar(self):
        agora = pygame.time.get_ticks()

        if self.__quebrada and (agora - self.__ultimo_update > self.__taxa_atualizacao):
            self.__ultimo_update = agora
            self.__index_imagem += 1

            if self.__index_imagem >= 8:
                self.__index_imagem = 8
        
        self.__image = pygame.transform.smoothscale(self.__imgs[self.__index_imagem], (self.__largura, self.__altura))
    
    def update(self, resetar = False):
        if resetar:
            self.estado_inicial()

        self.animacao_quebrar()
