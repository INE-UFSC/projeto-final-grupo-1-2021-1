import pygame

class Jogador:
  def __init__(self):
    self.tamanho = 50
    self.x = 50
    self.y = 500 - 30 - 50
    self.velocidade = 5
    self.pulo = -20
    self.superficie = pygame.Surface((self.tamanho, self.tamanho))
    self.superficie.fill('Purple')
    self.rect = self.superficie.get_rect(bottomleft = (self.x, self.y))
  
  def andar(self, direcao):
    if direcao == 'direita':
      self.rect.x += self.velocidade
    elif direcao == 'esquerda':
      self.rect.x -= self.velocidade
  
  def pular(self):
    if self.rect.y == self.y:
      self.pulo = -20
    
  def update(self):
    self.pulo += 1
    self.rect.y += self.pulo

    if self.rect.y >= self.y:
        self.rect.y = self.y
    
    keys = pygame.key.get_pressed()

    if keys[pygame.K_d]:
      self.andar('direita')
    if keys[pygame.K_a]:
      self.andar('esquerda')
    if keys[pygame.K_w]:
      self.pular()
