import pygame
import constantes as c

class Jogador:
  def __init__(self):
    self.tamanho = c.tamanho_inicial_jogador
    self.x = c.largura_tela/2 - self.tamanho
    self.y = c.altura_tela - 30 - self.tamanho
    self.pulo = 0
    self.superficie = pygame.Surface((self.tamanho, self.tamanho))
    self.superficie.fill('Purple')
    self.rect = self.superficie.get_rect(bottomleft = (self.x, self.y))
    self.tamanho_min = 10
    self.tamanho_max = 100
    self.tamanho_pulo = (15*self.tamanho - 2400)/90
    self.pulou = False
    self.velocidade = -(self.tamanho_pulo/3)
  
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
      self.pulo = self.tamanho_pulo
    
  def update(self, borda, caixas):
    dx = 0
    dy = 0
    
    keys = pygame.key.get_pressed()

    if keys[pygame.K_d]:
      dx += 5
    if keys[pygame.K_a]:
      dx -= 5
    if keys[pygame.K_w] and not self.pulou:
      self.pulo = self.tamanho_pulo
      self.pulou = True

    self.pulo += 1
    if self.pulo > 10:
      self.pulo = 10

    dy += self.pulo

    for caixa in caixas:
      #check for collision in x direction
      if caixa.rect.colliderect(self.rect.x + dx, self.rect.y, self.tamanho, self.tamanho):
        dx = 0
        if self.tamanho > caixa.forca_necessaria:
          caixas.remove(caixa)
      #check for collision in y direction
      if caixa.rect.colliderect(self.rect.x, self.rect.y + dy, self.tamanho, self.tamanho):
        #check if below the ground i.e. jumping
        if self.pulo < 0:
            dy = caixa.rect.bottom - self.rect.top
            self.pulo = 0
        #check if above the ground i.e. falling
        elif self.pulo >= 0:
            dy = caixa.rect.top - self.rect.bottom
            self.pulo = 0
            self.pulou = False

    self.rect.x += dx
    self.rect.y += dy

    if self.rect.y > self.y:
      self.rect.y = self.y
      self.pulou = False
    if self.rect.x < borda:
      self.rect.x = borda
    if self.rect.x > 3075 - self.tamanho:
      self.rect.x = 3075 - self.tamanho

  def toma_pilula(self, pilulas):
      pilulas_tomadas = pygame.sprite.spritecollide(self, pilulas, True)
      for pilula in pilulas_tomadas:
        if pilula.reseta_tamanho:
          self.mudar_tamanho(True)
        else:
          self.mudar_tamanho(False, pilula.efeito)
        
      self.mudar_velocidade()
        
  def mudar_tamanho(self, reseta, tamanho = 10):
    if self.tamanho + tamanho < self.tamanho_min or self.tamanho + tamanho > self.tamanho_max:
      return
    
    if reseta:
      self.tamanho = self.tamanho_min
    else:
      self.tamanho += tamanho

    self.superficie = pygame.Surface((self.tamanho, self.tamanho))
    self.rect = self.superficie.get_rect(bottomleft = (self.rect.x, self.rect.y))
    self.superficie.fill('Purple')
    self.y = 500 - 30 - self.tamanho
    self.tamanho_pulo = (15*self.tamanho - 2400)/90
  
  def mudar_velocidade(self):
    self.velocidade = -(self.tamanho_pulo/3)

  def reset(self):
    self.__init__()
    