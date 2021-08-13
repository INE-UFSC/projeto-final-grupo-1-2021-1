import pygame
vec = pygame.math.Vector2

class Camera:
    def __init__(self, player):
      self.player = player
      self.offset = vec(0, 0)
      self.DISPLAY_W, self.DISPLAY_H = 800, 500
      self.posicao_antiga = self.player.rect.x

    def scroll(self):
      if self.player.rect.x > self.posicao_antiga:
        self.offset.x = self.player.rect.x - self.DISPLAY_W/2 + self.player.tamanho
        self.posicao_antiga = self.player.rect.x

    def reset(self):
      self.__init__(self.player)
  