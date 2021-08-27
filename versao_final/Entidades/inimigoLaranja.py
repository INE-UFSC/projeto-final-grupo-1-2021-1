from Entidades.inimigo import Inimigo

class InimigoLaranja(Inimigo):
    def __init__(self, x, y, distancia_maxima = 100, cor = "Orange", velocidade = 7, largura = 30, altura = 70):
        super().__init__(cor, velocidade, largura, altura, x, y, distancia_maxima)

    def update(self):
        self.rect.x += self.velocidade
        self.distancia += self.velocidade
        if abs(self.distancia) > self.distancia_maxima:
            self.velocidade *= -1
            self.distancia = 0
