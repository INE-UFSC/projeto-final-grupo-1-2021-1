import pygame

class Jogador:
  def __init__(self):
    self.tamanho = 50
    self.x = 400 - 50
    self.y = 500 - 30 - 50
    self.velocidade = 5
    self.pulo = 0
    self.superficie = pygame.Surface((self.tamanho, self.tamanho))
    self.superficie.fill('Purple')
    self.rect = self.superficie.get_rect(bottomleft = (self.x, self.y))
  
  def andar(self, direcao, borda):
    if direcao == 'direita':
      self.rect.x += self.velocidade
    elif direcao == 'esquerda':
      self.rect.x -= self.velocidade
    if self.rect.x < borda:
      self.rect.x = borda
    if self.rect.x > 3075 - 50:
      self.rect.x = 3075 - 50


  def pular(self):
    if self.rect.y == self.y:
      self.pulo = -20
    
  def update(self, borda):
    self.pulo += 1
    self.rect.y += self.pulo

    if self.rect.y >= self.y:
        self.rect.y = self.y
    
    keys = pygame.key.get_pressed()

    if keys[pygame.K_d]:
      self.andar('direita', borda), 
    if keys[pygame.K_a]:
      self.andar('esquerda', borda)
    if keys[pygame.K_w]:
      self.pular()

