import pygame
from funciones import *
from clases import *
from constantes import *

pygame.init() # Inicia todos los modulos (.display, .mixer, etc )
SCREEN = pygame.display.set_mode(SCREEN_SIZE) #crear la pantalla (800 ancho, 600 de alto)
pygame.display.set_caption("cuadradito") # Cambiar titulo
clock = pygame.time.Clock() # Crea un reloj
jugador = Personaje(10,20)
speed = 10
bajar = True
left = True
is_running = True # bandera para decir que esta andando el progragama
while is_running:

    clock.tick(FPS) #va frenando el while para que dure lo mismo | Son los FPS

    # analizamos elementos
    is_running = analizar_elementos()

    pygame.draw
