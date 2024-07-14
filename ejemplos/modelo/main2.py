import pygame
#from aleatorios import *
from random import *
from sys import exit
from settings import *


# inicializar los modulos de pygame
pygame.init()

clock = pygame.time.Clock()

gravedad_y = True
gravedad_x = True

# configuracion pantalla principal
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("Primer Jueguito")

# configuro la direccion
UR = 9
DR = 3
DL = 1
UL = 7

direcciones = (UR, DR, DL, UL)


rect_w = 100
rect_h = 100
count_blocks = 2

def detectar_colision(rect_1, rect_2):
    if punto_en_rectangulo(rect_1.topleft, rect_2) or \
       punto_en_rectangulo(rect_1.topright, rect_2) or\
       punto_en_rectangulo(rect_1.bottomleft, rect_2) or\
       punto_en_rectangulo(rect_1.bottomright, rect_2) or\
       punto_en_rectangulo(rect_2.topleft, rect_1) or \
       punto_en_rectangulo(rect_2.topright, rect_1) or\
       punto_en_rectangulo(rect_2.bottomleft, rect_1) or\
       punto_en_rectangulo(rect_2.bottomright, rect_1):
        return True
    else:
        return False
        

def punto_en_rectangulo(punto, rect):
    x, y = punto
    return x >= rect.left and x <= rect.right and y >= rect.top and y <= rect.bottom
 
    


def create_block(left=0, top=0, width=50, height=50, color=(255, 255, 255), dir=3, borde=0, radio=-1):
    return {"rect": pygame.Rect(left, top, width, height), "color": color, "dir": dir, "borde": borde, "radio": radio}


blocks = []

for block in range(count_blocks):
    blocks.append(create_block(randint(0, WIDTH - rect_w), randint(0, HEIGHT -
                  rect_h), rect_w, rect_h, dir = direcciones[randrange(len(direcciones))], color = randint(0, WIDTH - rect_w)))
    





is_running = True

while is_running:
    clock.tick(FPS)
    # ----> detectar los eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            is_running = False

    # ----> actualizar los elementos

# verifico si el bloque choca contra los limites de la pantalla
# actualizo su direccion
    for block in blocks:
        if block["rect"].right >= WIDTH:
            # choco derecha
            if block["dir"] == DR:
                block["dir"] = DL
            elif block["dir"] == UR:
                block["dir"] = UL
            block["color"] = GREEN #random_color()
        elif block["rect"].left <= 0:
            # choco izquierda
            if block["dir"] == UL:
                block["dir"] = UR
            elif block["dir"] == DL:
                block["dir"] = DR
            block["borde"] = randrange(31)
        elif block["rect"].top <= 0:
            # choco arriba
            if block["dir"] == UL:
                block["dir"] = DL
            elif block["dir"] == UR:
                block["dir"] = DR
        elif block["rect"].bottom >= HEIGHT:
            # choco abajo
            if block["dir"] == DR:
                block["dir"] = UR
            elif block["dir"] == DL:
                block["dir"] = UL
            block["radio"] = randint(-1, 25)


# muevo el bloque de acuerdo a su direccion
    for block in blocks:
        if block["dir"] == DR:
            block["rect"].top += SPEED
            block["rect"].left += SPEED
        elif block["dir"] == DL:
            block["rect"].top += SPEED
            block["rect"].left -= SPEED
        elif block["dir"] == UL:
            block["rect"].top -= SPEED
            block["rect"].left -= SPEED
        elif block["dir"] == UR:
            block["rect"].top -= SPEED
            block["rect"].left += SPEED

    if detectar_colision(blocks[0]["rect"], blocks[1]["rect"]):
        print("Colision!!!!")

    

    


    # dibujar pantalla

    screen.fill(BLACK)

    for block in blocks:
        pygame.draw.rect(
            screen, block["color"], block["rect"], block["borde"], block["radio"])

    # actualizo la pantalla

    pygame.display.flip()

pygame.quit()