import pygame
from camera import Camera

class Nivel:
  def __init__(self, background, pilulas = [], caixas = [], inimigos = []):
    self.pilulas = pilulas
    self.caixas = caixas
    self.inimigos = inimigos
    self.background = pygame.image.load(background).convert()

    self.grupo_pilulas = pygame.sprite.Group()
    self.grupo_caixas= pygame.sprite.Group()
    self.grupo_inimigos = pygame.sprite.Group()

    self.grupo_pilulas.add(self.pilulas)
    self.grupo_caixas.add(self.caixas)
    self.grupo_inimigos.add(self.inimigos)
  
  def inserir_jogador(self, jogador):
    self.jogador = jogador
    self.camera = Camera(self.jogador)

  def reset(self):
    self.grupo_pilulas.empty()
    self.grupo_caixas.empty()
    self.grupo_inimigos.empty()

    self.grupo_pilulas.add(self.pilulas)
    self.grupo_caixas.add(self.caixas)
    self.grupo_inimigos.add(self.inimigos)

    self.jogador.reset()
    self.camera.reset()
  
  def update(self, screen):
    self.jogador.update(self.grupo_caixas, self.grupo_pilulas)
    self.camera.scroll()

    self.grupo_inimigos.update()
    
    if pygame.sprite.spritecollide(self.jogador, self.grupo_inimigos, False):
      self.reset()
    
    screen.blit(self.background, (0, 0))
    screen.blit(self.jogador.superficie, (self.jogador.rect.x, self.jogador.rect.y))

    self.grupo_pilulas.draw(screen)
    self.grupo_inimigos.draw(screen)
    self.grupo_caixas.draw(screen)