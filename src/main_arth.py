import pygame
from settings import * # Cosas para los settings 
# import sys (no le gusta al profe)
# sys.exit() # escapar del programa

pygame.init() # Inicia todos los modulos (.display, .mixer, etc )

SCREEN = pygame.display.set_mode(SCREEN_SIZE) #crear la pantalla (800 ancho, 600 de alto)
pygame.display.set_allow_screensaver("Mi primer juego") # Cambiar titulo

SCREEN.fill(CUSTOM) # Cambiar color de la pantalla .fill((red, green, blue)) maximo de valor de color es 255

contador = 0

is_running = True # bandera para decir que esta andando el progragama
while is_running:
    print(contador)
    contador +=1
    for event in pygame.event.get(): # pygame.event.get() # Devuelve una lista de los eventos que ocurrieron
        if event.type == pygame.QUIT: # pygame.QUIT = 256 numero del evento para cerrar (quit) | Todos los eventos tienen un valor numerico y aparecen como constant
            is_running = False

    pygame.display.flip() # Voltea la pantall \ actualiza

pygame.quit() # contrario a pygame.init() | Cierra el programa