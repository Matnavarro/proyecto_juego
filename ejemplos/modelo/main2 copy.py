import pygame
#from aleatorios import *
from random import *
from sys import exit
from settings import *
from bloques import *

# inicializar los modulos de pygame
pygame.init()

clock = pygame.time.Clock()

gravedad_y = True
gravedad_x = True

# configuracion pantalla principal
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("Primer Jueguito")

# Configuro la fuente para el texto

fuente = pygame.font.SysFont(None, 48, False, True)

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
        
def distancia_entre_puntos(punto_1:tuple[int,int], punto_2:tuple[int,int]):
    base = punto_1[0] - punto_2[0] # Es la cordenada en x de ambos puntos
    altura = punto_1[1] - punto_2[1]
    return (base ** 2 + altura ** 2) ** 0.5
    # base = rect_1.centerx - rect_2.centerx
    # altura = rect_1.centery - rect_2.centery
    # distancia = sqrt(pow(base,2)+pow(altura,2))

def detectar_colision_circulo(rect_1, rect_2):  
    r1 = rect_1.width // 2
    r2 =  rect_2.width // 2
    distancia = distancia_entre_puntos(rect_1.center, rect_2.center)
    if distancia <= r1 + r2:
        return True
    else: return False

def punto_en_rectangulo(punto, rect):
    x, y = punto
    return x >= rect.left and x <= rect.right and y >= rect.top and y <= rect.bottom
 



block = create_player()
#print(block["color"])
block["color"] = BLUE
coins = []
load_coin_list(coins, INITIAL_QTY_COINS)

score = 0
texto = fuente.render(f"Score: {score}", True, WHITE)

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
    if block["rect"].right >= WIDTH:
        # choco derecha
        if block["dir"] == DR:
            block["dir"] = DL
        elif block["dir"] == UR:
            block["dir"] = UL
        #block["color"] = BLUE #random_color()
    elif block["rect"].left <= 0:
        # choco izquierda
        if block["dir"] == UL:
            block["dir"] = UR
        elif block["dir"] == DL:
            block["dir"] = DR
        #block["borde"] = randrange(31)
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
        #block["radio"] = randint(-1, 25)


# muevo el bloque de acuerdo a su direccion

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

    
    for coin in coins.copy():
        if detectar_colision_circulo(block["rect"], coin["rect"]):
            score += 1
            texto = fuente.render(f"Score: {score}", True, WHITE)
            coins.remove(coin)
            print("Colision!!!!")
            if len(coins) == 0:
                load_coin_list(coins, INITIAL_QTY_COINS) # Vuelvo a llenar la pantalla de monedas


    # dibujar pantalla

    screen.fill(BLACK)

    pygame.draw.rect(
            screen, block["color"], block["rect"], block["borde"], block["radio"])
    

    for coin in coins:
        pygame.draw.rect(screen, coin["color"], coin["rect"], border_radius = coin["radio"])

    screen.blit(texto, (WIDTH // 2, 20))
    
    # actualizo la pantalla

    pygame.display.flip()

pygame.quit()