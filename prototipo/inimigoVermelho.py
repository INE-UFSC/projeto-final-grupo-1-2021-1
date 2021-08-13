import pygame
from inimigo import Inimigo

class InimigoVermelho(Inimigo):
    def __init__(self, x, y, pulo = -10, cor = "Red", velocidade = 2, largura = 70, altura = 50):
        super().__init__(cor, velocidade, largura, altura, x, y)
        self.pulo = pulo

    def andar(self):
        pass

