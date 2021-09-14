import pygame
from Visualizacao.visualizacaoBase import VisualizacaoBase
import constantes as c

class TelaInicial(VisualizacaoBase):
  def __init__(self):
    super().__init__()
    self.__background = pygame.image.load('images/tela_inicial.png').convert()
    self.__tecla_pressionada = False

    self.__texto = "Pressione espaço para começar"
    self.__superficie_texto = self.fonte.render(self.__texto, True, (255, 255, 255))

  def update(self, screen):
    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE] and not self.__tecla_pressionada:
      self.__tecla_pressionada = True
      return True
    
    if not keys[pygame.K_SPACE]:
      self.__tecla_pressionada = False
    
    screen.blit(self.__background, (0, 0))
    screen.blit(self.__superficie_texto,(c.largura_tela/2 - self.__superficie_texto.get_rect().width/2, 440))