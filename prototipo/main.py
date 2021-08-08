from jogador import Jogador
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

while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    jogador.update()
    
    canvas.blit(background, (0,0))
    canvas.blit(jogador.superficie, jogador.rect)
    window.blit(canvas,(0,0))

    pygame.display.update()