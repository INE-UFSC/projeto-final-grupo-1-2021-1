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

    plataforma1 = []
    x = 4125
    for i in range(6):
      plataforma1.append(Bloco(x, 380))
      x += 50
    
    coluna1 = []
    y = 80
    for i in range(7):
      coluna1.append(Bloco(4425, y))
      y += 50

    coluna2 = []
    y = 70
    for i in range(8):
      coluna2.append(Bloco(4740, y))
      y += 50
    
    coluna3 = []
    y = 30
    for i in range(5):
      coluna3.append(Bloco(6235, y))
      y += 50
    
    coluna4 = []
    y = 30
    for i in range(5):
      coluna4.append(Bloco(6685, y))
      y += 50
    
    plataforma2 = []
    x = 6285
    for i in range(8):
      plataforma2.append(Bloco(x, 30))
      x += 50

    plataforma3 = []
    x = 7280
    for i in range(18):
      plataforma2.append(Bloco(x, 70))
      x += 50
    
    coluna5 = []
    y = 120
    for i in range(6):
      coluna5.append(Bloco(7280, y))
      y += 50

    coluna6 = []
    y = 120
    for i in range(6):
      coluna6.append(Bloco(8180, y))
      y += 50

    self.__blocos_nivel_3 = [
        Bloco(710, 195), Bloco(1315, 305), Bloco(2380, 125), Bloco(2430, 125), Bloco(2480, 125),
        Bloco(3135, 320), Bloco(3135, 370), Bloco(3135, 420), Bloco(3355, 320), Bloco(4475, 230),
        Bloco(4690,120), Bloco(4690, 320), Bloco(4975, 180), Bloco(5170, 295),
        Bloco(5630, 420), Bloco(5630, 370), Bloco(5630, 320), Bloco(5630, 235), Bloco(5630, 185),
        Bloco(5630, 135), Bloco(6285, 280), Bloco(6285, 330), Bloco(6395, 330),
        Bloco(6395, 280), Bloco(6520, 280), Bloco(6520, 330), Bloco(6635, 280), Bloco(6635, 330),
        Bloco(6385, 120), Bloco(6535, 120), Bloco(8230, 320), *plataforma1, *coluna1, *coluna2,
        *coluna3, *coluna4, *plataforma2, *plataforma3, *coluna5, *coluna6
    ]

    self.__caixas_nivel_3 = [
        Caixa(40,40,430,430,40), Caixa(40,40,575,315,40), Caixa(275,110,925,195,100), Caixa(40,40,1183,153,40),
        Caixa(30,30,1358,120,20), Caixa(40,40,1600,190,40), Caixa(30,30,1805,95,20), Caixa(40,40,2075,220,40),
        Caixa(40,40,2865,225,40), Caixa(40,40,3620,295,40), Caixa(40,40,3860,375,40), Caixa(50,50,5630,85,50),
        Caixa(35,50,5630,285,30)
    ]

    self.__pilulas_nivel_3 =[ 
      Pilula('blue', -10, False, 20, 430), Pilula('blue', -10, False, 1370, 400), Pilula('blue', -10, False, 1340, 260),
      Pilula('red', 10, False, 3410, 155), Pilula('red', 10, False, 6055, 420), Pilula('green', -10, True, 6410, 100),
      Pilula('red', 10, False, 7225, 430), Pilula('red', 10, False, 7385, 430), Pilula('blue', -10, False, 7620, 255),
      Pilula('blue', -10, False, 8410, 285), Pilula('blue', -10, False, 8685, 295)
    ]

    self.__inimigos_nivel_3 = [ 
      InimigoLaranja(1050, 470, 230), InimigoVermelho(1350, 470, 340,-13), InimigoLaranja(1730,470, 235) ,InimigoVermelho(2035,470,315,-15), InimigoVermelho(2390,470,270),
      InimigoLaranja(2700, 470, 265), InimigoLaranja(3250, 470, 320), InimigoLaranja(3640, 470, 290), InimigoVermelho(4150, 380, 160),
      InimigoLaranja(4415,80,0, velocidade= 0), InimigoVermelho(4810, 470, 325), InimigoLaranja(5175, 470, 385), InimigoVermelho(5710, 470, 450),
      InimigoLaranja(6200, 470, 540), InimigoLaranja(6810, 470, 295), InimigoVermelho(7410, 470, 295, -24), InimigoVermelho(7745,470,395,-24),
      InimigoVermelho(9150,470, 240), InimigoVermelho(8350, 470, 600, -30, "bossV", largura=150, altura=150)
    ]

    self.__nivel_3 = Nivel(self.__background_nivel_3, self.__bandeirinha_nivel_3, self.__pilulas_nivel_3 , self.__caixas_nivel_3 , self.__inimigos_nivel_3 , self.__blocos_nivel_3)

  def carregar_niveis(self):
    self.carregar_nivel_1()
    self.carregar_nivel_2()
    self.carregar_nivel_3()
