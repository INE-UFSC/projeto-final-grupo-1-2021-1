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
        Caixa(50, 50, 1300, 420, 40), Caixa(75, 50, 1890, 245, 40),
        Caixa(50, 50, 2645, 175, 50), Caixa(50, 50, 2695, 175, 50),
        Caixa(50, 50, 3155, 175, 10), Caixa(50, 50, 3255, 175, 50),
        Caixa(50, 50, 3730, 420, 30), Caixa(50, 50, 3990, 100, 50),
        Caixa(50, 50, 4105, 100, 50), Caixa(50, 50, 6080, 165, 50),
        Caixa(50, 50, 6200, 165, 50), Caixa(30, 30, 4950, 230, 10),
        *coluna_caixas_grandes,
    ]
    self.__inimigos_nivel_1 = [
        InimigoVermelho(865, 470, distancia_maxima=350), InimigoVermelho(3784, 270),
        InimigoVermelho(5970, 390, distancia_maxima=450, pulo=-15),
        InimigoVermelho(4710, 470, distancia_maxima=600, pulo=-17),
        InimigoLaranja(2705, 470), InimigoLaranja(3070, 470, velocidade=8),
        InimigoLaranja(5665, 390, distancia_maxima=170, velocidade=5),
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
        Pilula('blue',-10, False, 4968, 180),
        Pilula('green',-10, True, 1540, 425),
        Pilula('green',-10, True, 2435, 405),
        *fila_pilulas_vermelhas,
    ]

    plataforma = []
    x = 5510
    for i in range(21):
      plataforma.append(Bloco(x, 390))
      x += 50
    
    coluna = []
    y = 240
    for i in range(3):
      coluna.append(Bloco(6460, y))
      y += 50

    self.__blocos_nivel_1 = [
        Bloco(825, 325), Bloco(1890, 95), Bloco(1890, 145), Bloco(1890, 195),
        Bloco(1890, 320), Bloco(1940, 320), Bloco(1990, 370), Bloco(2040, 420),
        Bloco(2675, 290), Bloco(2595, 175), Bloco(2745, 175), Bloco(2885, 175),
        Bloco(3205, 175), Bloco(3305, 175), Bloco(3230, 290), Bloco(3730, 270),
        Bloco(3730, 320), Bloco(3730, 370), Bloco(3780, 270), Bloco(3830, 270),
        Bloco(3880, 270), Bloco(3930, 270), Bloco(3980, 270), Bloco(4030, 270),
        Bloco(4080, 270), Bloco(4130, 270), Bloco(4180, 270), Bloco(4230, 270),
        Bloco(4280, 220), Bloco(4330, 170), Bloco(4380, 120), Bloco(4430, 120),
        Bloco(4480,120), Bloco(4530, 120),
        *plataforma, Bloco(5610, 340), Bloco(5910, 340), Bloco(5740, 140), Bloco(5790, 165),
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
    self.__background_nivel_2 = 'images/fase2.png'
    self.__bandeirinha_nivel_2 = Bandeirinha(c.bandeirinha, 158)

    plataforma_caixas = []
    x = 3610
    for i in range(3):
      plataforma_caixas.append(Caixa(30, 30, x, 113, 10))
      x += 50

    coluna_blocos1 = []
    coluna_blocos2 = []
    y = 320
    for i in range(3):
      coluna_blocos1.append(Bloco(810, y))
      coluna_blocos2.append(Bloco(2125, y))
      y += 50

    coluna_blocos3 = []
    coluna_blocos4 = []
    y = 250
    for i in range(2):
      coluna_blocos3.append(Bloco(2685, y))
      coluna_blocos4.append(Bloco(2815, y))
      y += 50

    plataforma_blocos1 = []
    x = 2840
    for i in range(4):
      plataforma_blocos1.append(Bloco(x, 350))
      x += 50

    plataforma_blocos2 = []
    plataforma_blocos3 = []
    x1 = 3140
    x2 = 3540
    for i in range(6):
      plataforma_blocos2.append(Bloco(x1, 201))
      plataforma_blocos3.append(Bloco(x2, 331))
      x1 += 50
      x2 += 50

    plataforma_blocos4 = []
    plataforma_blocos5 = []
    x1 = 3990
    x2 = 4295
    for i in range(5):
      plataforma_blocos4.append(Bloco(x1, 133))
      plataforma_blocos5.append(Bloco(x2, 133))
      x1 += 50
      x2 += 50

    plataforma_blocos6 = []
    x = 4595
    for i in range(4):
      plataforma_blocos6.append(Bloco(x, 133))
      x += 50

    plataforma_blocos7 = []
    x = 3955
    for i in range(12):
      plataforma_blocos7.append(Bloco(x, 355))
      x += 50

    escada_blocos1 = []
    escada_blocos2 = []
    x1 = 5125
    y1 = 420
    x2 = 5805
    y2 = 120
    for i in range(7):
      escada_blocos1.append(Bloco(x1, y1))
      escada_blocos2.append(Bloco(x2, y2))
      x1 += 50
      y1 -= 50
      x2 += 50
      y2 += 50

    coluna_blocos5 = []
    coluna_blocos6 = []
    y = 120
    for i in range(4):
      coluna_blocos5.append(Bloco(5475, y))
      coluna_blocos6.append(Bloco(5755, y))
      y += 50

    coluna_blocos7 = []
    coluna_blocos8 = []
    y = 320
    for i in range(3):
      coluna_blocos7.append(Bloco(6400, y))
      coluna_blocos8.append(Bloco(8070, y))
      y += 50

    plataforma_blocos8 = []
    x = 7050
    for i in range(8):
      plataforma_blocos8.append(Bloco(x, 234))
      x += 50

    plataforma_blocos9 = []
    x = 9420
    for i in range(4):
      plataforma_blocos9.append(Bloco(x, 158))
      x += 50

    self.__caixas_nivel_2 = [
      Caixa(30, 30, 1140, 112, 5), Caixa(30, 30, 1695, 105, 5), Caixa(50, 50, 3205, 420, 10), Caixa(50, 50, 3860, 420, 50),
      Caixa(50, 50, 4645, 420, 50), Caixa(30, 30, 6470, 215, 30), Caixa(30, 30, 6605, 96, 30), Caixa(30, 30, 6775, 220, 30),
      Caixa(30, 30, 6930, 136, 30), Caixa(30, 30, 7100, 63, 30), Caixa(30, 30, 7325, 50, 30), Caixa(30, 30, 6470, 215, 30),
      Caixa(30, 30, 7510, 125, 30), Caixa(30, 30, 7690, 163, 30), Caixa(30, 30, 7880, 122, 30), Caixa(40, 40, 8630, 430, 40),
      Caixa(40, 40, 8735, 345, 40), Caixa(40, 40, 8845, 276, 40),*plataforma_caixas
    ]

    self.__blocos_nivel_2 =[
      Bloco(900, 246), Bloco(1025, 179), Bloco(1240, 192), Bloco(1390, 217),
      Bloco(1520, 138), Bloco(1790, 194), Bloco(1990, 141), Bloco(2440, 420),
      Bloco(2505, 360), Bloco(2565, 304), Bloco(2635, 250), Bloco(3040, 300),
      Bloco(3090, 250), Bloco(3105, 420),Bloco(3440, 231), Bloco(3490, 281), 
      Bloco(3840, 280), Bloco(3155, 370), Bloco(3205, 320), Bloco(3360, 320),
      Bloco(3410, 370), Bloco(3460, 420),Bloco(3890, 231), Bloco(3940, 182), 
      Bloco(4555, 305), Bloco(4605, 256),Bloco(4655, 256), Bloco(4705, 302),
      Bloco(4755, 350), Bloco(9050, 190),Bloco(9320, 158), *plataforma_blocos1, 
      *plataforma_blocos2, *plataforma_blocos3, *plataforma_blocos4, *plataforma_blocos5, 
      *plataforma_blocos6, *plataforma_blocos7, *plataforma_blocos8, *plataforma_blocos9, 
      *coluna_blocos1, *coluna_blocos2, *coluna_blocos3, *coluna_blocos4, *coluna_blocos5, 
      *coluna_blocos6, *coluna_blocos7, *coluna_blocos8, *escada_blocos1, *escada_blocos2
    ]

    self.__pilulas_nivel_2 = [
      Pilula('red', 10, False, 1192, 430), Pilula('red', 10, False, 1430, 150), 
      Pilula('red', 10, False, 1606, 418), Pilula('blue', -10, False, 2149, 271), 
      Pilula('green', -10, True, 2652, 317), Pilula('blue', -10, False, 3007, 284),
      Pilula('blue', -10, False, 3182, 435), Pilula('blue', -10, False, 3687, 74),
      Pilula('red', 10, False, 4133, 301), Pilula('red', 10, False, 4227, 265),
      Pilula('blue', -10, False, 4304, 423), Pilula('blue', -10, False, 4415, 80),
      Pilula('blue', -10, False, 5213, 440), Pilula('green', -10, True, 5630, 208),
      Pilula('green', -10, True, 7320, 197), Pilula('red', 10, False, 8080, 277),
      Pilula('red', 10, False, 8319, 415)

    ]

    self.__inimigos_nivel_2 = [
      InimigoVermelho(866, 470, 400), InimigoLaranja(1260, 470, 400), InimigoVermelho(1705, 470, 380),
      InimigoLaranja(2499, 470, 280), InimigoVermelho(3132, 200, 280), InimigoLaranja(3539, 330, 250),
      InimigoVermelho(4002, 355, 480), InimigoLaranja(4281, 135, 180), InimigoLaranja(5226, 470, 340),
      InimigoVermelho(5600, 470, 330), InimigoVermelho(6445, 470, 430), InimigoVermelho(6913, 470, 500), 
      InimigoLaranja(7452, 470, 500), InimigoLaranja(7047, 235, 300), InimigoLaranja(8689, 470, 200),
      InimigoLaranja(8941, 470, 600,  largura=150, altura=150, mutante=True)
    ]

    self.__nivel_2 = Nivel(
      self.__background_nivel_2,
      self.__bandeirinha_nivel_2,
      self.__pilulas_nivel_2,
      self.__caixas_nivel_2,
      self.__inimigos_nivel_2,
      self.__blocos_nivel_2
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
      InimigoVermelho(9150,470, 240), InimigoVermelho(8350, 470, 600, -22, largura=150, altura=150, mutante=True)
    ]

    self.__nivel_3 = Nivel(self.__background_nivel_3, self.__bandeirinha_nivel_3, self.__pilulas_nivel_3 , self.__caixas_nivel_3 , self.__inimigos_nivel_3 , self.__blocos_nivel_3)

  def carregar_niveis(self):
    self.carregar_nivel_1()
    self.carregar_nivel_2()
    self.carregar_nivel_3()
