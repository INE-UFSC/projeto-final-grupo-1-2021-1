from Visualizacao.visualizacaoBase import VisualizacaoBase
import pygame
from Entidades.camera import Camera
from Entidades.botao import Botao

class Nivel(VisualizacaoBase):
  def __init__(self, background, bandeirinha, pilulas = [], caixas = [], inimigos = [], blocos = []):
    self.__pilulas = pilulas
    self.__caixas = caixas
    self.__inimigos = inimigos
    self.__blocos = blocos
    self.__bandeirinha = bandeirinha
    self.__botao_reset = Botao(750, 5,'images/restart.png')
    self.__background = pygame.image.load(background).convert()

    self.__grupo_pilulas = pygame.sprite.Group()
    self.__grupo_caixas = pygame.sprite.Group()
    self.__grupo_caixas_quebradas = pygame.sprite.Group()
    self.__grupo_inimigos = pygame.sprite.Group()
    self.__grupo_blocos = pygame.sprite.Group()
    self.__grupo_bandeirinha = pygame.sprite.Group()
    self.__grupo_botoes = pygame.sprite.Group()

    self.__grupo_pilulas.add(self.__pilulas)
    self.__grupo_caixas.add(self.__caixas)
    self.__grupo_inimigos.add(self.__inimigos)
    self.__grupo_blocos.add(self.__blocos)
    self.__grupo_bandeirinha.add(self.__bandeirinha)
    self.__grupo_botoes.add(self.__botao_reset)
  
  @property
  def bandeirinha(self):
    return self.__bandeirinha
  
  @property
  def camera(self):
    return self.__camera
  
  def inserir_jogador(self, jogador):
    self.__jogador = jogador
    self.__camera = Camera(self.__jogador)

  def reset(self):
    self.__grupo_pilulas.empty()
    self.__grupo_caixas.empty()
    self.__grupo_inimigos.empty()
    self.__grupo_blocos.empty()
    self.__grupo_botoes.empty()

    self.__grupo_pilulas.add(self.__pilulas)
    self.__grupo_caixas.add(self.__caixas)
    self.__grupo_inimigos.add(self.__inimigos)
    self.__grupo_blocos.add(self.__blocos)
    self.__grupo_botoes.add(self.__botao_reset)

    self.__jogador.reset()
    self.__camera.reset()
  
  def update(self, screen):
    self.__jogador.update(self.__grupo_caixas, self.__grupo_pilulas, self.__grupo_blocos, self.__grupo_caixas_quebradas)
    self.__camera.scroll()

    self.__grupo_inimigos.update()
    self.__grupo_caixas_quebradas.update()
    self.__grupo_botoes.update(self.__camera)
    
    if pygame.sprite.spritecollide(self.__jogador, self.__grupo_inimigos, False):
      self.reset()
    
    if self.__bandeirinha.rect.colliderect(self.__jogador.rect.x , self.__jogador.rect.y , self.__jogador.tamanho, self.__jogador.tamanho):
      return True # Jogador concluiu nível
    
    screen.blit(self.__background, (0, 0))
    screen.blit(self.__jogador.superficie, (self.__jogador.rect.x, self.__jogador.rect.y))
    
    if self.__botao_reset.interage() == True: #tenho que descobrir uma forma de deixar essa linha melhor e utilizável para mais botões
      self.reset()

    self.__grupo_pilulas.draw(screen)
    self.__grupo_inimigos.draw(screen)
    self.__grupo_caixas.draw(screen)
    self.__grupo_caixas_quebradas.draw(screen)
    self.__grupo_blocos.draw(screen)
    self.__grupo_bandeirinha.draw(screen)
    self.__grupo_botoes.draw(screen)