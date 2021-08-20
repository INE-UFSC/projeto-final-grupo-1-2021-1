import pygame
from camera import Camera

class Nivel:
  def __init__(self, background, bandeirinha, pilulas = [], caixas = [], inimigos = [], blocos = []):
    self.pilulas = pilulas
    self.caixas = caixas
    self.inimigos = inimigos
    self.blocos = blocos
    self.bandeirinha = bandeirinha
    self.background = pygame.image.load(background).convert()

    self.grupo_pilulas = pygame.sprite.Group()
    self.grupo_caixas= pygame.sprite.Group()
    self.grupo_inimigos = pygame.sprite.Group()
    self.grupo_blocos = pygame.sprite.Group()
    self.grupo_bandeirinha = pygame.sprite.Group()

    self.grupo_pilulas.add(self.pilulas)
    self.grupo_caixas.add(self.caixas)
    self.grupo_inimigos.add(self.inimigos)
    self.grupo_blocos.add(self.blocos)
    self.grupo_bandeirinha.add(self.bandeirinha)
  
  def inserir_jogador(self, jogador):
    self.jogador = jogador
    self.camera = Camera(self.jogador)

  def reset(self):
    self.grupo_pilulas.empty()
    self.grupo_caixas.empty()
    self.grupo_inimigos.empty()
    self.grupo_blocos.empty()

    self.grupo_pilulas.add(self.pilulas)
    self.grupo_caixas.add(self.caixas)
    self.grupo_inimigos.add(self.inimigos)
    self.grupo_blocos.add(self.blocos)

    self.jogador.reset()
    self.camera.reset()
  
  def update(self, screen):
    self.jogador.update(self.grupo_caixas, self.grupo_pilulas, self.grupo_blocos)
    self.camera.scroll()

    self.grupo_inimigos.update()
    
    if pygame.sprite.spritecollide(self.jogador, self.grupo_inimigos, False):
      self.reset()
    
    screen.blit(self.background, (0, 0))
    screen.blit(self.jogador.superficie, (self.jogador.rect.x, self.jogador.rect.y))

    self.grupo_pilulas.draw(screen)
    self.grupo_inimigos.draw(screen)
    self.grupo_caixas.draw(screen)
    self.grupo_blocos.draw(screen)
    self.grupo_bandeirinha.draw(screen)