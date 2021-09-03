from abc import abstractmethod, ABC

class VisualizacaoBase(ABC):
  @abstractmethod
  def __init__(self):
    pass

  @abstractmethod
  def update(self, screen):
    pass