from jogador import Jogador
from camera import Camera
from pilula import Pilula
from caixa import Caixa
from inimigoVermelho import InimigoVermelho
from inimigoLaranja import InimigoLaranja
import constantes as c
import pygame

pygame.init()
ALTURA, LARGURA = 500, 800
tamanho_jogador = 50
canvas = pygame.Surface((3075, 500))
window = pygame.display.set_mode((LARGURA, ALTURA))
running = True
background = pygame.image.load('images/fase.png').convert()
clock = pygame.time.Clock()

pygame.display.set_caption("√ Variável")

jogador = Jogador()
camera = Camera(jogador)
caixas = [
    # Caixa(50, 50, 550, 470, 2),
    # Caixa(200, 60, 1150, 470, 500)
]

inimigos = [
    InimigoVermelho(600, 470),
    InimigoLaranja(100, 470)
]

pilulas = [
    # Pilula('blue', -10, False, 500, 450),
    # Pilula('green', -10, True, 600, 450),
    # Pilula('red', 10, False, 700, 450),
    # Pilula('blue', -10, False, 800, 450),
    # Pilula('red', 10, False, 900, 450),
    # Pilula('blue', -10, False, 1000, 450),
    # Pilula('red', 10, False, 1100, 450),
    # Pilula('blue', -10, False, 50, 450),
    # Pilula('green', 2, True, 3000, 450),
]

pilula_grupo = pygame.sprite.Group()
pilula_grupo.add(pilulas)
inimigo_grupo = pygame.sprite.Group()
inimigo_grupo.add(inimigos)
caixa_grupo = pygame.sprite.Group()
caixa_grupo.add(caixas)

def reset():
    pilula_grupo.empty()
    inimigo_grupo.empty()
    caixa_grupo.empty()
    pilula_grupo.add(pilulas)
    inimigo_grupo.add(inimigos)
    caixa_grupo.add(caixas)
    jogador.reset()
    camera.reset()


while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    jogador.update(camera.borda, caixa_grupo)
    camera.scroll()
    for inimigo in inimigo_grupo:
        inimigo.andar()

    if pygame.sprite.spritecollide(jogador, pilula_grupo, False):
        jogador.toma_pilula(pilula_grupo)
        background = pygame.image.load('images/fase.png').convert()

    if pygame.sprite.spritecollide(jogador, inimigo_grupo, False):
        reset()
        print("Morreu")
        

    canvas.blit(background, (0, 0))
    canvas.blit(jogador.superficie, (jogador.rect.x, jogador.rect.y))
    pilula_grupo.draw(canvas)
    inimigo_grupo.draw(canvas)
    caixa_grupo.draw(canvas)
    window.blit(canvas,(camera.offset.x, 0))

    pygame.display.update()
