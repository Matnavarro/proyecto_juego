import pygame
import constantes


class Personaje():
    def __init__(self, x, y):
        self.forma = pygame.Rect(0, 0, 20, 20)
        self.forma.center = (x,y)

    def dibujar(self, interfaz):
        pygame.draw.rect(interfaz, constantes.YELLOW, self.forma)