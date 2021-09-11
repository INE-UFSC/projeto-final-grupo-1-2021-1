from Entidades.inimigo import Inimigo

class InimigoVermelho(Inimigo):
    def __init__(self, x, y, distancia_maxima = 200, pulo = -10, cor = "Vermelho", velocidade = 2, largura = 40, altura = 70):
        super().__init__(cor, velocidade, largura, altura, x, y, distancia_maxima)
        self.__pulo = pulo

    def update(self):
        self.andar_pulando()
    
    def andar_pulando(self):
        self.__pulo += 1
        if self.__pulo > 10:
            self.__pulo = 10
        self.rect.y += self.__pulo
        if self.rect.y >= self.y - self.altura:
            self.__pulo = -10
            self.rect.y = self.y - self.altura
        self.rect.x += self.velocidade
        self.distancia += self.velocidade
        if abs(self.distancia) > self.distancia_maxima:
            self.velocidade *= -1
            self.distancia = 0

