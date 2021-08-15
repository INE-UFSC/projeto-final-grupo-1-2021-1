import pygame
from mapas import niveis, tela_principal
from controladorJogo import ControladorJogo

jogo = ControladorJogo(tela_principal, niveis)

jogo.iniciar()

pygame.quit()
