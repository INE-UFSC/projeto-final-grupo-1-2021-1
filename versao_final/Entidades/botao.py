import pygame
import constantes as c
from Entidades.camera import Camera

class Botao(pygame.sprite.Sprite):
    def __init__(self,x,y,img):
        pygame.sprite.Sprite.__init__(self)
        image = pygame.image.load(img)
        self.rect = image.get_rect()
        self.image = pygame.transform.scale(image,(self.rect.w, self.rect.h))
        self.x = x
        self.y = y
        self.rect.y = self.y
        self.clickado = False

    def update(self, camera: Camera):
        self.rect.x = -camera.offset.x + self.x

    def interage(self):
        acao = False
        mouse = pygame.mouse.get_pos()
        if self.x < mouse[0] and self.x + self.rect[2] > mouse[0] and self.rect[3]+self.y > mouse[1] and self.y < mouse[1] :
            if pygame.mouse.get_pressed()[0] == 1 and self.clickado == False:
                acao = True
                self.clickado = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clickado = False
        
        return acao