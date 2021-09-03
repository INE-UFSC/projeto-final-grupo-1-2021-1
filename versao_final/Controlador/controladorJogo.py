import pygame
from Entidades.jogador import Jogador
import constantes as c

class ControladorJogo:
  def __init__(self, tela, niveis):
    self.__jogador = Jogador()
    self.__niveis = niveis
    self.__index_nivel_atual = 0
    self.__nivel = niveis[self.__index_nivel_atual]
    self.__tela = tela
    self.__running = True
    self.__relogio = pygame.time.Clock()
    self.__canvas = pygame.Surface((c.largura_background, c.altura_background))

    for nivel in self.__niveis:
      nivel.inserir_jogador(self.__jogador)

  def passar_nivel(self):
    self.__index_nivel_atual += 1
    if self.__index_nivel_atual == len(self.__niveis):
      self.__index_nivel_atual = 0
    self.__nivel = self.__niveis[self.__index_nivel_atual]
    self.__nivel.reset()
  
  def iniciar(self):
    while self.__running:
      self.__relogio.tick(60)

      for event in pygame.event.get():
          if event.type == pygame.QUIT:
            self.__running = False

          #Passa de nível quando aperta-se k, é obviamente provisório, só para ver se funciona
          if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_k:
              self.passar_nivel()

      if self.__nivel.bandeirinha.rect.colliderect(self.__jogador.rect.x , self.__jogador.rect.y , self.__jogador.tamanho, self.__jogador.tamanho):
        self.passar_nivel()

      
      self.__nivel.update(self.__canvas)
      self.__tela.blit(self.__canvas,(self.__nivel.camera.offset.x, 0))

      pygame.display.update()