import pygame
import constantes as c

vec = pygame.math.Vector2

class Camera:
    def __init__(self, jogador):
      self.__jogador = jogador
      self.__offset = vec(0, 0)
      self.__posicao_antiga = self.__jogador.rect.x + self.__jogador.tamanho/2
      self.__borda = 0
    
    @property
    def offset(self):
      return self.__offset

    def scroll(self):
      if self.__jogador.rect.x + self.__jogador.tamanho/2 >= self.__posicao_antiga:
        self.__offset.x = -self.__jogador.rect.x + 400 - self.__jogador.tamanho/2
        self.__borda = self.__jogador.rect.x - c.largura_tela/2 + self.__jogador.tamanho/2
        self.__posicao_antiga = self.__jogador.rect.x + self.__jogador.tamanho/2
      elif self.__jogador.rect.x < self.__borda:
        self.__jogador.rect.x = self.__borda

      if self.__offset.x <= -c.borda_final:
        self.__offset.x = -c.borda_final
        self.__borda = -self.__offset.x

      if self.__jogador.rect.x > c.borda_final + c.largura_tela:
        self.__jogador.rect.x = c.borda_final + c.largura_tela

    def reset(self):
      self.__init__(self.__jogador)
  