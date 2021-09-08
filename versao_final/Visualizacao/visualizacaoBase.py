from abc import abstractmethod, ABC
import pygame

class VisualizacaoBase(ABC):
  @abstractmethod
  def __init__(self):
    self.__fonte_titulo = pygame.font.SysFont('comicsans', 30, bold=pygame.font.Font.bold)
    self.__fonte = pygame.font.SysFont('comicsans', 30)
  
  @property
  def fonte_titulo(self):
    return self.__fonte_titulo
  
  @property
  def fonte(self):
    return self.__fonte

  @abstractmethod
  def update(self, screen):
    pass