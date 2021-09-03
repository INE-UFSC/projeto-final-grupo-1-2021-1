import pygame
from Visualizacao.visualizacaoBase import VisualizacaoBase

class TelaVitoria(VisualizacaoBase):
  def __init__(self):
    self.__background = pygame.image.load('images/vitoria.png').convert()
    self.__tecla_pressionada = False
  
  def update(self, screen):
    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE] and not self.__tecla_pressionada:
      self.__tecla_pressionada = True
      return True
    
    if not keys[pygame.K_SPACE]:
      self.__tecla_pressionada = False
    
    screen.blit(self.__background, (0, 0))