from constantes import *
from random import *
from ajustes import *

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
        imagen (_type_, optional): Imagen. Defaults to None.

    Returns:
        dict: Diccionario del rectangulo y la imagen
    """
    dict_block = {}
    dict_block["rect"] = pygame.Rect(left, top, width, height)
    dict_block["color"] = color
    dict_block["borde"] = borde
    dict_block["radio"] = radio
    dict_block["img"] = imagen

    return dict_block


def create_player(rect_w:int=30, rect_h:int=30, imagen = None)->dict:
    """Configura un personaje posicionado en el centro

    Args:
        rect_w (int, optional): Ancho del rect. Defaults to 50.
        rect_h (int, optional): Alto del rect. Defaults to 50.
        imagen (_type_, optional): Imagen. Defaults to None.

    Returns:
        dict: Diccionario con el rectangulo y la imagen
    """
    if imagen:
        imagen = pygame.transform.scale(imagen, (rect_w, rect_h))

    x_center = (WIDTH - rect_w) // 2
    y_center = (HEIGHT - rect_h) // 2
    return create_block(x_center, y_center, rect_w, rect_h, imagen = imagen)

def create_collectable(imagen = None)->dict:
    """crea objeto a recolectar

    Args:
        imagen (_type_, optional): Imagen. Defaults to None.

    Returns:
        dict: diccionario con el rectangulo y la imagen
    """
    width = 20
    height = 20
    radio = width // 2
    pos_x = randint(0, WIDTH//2)
    pos_y = randint(0, HEIGHT)
    return create_block(pos_x, pos_y, width, height, BLUE, radio = radio, imagen = imagen)

def create_projectile(pos_x, pos_y, imagen = None):
    width = 20
    height = 20
    if imagen:
        imagen = pygame.transform.scale(imagen, (width, height))

    return create_block(pos_x, pos_y, width, height, MAGENTA, imagen = imagen)

def move_player(jugador, move_left, move_right, move_up, move_down):
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

def wait_user(tecla) :
    continuar = True
    while continuar :
        for evento in pygame.event.get() :
            if evento.type == pygame.KEYDOWN:
                if evento.key == tecla:
                    continuar = False







def move_projectiles(screen, proyectil, proyectiles_lr, proyectiles_rl, proyectiles_tb, proyectiles_bt):

    for proyectil in proyectiles_lr[:]:  # Usamos [:] para iterar sobre una copia y poder eliminar mientras iteramos
        proyectil["rect"].x += PROJECTILE_SPEED
        pygame.draw.rect(screen, proyectil["color"], proyectil["rect"], proyectil["borde"], proyectil["radio"])
    # Eliminar proyectiles que salen de la pantalla
        if proyectil["rect"].right > WIDTH:
            proyectiles_lr.remove(proyectil)

    for proyectil in proyectiles_rl[:]:  # Usamos [:] para iterar sobre una copia y poder eliminar mientras iteramos
        proyectil["rect"].x -= PROJECTILE_SPEED
        pygame.draw.rect(screen, proyectil["color"], proyectil["rect"], proyectil["borde"], proyectil["radio"])
        # Eliminar proyectiles que salen de la pantalla
        if proyectil["rect"].right < 0:
            proyectiles_rl.remove(proyectil)

    for proyectil in proyectiles_tb[:]:  # Usamos [:] para iterar sobre una copia y poder eliminar mientras iteramos
        proyectil["rect"].y += PROJECTILE_SPEED
        pygame.draw.rect(screen, proyectil["color"], proyectil["rect"], proyectil["borde"], proyectil["radio"])
        # Eliminar proyectiles que salen de la pantalla
        if proyectil["rect"].top > HEIGHT:
            proyectiles_tb.remove(proyectil)

    for proyectil in proyectiles_bt[:]:  # Usamos [:] para iterar sobre una copia y poder eliminar mientras iteramos
        proyectil["rect"].y -= PROJECTILE_SPEED
        pygame.draw.rect(screen, proyectil["color"], proyectil["rect"], proyectil["borde"], proyectil["radio"])
        # Eliminar proyectiles que salen de la pantalla
        if proyectil["rect"].bottom < 0:
            proyectiles_bt.remove(proyectil)