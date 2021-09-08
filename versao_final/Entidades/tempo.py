import pygame
import constantes as c
from Entidades.camera import Camera

class Tempo():
    def __init__(self):
        self.__segundos = 0
        self.__tempo_anterior = 0
        self.__x = 10
        self.__fonte_tempo = pygame.font.SysFont("comicsans", 35)
    
    @property
    def segundos(self):
        return self.__segundos
    
    def __str__(self):
        return f'{self.__segundos}'

    def contar(self):
        self.t = pygame.time.get_ticks() - self.__tempo_anterior
        self.__segundos = self.t // c.transforma_segundos
        self.__segundos

    def reset_timer(self):
        self.__tempo_anterior = pygame.time.get_ticks()
    
    def update(self, camera: Camera):
        self.__x = -camera.offset.x + 10

    def draw(self, screen):
        texto_tempo = self.__fonte_tempo.render(f"Tempo: {self.__segundos}", True, (0,0,0))
        screen.blit(texto_tempo, (self.__x, 10))
