import pygame
vec = pygame.math.Vector2

class Camera:
    def __init__(self, jogador):
      self.jogador = jogador
      self.offset = vec(0, 0)
      self.DISPLAY_W, self.DISPLAY_H = 800, 500
      self.posicao_antiga = self.jogador.rect.x + self.jogador.tamanho/2
      self.borda = 0

    def scroll(self):
      if self.jogador.rect.x + self.jogador.tamanho/2 >= self.posicao_antiga:
        self.offset.x = -self.jogador.rect.x + 400 - self.jogador.tamanho/2
        self.borda = self.jogador.rect.x - self.DISPLAY_W/2 + self.jogador.tamanho/2
        self.posicao_antiga = self.jogador.rect.x + self.jogador.tamanho/2
      elif self.jogador.rect.x < self.borda:
        self.jogador.rect.x = self.borda

    def reset(self):
      self.__init__(self.jogador)
  