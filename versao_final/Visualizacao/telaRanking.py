import pygame
import constantes as c
from Visualizacao.visualizacaoBase import VisualizacaoBase

class TelaRanking(VisualizacaoBase):
  def __init__(self):
    super().__init__()
    self.__background = pygame.image.load('images/ranking.png').convert()
    self.__tecla_pressionada = True
    self.__continuacao = "Pressione espaço para voltar a tela inicial"
    self.__superficie_texto_continuacao = self.fonte.render(self.__continuacao, True, (0, 0, 0))
  
  def update(self, screen):
    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE] and not self.__tecla_pressionada:
      self.__tecla_pressionada = True
      return True
    
    if not keys[pygame.K_SPACE]:
      self.__tecla_pressionada = False
    
    screen.blit(self.__background, (0, 0))
    screen.blit(self.__superficie_texto_continuacao,(c.largura_tela/2 - self.__superficie_texto_continuacao.get_rect().width/2, 440))
