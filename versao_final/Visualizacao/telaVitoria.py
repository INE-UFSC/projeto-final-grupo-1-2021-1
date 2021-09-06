import pygame
import constantes as c
from random import randint
from Visualizacao.visualizacaoBase import VisualizacaoBase

class TelaVitoria(VisualizacaoBase):
  def __init__(self, niveis):
    self.__niveis = niveis
    self.__background = pygame.image.load('images/vitoria.png').convert()
    self.__tecla_pressionada = False
    self.__primeira_aparicao = True

    self.__fonte_titulo = pygame.font.SysFont('Roboto', 30, bold=pygame.font.Font.bold)
    self.__fonte = pygame.font.SysFont('Roboto', 30)

    self.__continuacao = "Pressione espaço para voltar a tela inicial"
    self.__superficie_texto_continuacao = self.__fonte.render(self.__continuacao, True, (0, 0, 0))

    self.__texto_tempo = "Tempo total"
    self.__superficie_texto_tempo = self.__fonte_titulo.render(self.__texto_tempo, True, (0, 0, 0))

    self.__tempo = "300 segundos"
    self.__superficie_tempo = self.__fonte.render(self.__tempo, True, (0, 0, 0))

    self.__tempo_niveis = "Tempos"
    self.__superficie_tempo_niveis = self.__fonte_titulo.render(self.__tempo_niveis, True, (0, 0, 0))

    self.__tempo_nivel_1 = "Fase 1: 100 s"
    self.__superficie_nivel_1 = self.__fonte.render(self.__tempo_nivel_1, True, (0, 0, 0))

    self.__tempo_nivel_2 = "Fase 2: 105 s"
    self.__superficie_nivel_2 = self.__fonte.render(self.__tempo_nivel_2, True, (0, 0, 0))

    self.__tempo_nivel_3 = "Fase 3: 95 s"
    self.__superficie_nivel_3 = self.__fonte.render(self.__tempo_nivel_3, True, (0, 0, 0))
  
  def update(self, screen):
    if self.__primeira_aparicao:
      self.atualizar_tempos()
      self.__primeira_aparicao = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE] and not self.__tecla_pressionada:
      self.__tecla_pressionada = True
      self.__primeira_aparicao = True
      return True
    
    if not keys[pygame.K_SPACE]:
      self.__tecla_pressionada = False
    
    screen.blit(self.__background, (0, 0))
    screen.blit(self.__superficie_texto_continuacao,(c.largura_tela/2 - self.__superficie_texto_continuacao.get_rect().width/2, 440))

    screen.blit(self.__superficie_texto_tempo, (30, 175))
    screen.blit(self.__superficie_tempo, (30, 210))

    screen.blit(self.__superficie_tempo_niveis, (665, 175))
    screen.blit(self.__superficie_nivel_1, (630, 210))
    screen.blit(self.__superficie_nivel_2, (630, 240))
    screen.blit(self.__superficie_nivel_3, (630, 270))
  
  def atualizar_tempos(self):
    self.__tempo_nivel_1 = f"Fase 1: {randint(10, 200)} s"
    self.__superficie_nivel_1 = self.__fonte.render(self.__tempo_nivel_1, True, (0, 0, 0))

    self.__tempo_nivel_2 = f"Fase 2: {randint(10, 200)} s"
    self.__superficie_nivel_2 = self.__fonte.render(self.__tempo_nivel_2, True, (0, 0, 0))

    self.__tempo_nivel_3 = f"Fase 3: {randint(10, 200)} s"
    self.__superficie_nivel_3 = self.__fonte.render(self.__tempo_nivel_3, True, (0, 0, 0))