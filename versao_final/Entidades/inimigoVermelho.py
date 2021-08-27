from Entidades.inimigo import Inimigo

class InimigoVermelho(Inimigo):
    def __init__(self, x, y, distancia_maxima = 200, pulo = -10, cor = "Red", velocidade = 2, largura = 70, altura = 50):
        super().__init__(cor, velocidade, largura, altura, x, y, distancia_maxima)
        self.pulo = pulo

    def update(self):
        self.pulo += 1
        if self.pulo > 10:
            self.pulo = 10
        self.rect.y += self.pulo
        if self.rect.y >= self.y - self.altura:
            self.pulo = -10
            self.rect.y = self.y - self.altura
        self.rect.x += self.velocidade
        self.distancia += self.velocidade
        if abs(self.distancia) > self.distancia_maxima:
            self.velocidade *= -1
            self.distancia = 0

