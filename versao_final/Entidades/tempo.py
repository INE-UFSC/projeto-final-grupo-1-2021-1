import pygame
import constantes as c

class Tempo():
    def __init__(self):
        self.__tempo_fases = []
        self.__segundos = 0
        self.__tempo_anterior = 0

    def contar(self):
        self.t = pygame.time.get_ticks() - self.__tempo_anterior
        self.__segundos = self.t // c.transforma_segundos
        return self.__segundos

    def reset_timer(self):
        self.__tempo_anterior = pygame.time.get_ticks()

    def salvar_tempo(self):
        self.__tempo_fases.append(self.__segundos)

    def limpar_tempos(self):
        self.__tempo_fases = []
    
    def listar_tempos(self):
        return self.__tempo_fases


#main_font = pygame.font.SysFont("comicsans", 35)
#vidas_label = main_font.render(f"Tempo: {tempo}", 1, (0,0,0))
#self.__tela.blit(vidas_label, (10, 10))