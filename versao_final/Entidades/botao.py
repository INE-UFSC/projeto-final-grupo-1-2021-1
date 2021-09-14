import pygame
from Entidades.camera import Camera

class Botao(pygame.sprite.Sprite):
    def __init__(self,x,y,img):
        pygame.sprite.Sprite.__init__(self)
        image = pygame.image.load(img)
        self.__rect = image.get_rect()
        self.__image = pygame.transform.scale(image,(self.__rect.w, self.__rect.h))
        self.__x = x
        self.__y = y
        self.__rect.y = self.__y
        self.__clickado = False
        self.__som_click = pygame.mixer.Sound('sounds/click.wav')

    @property
    def rect(self):
        return self.__rect

    @property
    def image(self):
        return self.__image

    def update(self, camera: Camera):
        self.__rect.x = -camera.offset.x + self.__x

    def interage(self):
        acao = False
        mouse = pygame.mouse.get_pos()
        if self.__x < mouse[0] and self.__x + self.__rect[2] > mouse[0] and self.__rect[3]+self.__y > mouse[1] and self.__y < mouse[1] :
            if pygame.mouse.get_pressed()[0] == 1 and self.__clickado == False:
                acao = True
                self.__clickado = True
                pygame.mixer.Sound.play(self.__som_click)

        if pygame.mouse.get_pressed()[0] == 0:
            self.__clickado = False

        return acao