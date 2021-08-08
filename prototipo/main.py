from jogador import Jogador
from camera import Camera
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

while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    jogador.update(camera.offset.x)
    camera.scroll()
    
    canvas.blit(background, (-camera.offset.x, 0))
    canvas.blit(jogador.superficie, (jogador.rect.x - camera.offset.x, jogador.rect.y))
    window.blit(canvas,(0,0))

    pygame.display.update()
