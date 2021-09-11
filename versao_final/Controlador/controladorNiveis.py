from Entidades.bandeirinha import Bandeirinha
from Entidades.bandeirinha import Bandeirinha
from Entidades.pilula import Pilula
from Entidades.caixa import Caixa
from Entidades.bloco import Bloco
from Entidades.inimigoVermelho import InimigoVermelho
from Entidades.inimigoLaranja import InimigoLaranja
from Entidades.nivel import Nivel
import constantes as c

class ControladorNiveis:
  def __init__(self):
    self.carregar_niveis()
    self.__niveis = [self.__nivel_1, self.__nivel_2, self.__nivel_3]
    self.__index_nivel_atual = 0
    self.__nivel_atual = self.__niveis[self.__index_nivel_atual]
  
  @property
  def nivel_atual(self):
    return self.__nivel_atual
  
  @property
  def index_nivel_atual(self):
    return self.__index_nivel_atual
  
  @property
  def niveis(self):
    return self.__niveis
  
  def eh_ultimo_nivel(self):
    return self.__index_nivel_atual == len(self.__niveis) - 1
  
  def pegar_proximo_nivel(self):
    self.__index_nivel_atual += 1
    if self.__index_nivel_atual == len(self.__niveis):
      self.__index_nivel_atual = 0
    self.__nivel_atual = self.__niveis[self.__index_nivel_atual]
    return self.__nivel_atual
  
  def carregar_nivel_1(self):
    self.__background_nivel_1 = 'images/fase1.png'
    self.__bandeirinha_nivel_1 = Bandeirinha(c.bandeirinha, 470)

    coluna_caixas_grandes = []
    caixa_y = 130
    for i in range(3):
      coluna_caixas_grandes.append(Caixa(100, 100, 8700, caixa_y, 70))
      caixa_y += 120

    self.__caixas_nivel_1 = [
        Caixa(50, 50, 1300, 420, 40), Caixa(75, 50, 1891, 247, 40),
        Caixa(50, 50, 2645, 173, 50), Caixa(50, 50, 2695, 173, 50),
        Caixa(50, 50, 3156, 173, 10), Caixa(50, 50, 3255, 173, 50),
        Caixa(50, 50, 3729, 420, 30), Caixa(50, 50, 3990, 100, 50),
        Caixa(50, 50, 4105, 100, 50), Caixa(50, 50, 6079, 167, 50),
        Caixa(50, 50, 6199, 167, 50), Caixa(30, 30, 4952, 228, 10),
        *coluna_caixas_grandes,
    ]
    self.__inimigos_nivel_1 = [
        InimigoVermelho(823, 470, 400), InimigoVermelho(3784, 270),
        InimigoVermelho(5966, 390, distancia_maxima=450, pulo=-15),
        InimigoVermelho(4710, 470, distancia_maxima=600, pulo=-20),
        InimigoLaranja(2705, 470), InimigoLaranja(3070, 470, velocidade=8),
        InimigoLaranja(5662, 390, distancia_maxima=170, velocidade=5),
        InimigoLaranja(4015, 270, distancia_maxima=200),
    ]

    fila_pilulas_vermelhas = []
    pilula_x = 6695
    for i in range(5):
      fila_pilulas_vermelhas.append(Pilula('red', 10, False, pilula_x, 430))
      pilula_x += 300

    self.__pilulas_nivel_1 = [
        Pilula('red', 10, False, 555, 420),
        Pilula('red', 10, False, 2650, 146),
        Pilula('red', 10, False, 2900, 126),
        Pilula('red', 10, False, 2985, 410),
        Pilula('red', 10, False, 3795, 218),
        Pilula('red', 10, False, 4307, 297),
        Pilula('red', 10, False, 5243, 432),
        Pilula('blue',-10, False, 735, 420),
        Pilula('blue',-10, False, 3920, 400),
        Pilula('blue',-10, False, 5798, 68),
        Pilula('blue',-10, False, 4977, 180),
        Pilula('green',-10, True, 1540, 425),
        Pilula('green',-10, True, 2435, 405),
        *fila_pilulas_vermelhas,
    ]

    plataforma = []
    x = 5507
    for i in range(21):
      plataforma.append(Bloco(x, 390))
      x += 50
    
    coluna = []
    y = 240
    for i in range(3):
      coluna.append(Bloco(6457, y))
      y += 50

    self.__blocos_nivel_1 = [
        Bloco(825, 325), Bloco(1891, 98), Bloco(1891, 148), Bloco(1891, 198),
        Bloco(1891, 321), Bloco(1941, 321), Bloco(1991, 370), Bloco(2041, 420),
        Bloco(2676, 290), Bloco(2595, 173), Bloco(2745, 173), Bloco(2883, 173),
        Bloco(3206, 173), Bloco(3305, 173), Bloco(3232, 290), Bloco(3729, 270),
        Bloco(3729, 320), Bloco(3729, 370), Bloco(3779, 270), Bloco(3829, 270),
        Bloco(3877, 270), Bloco(3927, 270), Bloco(3977, 270), Bloco(4027, 270),
        Bloco(4077, 270), Bloco(4127, 270), Bloco(4177, 270), Bloco(4227, 270),
        Bloco(4275, 222), Bloco(4322, 174), Bloco(4372, 126), Bloco(4421, 126),
        *plataforma, Bloco(5607, 340), Bloco(5907, 340), Bloco(5740, 141), Bloco(5790, 166),
        *coluna
    ]

    self.__nivel_1 = Nivel(
      self.__background_nivel_1,
      self.__bandeirinha_nivel_1,
      self.__pilulas_nivel_1,
      self.__caixas_nivel_1,
      self.__inimigos_nivel_1,
      self.__blocos_nivel_1
    )

  def carregar_nivel_2(self):
    self.__caixas_nivel_2 = [
      Caixa(50, 50, 600, 420, 40),
      Caixa(100, 50, 700, 370, 40),
      Caixa(150, 50, 800, 320, 40),
      Caixa(50, 100, 900, 420, 40),
      Caixa(200, 100, 1100, 270, 55),
    ]

    self.__bandeirinha_nivel_2 = Bandeirinha(c.bandeirinha, 470)
    self.__background_nivel_2 = 'images/fase2.png'
    self.__nivel_2 = Nivel(
      self.__background_nivel_2,
      self.__bandeirinha_nivel_2,
      caixas=self.__caixas_nivel_2
    )

  def carregar_nivel_3(self):
    self.__bandeirinha_nivel_3 = Bandeirinha(c.bandeirinha, 470)
    self.__background_nivel_3 = 'images/fase3.png'
    self.__nivel_3 = Nivel(self.__background_nivel_3, self.__bandeirinha_nivel_3)

  def carregar_niveis(self):
    self.carregar_nivel_1()
    self.carregar_nivel_2()
    self.carregar_nivel_3()
