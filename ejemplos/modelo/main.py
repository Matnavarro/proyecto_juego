import pygame
from settings import * # Cosas para los settings 

# import sys (no le gusta al profe)
# sys.exit() # escapar del programa

pygame.init() # Inicia todos los modulos (.display, .mixer, etc )

SCREEN = pygame.display.set_mode(SCREEN_SIZE) #crear la pantalla (800 ancho, 600 de alto)
pygame.display.set_allow_screensaver("Mi primer juego") # Cambiar titulo

pygame.display.set_caption("cuadradito") # Cambiar titulo

clock = pygame.time.Clock() # Crea un reloj

#rect_1 = pygame.rect.Rect() # cualquiera sirve, conviene la otra
rect_1 = pygame.Rect(300, 400, 50, 80) # objeto rectangulo x e y de donde empieza, el ancho y el alto
rect_1 = pygame.Rect((ANCHO - 200)//2, (ALTO - 100)//2, 50, 50) # objeto rectangulo x e y de donde empieza, el ancho y el alto

#pygame.color.THECOLORS ### (?)
# for color in pygame.color.THECOLORS.keys():
#     print(color)

speed = 10
bajar = True
left = True
is_running = True # bandera para decir que esta andando el progragama
while is_running:

    clock.tick(FPS) #va frenando el while para que dure lo mismo | Son los FPS

    # analizamos elementos
    for event in pygame.event.get(): # pygame.event.get() Devuelve una lista de los eventos que ocurrieron
        if event.type == pygame.QUIT: # pygame.QUIT = 256 numero del evento para cerrar (quit) | Todos los eventos tienen un valor numerico y aparecen como constant
            is_running = False


    # actualizamos elementos
    if bajar:
        if rect_1.bottom <= ALTO:
            rect_1.y += speed

        else:
            bajar = False
    else:
        if rect_1.top >= 0:
           rect_1.y -= speed        
        else:
            bajar = True

    if left:
        if rect_1.right <= ANCHO:
            rect_1.x += speed
        else:
            left = False
    else:
        if rect_1.left >= 0:
           rect_1.x -= speed        
        else:
            left = True


    # dibujamos en pantalla
                                                #pygame.draw.rect(SCREEN, RED, (0, 0, 200, 100)) # se pasa la pantalla y el rectangulo
    SCREEN.fill(CUSTOM) # Cambiar color de la pantalla .fill((red, green, blue)) maximo de valor de color es 255
    pygame.draw.rect(SCREEN, RED, rect_1)


    # actualizamos pantalla
    #pygame.display.update()
    pygame.display.flip() # Voltea la pantalla \ actualiza
    

















    # pygame.draw.rect(SCREEN, BLUE, rect_1)
    # rect_3 = pygame.draw.circle(SCREEN, MAGENTA, SCREEN_CENTER, 75, 5) # tamaño circulo, el 5 es opcional, para que haga circunferencia de esos pixeles
    # pygame.draw.rect(SCREEN, BLUE, rect_3, 5) # dibujo rectangulo del tamaño del circulo
    # rect_2 = pygame.draw.ellipse(SCREEN, RED, (0, 0, 200, 100))
    # pygame.draw.rect(SCREEN, YELLOW, rect_2, 5) # se pasa la pantalla y el rectangulo
    # rect_4 = pygame.draw.line(SCREEN, BLACK, rect_2.center, rect_3.center, 3)
    # pygame.draw.rect(SCREEN, WHITE, rect_4, 3)
    # rect_5 = pygame.draw.polygon(SCREEN, BLUE, [(50, 50), (400, 300), (300, 500)], 3)
    # pygame.draw.rect(SCREEN, BLACK, rect_5, 3)
    



pygame.quit() # contrario a pygame.init() | Cierra el programa