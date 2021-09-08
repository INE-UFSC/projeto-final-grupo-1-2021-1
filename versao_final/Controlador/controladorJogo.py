from Visualizacao.telaVitoria import TelaVitoria
from Visualizacao.telaTransicaoNivel import TelaTransicaoNivel
import pygame
from Visualizacao.telaInicial import TelaInicial
from Entidades.jogador import Jogador
from Controlador.controladorNiveis import ControladorNiveis
from Entidades.tempo import Tempo
import constantes as c

class ControladorJogo:
  def __init__(self):
    pygame.init()
    pygame.font.init() 
    pygame.display.set_caption("√ Variável")
    self.__tela = pygame.display.set_mode((c.largura_tela, c.altura_tela))

    self.__jogador = Jogador()
    self.__controladorNiveis = ControladorNiveis()
    self.__nivel = self.__controladorNiveis.nivel_atual
    self.__running = True
    self.__relogio = pygame.time.Clock()
    self.__canvas = pygame.Surface((c.largura_background, c.altura_background))
    self.__timer = Tempo()

    self.__nivel.inserir_jogador(self.__jogador)

    self.__tela_inicial = TelaInicial()
    self.__tela_transicao_nivel = TelaTransicaoNivel()
    self.__tela_vitoria = TelaVitoria(self.__controladorNiveis.niveis)
  
    self.__estados = [self.__tela_inicial, self.__nivel, self.__tela_transicao_nivel, self.__tela_vitoria]
    self.__index_estado_atual = c.estado_tela_inicial
    self.__estado_atual = self.__estados[self.__index_estado_atual]

    self.__fonte_tempo = pygame.font.SysFont("comicsans", 35)
    self.__tempor = 0

  def passar_nivel(self):
    self.__nivel = self.__controladorNiveis.pegar_proximo_nivel()
    self.__nivel.inserir_jogador(self.__jogador)
    self.__nivel.reset()
    self.__timer.reset_timer()
    self.__estados[c.estado_jogando_nivel] = self.__nivel
  
  def proximo_estado(self):
    if self.__index_estado_atual == c.estado_tela_inicial:
      self.__timer.limpar_tempos()
      self.__index_estado_atual = c.estado_jogando_nivel
    elif self.__index_estado_atual == c.estado_jogando_nivel:
      self.__timer.salvar_tempo()
      if self.__controladorNiveis.eh_ultimo_nivel():
        self.__index_estado_atual = c.estado_vitoria
      else:
        self.__tela_transicao_nivel.atualiza_texto(f'Você concluiu com exito o nível {self.__controladorNiveis.index_nivel_atual + 1}')
        self.__index_estado_atual = c.estado_transicao_nivel
      self.passar_nivel()
    elif self.__index_estado_atual == c.estado_transicao_nivel:
      self.__index_estado_atual = c.estado_jogando_nivel
    elif self.__index_estado_atual == c.estado_vitoria:
      self.__index_estado_atual = c.estado_tela_inicial
    
    self.__estado_atual = self.__estados[self.__index_estado_atual]
  
  def iniciar(self):
    while self.__running:
      self.__relogio.tick(60)

      for event in pygame.event.get():
          if event.type == pygame.QUIT:
            self.__running = False
      
      realizar_transicao = self.__estado_atual.update(self.__canvas)

      if realizar_transicao:
        self.proximo_estado()

      self.__tela.blit(self.__canvas,(self.__nivel.camera.offset.x, 0))

#retirem esse comentário quando forem dar o proximo commit
#tive que fazer uma verificação como no caso acima para passar de fase, mas aqui funciona para mostrarmos ou não o tempo e resetá-lo
      if self.__index_estado_atual == c.estado_jogando_nivel:
        self.__tempor = self.__timer.contar()
      elif self.__index_estado_atual == c.estado_transicao_nivel:
        self.__timer.reset_timer()
      elif self.__index_estado_atual == c.estado_tela_inicial:
        self.__timer.reset_timer()
        self.__tempor = self.__timer.contar()

      if self.__controladorNiveis.nivel_atual.reset_timer == True:
        self.__timer.reset_timer()
      
      #if self.__index_estado_atual == c.estado_vitoria:
        #print(self.__timer.listar_tempos()) 
      texto_tempo = self.__fonte_tempo.render(f"Tempo: {self.__tempor}", 1, (0,0,0))

#retirem essa parte também
#é um if para não mostrar o tempo nem na tela inicial nem na tela de vitória, podemos mudar isso depois qualquer coisa
#mas fiz um listar no tempo.py que vai retornar os tempos de cada fase para arrumarmos bonitinho no final
      if self.__index_estado_atual == c.estado_tela_inicial or self.__index_estado_atual == c.estado_vitoria:
        pass
      else:
        self.__tela.blit(texto_tempo, (10, 10))

      pygame.display.update()