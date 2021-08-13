import pygame
from inimigo import Inimigo

class InimigoLaranja(Inimigo):
    def __init__(self, x, y, cor = "Orange", velocidade = 7, largura = 30, altura = 70):
        super().__init__(cor, velocidade, largura, altura, x, y)

    def andar(self):
        pass
