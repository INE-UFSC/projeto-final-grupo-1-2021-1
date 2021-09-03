import pygame
from Entidades.jogador import Jogador
from Controlador.controladorNiveis import ControladorNiveis
import constantes as c

class ControladorJogo:
  def __init__(self):
    pygame.init()
    pygame.display.set_caption("√ Variável")
    self.__tela = pygame.display.set_mode((c.largura_tela, c.altura_tela))

    self.__jogador = Jogador()
    self.__controladorNiveis = ControladorNiveis()
    self.__nivel = self.__controladorNiveis.nivel_atual
    self.__running = True
    self.__relogio = pygame.time.Clock()
    self.__canvas = pygame.Surface((c.largura_background, c.altura_background))

    self.__nivel.inserir_jogador(self.__jogador)

  def passar_nivel(self):
    self.__nivel = self.__controladorNiveis.pegar_proximo_nivel()
    self.__nivel.inserir_jogador(self.__jogador)
    self.__nivel.reset()
  
  def iniciar(self):
    while self.__running:
      self.__relogio.tick(60)

      for event in pygame.event.get():
          if event.type == pygame.QUIT:
            self.__running = False

          #Passa de nível quando aperta-se k, é obviamente provisório, só para ver se funciona
          if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_k:
              self.passar_nivel()

      if self.__nivel.bandeirinha.rect.colliderect(self.__jogador.rect.x , self.__jogador.rect.y , self.__jogador.tamanho, self.__jogador.tamanho):
        self.passar_nivel()

      
      self.__nivel.update(self.__canvas)
      self.__tela.blit(self.__canvas,(self.__nivel.camera.offset.x, 0))

      pygame.display.update()