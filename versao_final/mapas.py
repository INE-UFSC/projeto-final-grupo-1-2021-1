import pygame
from Entidades.bandeirinha import Bandeirinha
from Entidades.pilula import Pilula
from Entidades.caixa import Caixa
from Entidades.bloco import Bloco
from Entidades.inimigoVermelho import InimigoVermelho
from Entidades.inimigoLaranja import InimigoLaranja
from Entidades.nivel import Nivel
from Entidades.botao import Botao
import constantes as c

pygame.init()
pygame.display.set_caption("√ Variável")
tela_principal = pygame.display.set_mode((c.largura_tela, c.altura_tela))

#fase1
background_nivel_1 = 'images/fase1.png'
bandeirinha_nivel_1 = Bandeirinha(c.bandeirinha, 470)
caixas_nivel_1 = [
    Caixa(150, 50, 1900, 470, 100),
    Caixa(50, 50, 2230, 470, 40),
]
inimigos_nivel_1 = [
    InimigoVermelho(700, 470),
    InimigoVermelho(2675, 470),
    InimigoLaranja(1535, 470)
]
pilulas_nivel_1 = [
    Pilula('red', 10, False, 675, 450),
    Pilula('blue',-10, False, 866, 250),
    Pilula('blue',-10, False, 1482, 430),
    Pilula('green',-10, True, 1918, 290),
    Pilula('red', 10, False, 2385, 450),
]

blocos_nivel_1 = [
    Bloco(50, 50, 807, 255),
    Bloco(50, 50, 891, 255),
    Bloco(50, 50, 1036, 470),
    Bloco(100, 50, 1086, 470),
    Bloco(100, 50, 1150, 470),
    Bloco(50, 50, 1200, 470),
    Bloco(50, 50, 2280, 420)

]

botoes = [
    Botao(754,0,'images/restart.png')
]

#fase2
bandeirinha_nivel_2 = Bandeirinha(c.bandeirinha, 470)
background_nivel_2 = 'images/fase2.png'

#fase3
bandeirinha_nivel_3 = Bandeirinha(c.bandeirinha, 470)
background_nivel_3 = 'images/fase3.png'

nivel_1 = Nivel(background_nivel_1, bandeirinha_nivel_1, pilulas_nivel_1, caixas_nivel_1, inimigos_nivel_1, blocos_nivel_1, botoes= botoes)
nivel_2 = Nivel(background_nivel_2, bandeirinha_nivel_2, botoes= botoes)
nivel_3 = Nivel(background_nivel_3, bandeirinha_nivel_3, botoes=botoes)

niveis = [nivel_1, nivel_2, nivel_3]