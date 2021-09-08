import pygame
import constantes as c

class Jogador:
  def __init__(self):
    self.__tamanho = c.tamanho_inicial_jogador
    self.__x = c.largura_tela/2 - self.__tamanho/2
    self.__y = c.altura_tela - 30 - self.__tamanho
    self.__pulo = 0
    self.__superficie = pygame.Surface((self.__tamanho, self.__tamanho))
    self.__superficie.fill('Purple')
    self.__rect = self.__superficie.get_rect(bottomleft = (self.__x, self.__y))
    self.__tamanho_min = 10
    self.__tamanho_max = 100
    self.__tamanho_pulo = (15*self.__tamanho - 2400)/90
    self.__pulou = False

  @property
  def rect(self):
    return self.__rect
  
  @property
  def superficie(self):
    return self.__superficie
  
  @property
  def tamanho(self):
    return self.__tamanho

  def pular(self):
    if self.__rect.y == self.__y:
      self.__pulo = self.__tamanho_pulo
    
  def update(self, caixas, pilulas, blocos, caixas_quebradas):
    dx = 0
    dy = 0
    
    keys = pygame.key.get_pressed()

    if keys[pygame.K_d]:
      dx += 5
    if keys[pygame.K_a]:
      dx -= 5
    if keys[pygame.K_w] and not self.__pulou:
      self.__pulo = self.__tamanho_pulo
      self.__pulou = True

    self.__pulo += 1
    if self.__pulo > 10:
      self.__pulo = 10

    dy += self.__pulo

    for caixa in caixas:
      #Colisão no eixo x
      if caixa.rect.colliderect(self.__rect.x + dx, self.__rect.y, self.__tamanho, self.__tamanho):
        dx = 0
        if self.__tamanho > caixa.forca_necessaria:
          caixas.remove(caixa)
          caixa.quebrar()
          caixas_quebradas.add(caixa)
      #Colisão no eixo y
      if caixa.rect.colliderect(self.__rect.x, self.__rect.y + dy, self.__tamanho, self.__tamanho):
        #Colisão quando está pulando
        if self.__pulo < 0:
            dy = caixa.rect.bottom - self.__rect.top
            self.__pulo = 0
        #Colisão quando está caindo
        elif self.__pulo >= 0:
            dy = caixa.rect.top - self.__rect.bottom
            self.__pulo = 0
            self.__pulou = False
    
    for bloco in blocos:
      #Colisão no eixo x
      if bloco.rect.colliderect(self.__rect.x + dx, self.__rect.y, self.__tamanho, self.__tamanho):
        dx = 0
      #Colisão no eixo y
      if bloco.rect.colliderect(self.__rect.x, self.__rect.y + dy, self.__tamanho, self.__tamanho):
        #Colisão quando está pulando
        if self.__pulo < 0:
            dy = bloco.rect.bottom - self.__rect.top
            self.__pulo = 0
        #Colisão quando está caindo
        elif self.__pulo >= 0:
            dy = bloco.rect.top - self.__rect.bottom
            self.__pulo = 0
            self.__pulou = False
    
    for pilula in pilulas:
      if pilula.rect.colliderect(self.__rect.x + dx, self.__rect.y + dy, self.__tamanho, self.__tamanho):
        self.toma_pilula(pilula)
        pilulas.remove(pilula)

    self.__rect.x += dx
    self.__rect.y += dy

    if self.__rect.y > self.__y:
      self.__rect.y = self.__y
      self.__pulou = False
    if self.__rect.x > c.largura_background - self.__tamanho:
      self.__rect.x = c.largura_background - self.__tamanho

  def toma_pilula(self, pilula):
      if pilula.reseta_tamanho:
        self.mudar_tamanho(True)
      else:
        self.mudar_tamanho(False, pilula.efeito)
        
  def mudar_tamanho(self, reseta, tamanho = 10):
    if self.__tamanho + tamanho < self.__tamanho_min or self.__tamanho + tamanho > self.__tamanho_max:
      return
    
    if reseta:
      self.__tamanho = self.__tamanho_min
    else:
      self.__tamanho += tamanho

    self.__y = c.altura_tela - 30 - self.__tamanho
    self.__superficie = pygame.Surface((self.__tamanho, self.__tamanho))
    self.__rect = self.__superficie.get_rect(bottomleft = (self.__rect.x, self.__rect.y + self.__tamanho))
    self.__superficie.fill('Purple')
    self.__tamanho_pulo = (15*self.__tamanho - 2400)/90

  def reset(self):
    self.__init__()
    