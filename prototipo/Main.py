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

jogador = pygame.Surface((tamanho_jogador, tamanho_jogador))
jogador.fill("Purple")
pos_x = 50
pos_y = 500-30-50
jogador_rect = jogador.get_rect(bottomleft = (pos_x, 500-30))
player_vel = 5

gravidade = 0



while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                if jogador_rect.y == pos_y:
                    gravidade = -20
        

    keys = pygame.key.get_pressed()  
    if keys[pygame.K_a]:
        jogador_rect.x -= player_vel
    if keys[pygame.K_d]:
        jogador_rect.x += player_vel

    
    gravidade += 1
    jogador_rect.y += gravidade
    if jogador_rect.y >= pos_y:
        jogador_rect.y = pos_y
    
        

    
    canvas.blit(background, (0,0))
    canvas.blit(jogador, jogador_rect)
    window.blit(canvas,(0,0))

    pygame.display.update()