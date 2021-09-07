from Entidades.bandeirinha import Bandeirinha
from Entidades.bandeirinha import Bandeirinha
from Entidades.pilula import Pilula
from Entidades.caixa import Caixa
from Entidades.bloco import Bloco
from Entidades.inimigoVermelho import InimigoVermelho
from Entidades.inimigoLaranja import InimigoLaranja
from Entidades.nivel import Nivel
from Entidades.botao import Botao
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
    self.__caixas_nivel_1 = [
        Caixa(150, 50, 1900, 470, 2),
        Caixa(50, 50, 2230, 470, 40),
    ]
    self.__inimigos_nivel_1 = [
        InimigoVermelho(700, 470),
        InimigoVermelho(2675, 470),
        InimigoLaranja(1535, 470)
    ]
    self.__pilulas_nivel_1 = [
        Pilula('red', 10, False, 675, 450),
        Pilula('blue',-10, False, 866, 250),
        Pilula('blue',-10, False, 1482, 430),
        Pilula('green',-10, True, 1918, 290),
        Pilula('red', 10, False, 2385, 450),
    ]
    self.__blocos_nivel_1 = [
        Bloco(50, 50, 807, 255),
        Bloco(50, 50, 891, 255),
        Bloco(50, 50, 1036, 470),
        Bloco(100, 50, 1086, 470),
        Bloco(100, 50, 1150, 470),
        Bloco(50, 50, 1200, 470),
        Bloco(50, 50, 2280, 420)

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
      Caixa(50, 50, 600, 470, 40),
      Caixa(100, 50, 700, 470, 40),
      Caixa(150, 50, 800, 470, 40),
      Caixa(50, 100, 900, 470, 40),
      Caixa(200, 100, 1100, 470, 55),
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
