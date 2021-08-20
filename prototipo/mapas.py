import pygame
from pilula import Pilula
from caixa import Caixa
from bloco import Bloco
from inimigoVermelho import InimigoVermelho
from inimigoLaranja import InimigoLaranja
from nivel import Nivel
import constantes as c

pygame.init()
pygame.display.set_caption("√ Variável")
tela_principal = pygame.display.set_mode((c.largura_tela, c.altura_tela))

background_nivel_1 = 'images/fase.png'
caixas_nivel_1 = [
    Caixa(50, 50, 550, 470, 40),
    Caixa(50, 50, 550, 250, 40),
    Caixa(200, 60, 1150, 470, 500)
]
inimigos_nivel_1 = [
    InimigoVermelho(600, 470),
    InimigoLaranja(100, 470)
]
pilulas_nivel_1 = [
    Pilula('red', 10, False, 500, 450),
    Pilula('blue',-10, False, 350, 450),
    Pilula('green',-10, True, 250, 450),
    Pilula('blue',-10, False, 200, 450),
    Pilula('red', 10, False, 575, 190),
    Pilula('red', 10, False, 575, 10),
]

blocos_nivel_1 = [
    Bloco(50, 50, 1000, 470 )

]

nivel_1 = Nivel(background_nivel_1, pilulas_nivel_1, caixas_nivel_1, inimigos_nivel_1, blocos_nivel_1)
nivel_2 = Nivel(background_nivel_1)

niveis = [nivel_1, nivel_2]