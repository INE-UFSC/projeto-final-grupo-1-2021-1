import pygame

class Jogador:
  def __init__(self):
    self.tamanho = 100
    self.x = 400 - self.tamanho
    self.y = 500 - 30 - self.tamanho
    self.velocidade = 5
    self.pulo = 0
    self.superficie = pygame.Surface((self.tamanho, self.tamanho))
    self.superficie.fill('Purple')
    self.rect = self.superficie.get_rect(bottomleft = (self.x, self.y))
    self.tamanho_min = 10
    self.tamanho_max = 100
  
  def andar(self, direcao, borda):
    if direcao == 'direita':
      self.rect.x += self.velocidade
    elif direcao == 'esquerda':
      self.rect.x -= self.velocidade
    if self.rect.x < borda:
      self.rect.x = borda
    if self.rect.x > 3075 - self.tamanho:
      self.rect.x = 3075 - self.tamanho


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

  def toma_pilula(self, pilulas):
      pilulas_tomadas = pygame.sprite.spritecollide(self, pilulas, True)
      for pilula in pilulas_tomadas:
        self.mudar_tamanho(pilula.efeito)
        
  def mudar_tamanho(self,tamanho):
    if self.tamanho + tamanho <= self.tamanho_min or self.tamanho + tamanho >= self.tamanho_max:
      return
    self.tamanho += tamanho
    self.superficie = pygame.Surface((self.tamanho, self.tamanho))
    self.rect = self.superficie.get_rect(bottomleft = (self.rect.x, self.rect.y))
    self.superficie.fill('Purple')
    self.y = 500 - 30 - self.tamanho
  
      

