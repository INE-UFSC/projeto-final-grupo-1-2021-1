from jogador import Jogador
from camera import Camera
from pilula import Pilula
import pygame

pygame.init()
ALTURA, LARGURA = 500, 800
tamanho_jogador = 50
canvas = pygame.Surface((LARGURA, ALTURA))
window = pygame.display.set_mode((LARGURA, ALTURA))
running = True
background = pygame.image.load('images/fase.png').convert()
clock = pygame.time.Clock()

pygame.display.set_caption("√ Variável")

jogador = Jogador()
camera = Camera(jogador)

pilulas = [
    Pilula('blue', -10, False, 500, 450),
    Pilula('green', -10, True, 600, 450),
    Pilula('red', 10, False, 700, 450),
    Pilula('blue', -10, False, 800, 450),
    Pilula('red', 10, False, 900, 450),
    Pilula('blue', -10, False, 1000, 450),
    Pilula('red', 10, False, 1100, 450),
    Pilula('blue', -10, False, 50, 450),
    Pilula('green', 2, True, 3000, 450),
]

pilula_grupo = pygame.sprite.Group()
pilula_grupo.add(pilulas)

while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    jogador.update(camera.offset.x)
    camera.scroll()

    if pygame.sprite.spritecollide(jogador, pilula_grupo, False):
        jogador.toma_pilula(pilula_grupo)
        background = pygame.image.load('images/fase.png').convert()
        

    canvas.blit(background, (-camera.offset.x, 0))
    canvas.blit(jogador.superficie, (jogador.rect.x - camera.offset.x, jogador.rect.y))
    pilula_grupo.draw(background)
    window.blit(canvas,(0, 0))

    pygame.display.update()
