from constantes import *
from random import *
from ajustes import *
import sys

def create_block(left:int=0, top:int=0, width:int=50, height:int=50, color:tuple=(255, 255, 255), borde:int=0, radio=-1, imagen=None)->dict:
    """Genera un bloque

    Args:
        left (int, optional): Posicion x inicial del rect. Defaults to 0.
        top (int, optional): Posicion y inicial del rect. Defaults to 0.
        width (int, optional): Ancho del rect. Defaults to 50.
        height (int, optional): Alto del rect.. Defaults to 50.
        color (tuple, optional): Color. Defaults to (255, 255, 255).
        borde (int, optional): borde. Defaults to 0.
        radio (int, optional): Radio del rect. Defaults to -1.
        imagen (pygame.surface, optional): Imagen. Defaults to None.

    Returns:
        dict: Diccionario del rectangulo y la imagen
    """
    dict_block = {}
    dict_block["rect"] = pygame.Rect(left, top, width, height)
    dict_block["color"] = color
    dict_block["borde"] = borde
    dict_block["radio"] = radio
    if imagen:
        dict_block["img"] = pygame.transform.scale(imagen, (width, height))

    return dict_block

def create_player(rect_w:int=30, rect_h:int=30, imagen:pygame.surface = None)->dict:
    """Configura un personaje posicionado en el centro

    Args:
        rect_w (int, optional): Ancho del rect. Defaults to 50.
        rect_h (int, optional): Alto del rect. Defaults to 50.
        imagen (pygame.surface, optional): Imagen. Defaults to None.

    Returns:
        dict: Diccionario con el rectangulo y la imagen
    """

    x_center = (WIDTH - rect_w) // 2
    y_center = (HEIGHT - rect_h) // 2
    return create_block(x_center, y_center, rect_w, rect_h, imagen = imagen)

def create_collectable(imagen:pygame.surface = None)->dict:
    """crea objeto a recolectar

    Args:
        imagen (pygame.surface, optional): Imagen. Defaults to None.

    Returns:
        dict: diccionario con el rectangulo y la imagen
    """
    width = 30
    height = 30

    radio = width // 2
    margen = 15
    margen_x = WIDTH * margen // 100
    margen_y =  HEIGHT * margen // 100
    pos_x = randint(margen_x, WIDTH - margen_x)
    pos_y = randint(margen_y, HEIGHT - margen_y)

    return create_block(pos_x, pos_y, width, height, BLUE, radio = radio, imagen = imagen)

def create_projectile(pos_x:int, pos_y:int, imagen:pygame.surface = None, color:tuple = MAGENTA)->dict:
    """Crea un proyectil

    Args:
        pos_x (int): coordenada en x
        pos_y (int): coordenada en y
        imagen (pygame.surface, optional): imagen. Defaults to None.
        color (tuple, optional): color. Defaults to MAGENTA.

    Returns:
        dict: diccionario con el rect y la imagen
    """
    width = 20
    height = 20

    return create_block(pos_x, pos_y, width, height, color, imagen = imagen)

def detectar_colision(rect_1:pygame.rect, rect_2:pygame.rect)->bool:
    """Detecta la colision entre dos rect

    Args:
        rect_1 (pygame.rect): rect 1
        rect_2 (pygame.rect): rect 2

    Returns:
        bool: True si colisionan, False si no.
    """
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
        
def punto_en_rectangulo(punto:tuple, rect:pygame.rect)->bool:
    """Detecta si un punto se encuentra dentro de un rect

    Args:
        punto (tuple): punto a analizar
        rect (pygame.rect): rect a analizar

    Returns:
        bool: True si el punto está dentro del rect. False si no.
    """
    x = punto[0]
    y = punto[1]
    return x >= rect.left and x <= rect.right and y >= rect.top and y <= rect.bottom

def delete_projectiles(proyectiles:list):
    """remueve todos los elementos de una lista individual

    Args:
        proyectiles (list): lista a vaciar
    """
    for proyectil in proyectiles[:]:
        proyectiles.remove(proyectil)

def delete_all_projectiles(proyectiles_lr:list, proyectiles_rl:list, proyectiles_tb:list, proyectiles_bt:list):
    """Elimina todos los proyectiles de la pantalla

    Args:
        proyectiles_lr (list): proyectiles de left to right
        proyectiles_rl (list): proyectiles de right to left
        proyectiles_tb (list): proyectiles de up to down
        proyectiles_bt (list): proyectiles de down to up
    """
    delete_projectiles(proyectiles_lr)
    delete_projectiles(proyectiles_rl)
    delete_projectiles(proyectiles_tb)
    delete_projectiles(proyectiles_bt)

def move_player(jugador:pygame.rect, move_left:bool, move_right:bool, move_up:bool, move_down:bool):
    """Mueve el jugador por la pantalla dependiendo de la tecla presionada

    Args:
        jugador (pygame.rect): Rect del jugador
        move_left (bool): flag movimiento a la izquierda
        move_right (bool): flag movimiento a la derecha
        move_up (bool): flag movimiento hacia arriba
        move_down (bool): flag movimiento hacia abajo
    """
    if move_left and jugador.left > 0:
        jugador.left -= SPEED
        if jugador.left < 0:
            jugador.left = 0

    if move_right and jugador.right < WIDTH:
        jugador.right += SPEED
        if jugador.right > WIDTH:
            jugador.right = WIDTH

    if move_up and jugador.top > 0:
        jugador.top -= SPEED
        if jugador.top < 0:
            jugador.top = 0

    if move_down and jugador.bottom < HEIGHT:
        jugador.bottom += SPEED
        if jugador.bottom > HEIGHT:
            jugador.bottom = HEIGHT

def move_proyectil_lr(proyectil:dict, lista_proyectiles:list):
    """Mueve el proyectil de izq a der

    Args:
        proyectil (dict): proyectil a mover
        lista_proyectiles (list): lista de proyectiles
    """

    proyectil["rect"].x += PROJECTILE_SPEED
    screen.blit(proyectil["img"], proyectil["rect"])
    if proyectil["rect"].left > WIDTH: 
        lista_proyectiles.remove(proyectil)

def move_proyectil_rl(proyectil, lista_proyectiles):
    """Mueve el proyectil de der a izq

    Args:
        proyectil (dict): proyectil a mover
        lista_proyectiles (list): lista de proyectiles
    """

    proyectil["rect"].x -= PROJECTILE_SPEED
    screen.blit(proyectil["img"], proyectil["rect"])
    if proyectil["rect"].right < 0:
        lista_proyectiles.remove(proyectil)

def move_proyectil_tb(proyectil, lista_proyectiles):
    """Mueve el proyectil de arriba a abajo

    Args:
        proyectil (dict): proyectil a mover
        lista_proyectiles (list): lista de proyectiles
    """

    proyectil["rect"].y += PROJECTILE_SPEED
    screen.blit(proyectil["img"], proyectil["rect"])
    if proyectil["rect"].top > HEIGHT:
        lista_proyectiles.remove(proyectil)

def move_proyectil_bt(proyectil, lista_proyectiles):
    """Mueve el proyectil de abajo hacia arriba

    Args:
        proyectil (dict): proyectil a mover
        lista_proyectiles (list): lista de proyectiles
    """

    proyectil["rect"].y -= PROJECTILE_SPEED
    screen.blit(proyectil["img"], proyectil["rect"])
    if proyectil["rect"].top < 0:
        lista_proyectiles.remove(proyectil)


