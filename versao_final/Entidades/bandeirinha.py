import pygame

class Bandeirinha(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.altura = 100
        self.largura = 30
        self.x = x
        self.y = y
        self.superficie = pygame.Surface((self.largura, self.altura))
        self.superficie.fill('Green')
        self.rect = self.superficie.get_rect(bottomleft = (self.x, self.y))
        self.image = self.superficie