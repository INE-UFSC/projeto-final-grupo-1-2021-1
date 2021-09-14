from pickle import STRING
from Entidades.RankingDAO import RankingDAO
import pygame
import constantes as c
from Visualizacao.visualizacaoBase import VisualizacaoBase

class TelaRanking(VisualizacaoBase):
  def __init__(self):
    super().__init__()
    self.__ranking_dao = RankingDAO()
    self.__background = pygame.image.load('images/ranking.png').convert()
    self.__tecla_pressionada = True
    self.__continuacao = "Pressione espaço para voltar a tela inicial"
    self.__superficie_texto_continuacao = self.fonte.render(self.__continuacao, True, (255, 255, 255))
    self.__primeira_aparicao = True
  
  def update(self, screen):
    if self.__primeira_aparicao:
      self.pegar_ranking()
      self.__primeira_aparicao = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE] and not self.__tecla_pressionada:
      self.__tecla_pressionada = True
      self.__primeira_aparicao = True
      return True
    
    if not keys[pygame.K_SPACE]:
      self.__tecla_pressionada = False
    
    screen.blit(self.__background, (0, 0))
    screen.blit(self.__superficie_texto_continuacao,(c.largura_tela/2 - self.__superficie_texto_continuacao.get_rect().width/2, 470))

    posicao = 188
    for tempo in self.__tempos:
      tempo_texto = f'{tempo} s' if tempo != None else '-'
      superficie_texto = self.fonte.render(f'{tempo_texto}', True, (0, 0, 0))
      screen.blit(superficie_texto, (c.largura_tela/2 - superficie_texto.get_rect().width/2, posicao))
      posicao += 52

  def pegar_ranking(self):
    self.__ranking = self.__ranking_dao.ranking()
    self.atualizar_textos()
  
  def atualizar_textos(self):
    tempos = [None] * 5

    for index, tempo in enumerate(self.__ranking):
      tempos[index] = tempo
    
    self.__tempos = tempos
