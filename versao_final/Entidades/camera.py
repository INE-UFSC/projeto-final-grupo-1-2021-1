import pygame
vec = pygame.math.Vector2

class Camera:
    def __init__(self, jogador):
      self.__jogador = jogador
      self.__offset = vec(0, 0)
      self.__DISPLAY_W, self.__DISPLAY_H = 800, 500
      self.__posicao_antiga = self.__jogador.rect.x + self.__jogador.tamanho/2
      self.__borda = 0
    
    @property
    def offset(self):
      return self.__offset

    def scroll(self):
      if self.__jogador.rect.x + self.__jogador.tamanho/2 >= self.__posicao_antiga:
        self.__offset.x = -self.__jogador.rect.x + 400 - self.__jogador.tamanho/2
        self.__borda = self.__jogador.rect.x - self.__DISPLAY_W/2 + self.__jogador.tamanho/2
        self.__posicao_antiga = self.__jogador.rect.x + self.__jogador.tamanho/2
      elif self.__jogador.rect.x < self.__borda:
        self.__jogador.rect.x = self.__borda

    def reset(self):
      self.__init__(self.__jogador)
  