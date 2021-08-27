import pygame
from Entidades.jogador import Jogador
import constantes as c

class ControladorJogo:
  def __init__(self, tela, niveis):
    self.jogador = Jogador()
    self.niveis = niveis
    self.index_nivel_atual = 0
    self.nivel = niveis[self.index_nivel_atual]
    self.tela = tela
    self.running = True
    self.relogio = pygame.time.Clock()
    self.canvas = pygame.Surface((3075, 500))

    for nivel in self.niveis:
      nivel.inserir_jogador(self.jogador)

  def passar_nivel(self):
    self.index_nivel_atual += 1
    if self.index_nivel_atual == len(self.niveis):
      self.index_nivel_atual = 0
    self.nivel = self.niveis[self.index_nivel_atual]
    self.nivel.reset()
  
  def iniciar(self):
    while self.running:
      self.relogio.tick(60)

      for event in pygame.event.get():
          if event.type == pygame.QUIT:
            self.running = False

          #Passa de nível quando aperta-se k, é obviamente provisório, só para ver se funciona
          if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_k:
              self.passar_nivel()

      if self.nivel.bandeirinha.rect.colliderect(self.jogador.rect.x , self.jogador.rect.y , self.jogador.tamanho, self.jogador.tamanho):
        self.passar_nivel()

      
      self.nivel.update(self.canvas)
      self.tela.blit(self.canvas,(self.nivel.camera.offset.x, 0))

      pygame.display.update()