import pygame
import constantes as c
from Visualizacao.visualizacaoBase import VisualizacaoBase

class TelaTransicaoNivel(VisualizacaoBase):
  def __init__(self):
    self.__background = pygame.image.load('images/fase_concluida.png').convert()
    self.__tecla_pressionada = False

    self.__fonte = pygame.font.SysFont('Roboto', 30)
    self.__texto = ""
    self.__continuacao = "Pressione espaço para continuar"
    self.__superficie_texto = self.__fonte.render(self.__texto, True, (0, 0, 0))
    self.__superficie_texto_continuacao = self.__fonte.render(self.__continuacao, True, (0, 0, 0))
  
  def update(self, screen):
    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE] and not self.__tecla_pressionada:
      self.__tecla_pressionada = True
      return True
    
    if not keys[pygame.K_SPACE]:
      self.__tecla_pressionada = False
    
    screen.blit(self.__background, (0, 0))
    screen.blit(self.__superficie_texto,(c.largura_tela/2 - self.__superficie_texto.get_rect().width/2, 410))
    screen.blit(self.__superficie_texto_continuacao,(c.largura_tela/2 - self.__superficie_texto_continuacao.get_rect().width/2, 440))
  
  def atualiza_texto(self, texto):
    self.__texto = texto
    self.__superficie_texto = self.__fonte.render(self.__texto, True, (0, 0, 0))
