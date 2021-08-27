import pygame

class Bloco(pygame.sprite.Sprite):
    def __init__(self, altura: int, largura: int, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.altura = altura
        self.largura = largura
        self.x = x
        self.y = y
        self.superficie = pygame.Surface((self.largura, self.altura))
        self.superficie.fill('Black')
        self.rect = self.superficie.get_rect(bottomleft = (self.x, self.y))
        self.image = self.superficie