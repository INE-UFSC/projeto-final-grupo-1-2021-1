from Entidades.inimigo import Inimigo

class InimigoLaranja(Inimigo):
    def __init__(self, x, y, distancia_maxima = 300, cor = "Laranja", velocidade = 7, largura = 70, altura = 40, mutante = False):
        super().__init__(cor, velocidade, largura, altura, x, y, distancia_maxima, mutante)

    def update(self):
        self.andar()
    
    def andar(self):
        self.rect.x += self.velocidade
        self.distancia += self.velocidade
        if abs(self.distancia) > self.distancia_maxima:
            self.velocidade *= -1
            self.distancia = 0
