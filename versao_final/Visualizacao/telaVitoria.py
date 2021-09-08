import pygame
import constantes as c
from Visualizacao.visualizacaoBase import VisualizacaoBase

class TelaVitoria(VisualizacaoBase):
  def __init__(self, niveis):
    super().__init__()
    self.__niveis = niveis
    self.__background = pygame.image.load('images/vitoria.png').convert()
    self.__tecla_pressionada = False
    self.__primeira_aparicao = True

    self.__continuacao = "Pressione espaço para voltar a tela inicial"
    self.__superficie_texto_continuacao = self.fonte.render(self.__continuacao, True, (0, 0, 0))

    self.__texto_tempo = "Tempo total"
    self.__superficie_texto_tempo = self.fonte_titulo.render(self.__texto_tempo, True, (0, 0, 0))

    self.__tempo = "300 segundos"
    self.__superficie_tempo = self.fonte.render(self.__tempo, True, (0, 0, 0))

    self.__tempo_niveis = "Tempos"
    self.__superficie_tempo_niveis = self.fonte_titulo.render(self.__tempo_niveis, True, (0, 0, 0))

    self.__tempo_nivel_1 = f"Fase 1: {self.__niveis[0].tempo} s"
    self.__superficie_nivel_1 = self.fonte.render(self.__tempo_nivel_1, True, (0, 0, 0))

    self.__tempo_nivel_2 = f"Fase 2: {self.__niveis[1].tempo} s"
    self.__superficie_nivel_2 = self.fonte.render(self.__tempo_nivel_2, True, (0, 0, 0))

    self.__tempo_nivel_3 = f"Fase 3: {self.__niveis[2].tempo} s"
    self.__superficie_nivel_3 = self.fonte.render(self.__tempo_nivel_3, True, (0, 0, 0))
  
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
    self.__tempo_nivel_1 = f"Fase 1: {self.__niveis[0].tempo} s"
    self.__superficie_nivel_1 = self.fonte.render(self.__tempo_nivel_1, True, (0, 0, 0))

    self.__tempo_nivel_2 = f"Fase 2: {self.__niveis[1].tempo} s"
    self.__superficie_nivel_2 = self.fonte.render(self.__tempo_nivel_2, True, (0, 0, 0))

    self.__tempo_nivel_3 = f"Fase 3: {self.__niveis[2].tempo} s"
    self.__superficie_nivel_3 = self.fonte.render(self.__tempo_nivel_3, True, (0, 0, 0))

    total = 0
    for nivel in self.__niveis:
      total += nivel.tempo
    self.__tempo = f"{total} segundos"
    self.__superficie_tempo = self.fonte.render(self.__tempo, True, (0, 0, 0))