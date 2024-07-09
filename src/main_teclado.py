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

move_left = False
move_right = False
move_up = False
move_down = False

NEWCOINEVENT = pygame.USEREVENT + 1

# configuracion pantalla principal
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("Primer Jueguito")

colission_sound = pygame.mixer.Sound("./src/assets/sounds/coin.mp3")

imagen_ovni = pygame.image.load("./src/assets/images/ovni.png")
imagen_fondo = pygame.image.load("./src/assets/images/fondo.jpg")

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
        
def punto_en_rectangulo(punto, rect):
    x, y = punto
    return x >= rect.left and x <= rect.right and y >= rect.top and y <= rect.bottom
    
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

 



block = create_player(imagen_ovni)
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
        
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT:
                print("izq")
                move_left = True
            if evento.key == pygame.K_RIGHT:
                print("der")
                move_right = True
            if evento.key == pygame.K_UP:
                print("arriba")
                move_up = True
            if evento.key == pygame.K_DOWN:
                print("abajo")
                move_down = True

        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_LEFT:
                print("izq")
                move_left = False
            if evento.key == pygame.K_RIGHT:
                print("der")
                move_right = False
            if evento.key == pygame.K_UP:
                print("arriba")
                move_up = False
            if evento.key == pygame.K_DOWN:
                print("abajo")
                move_down = False

        if evento.type == pygame.MOUSEBUTTONDOWN:
            if evento.button == 1:
                new_coin = create_coin()
                new_coin["color"] = MAGENTA
                new_coin["rect"].center = evento.pos
                coins.append(new_coin)
            print(evento)

    # ----> actualizar los elementos

# verifico si el bloque choca contra los limites de la pantalla
# actualizo su direccion
    # if block["rect"].right >= WIDTH:
    #     # choco derecha
    #     if block["dir"] == DR:
    #         block["dir"] = DL
    #     elif block["dir"] == UR:
    #         block["dir"] = UL
    #     #block["color"] = BLUE #random_color()
    # elif block["rect"].left <= 0:
    #     # choco izquierda
    #     if block["dir"] == UL:
    #         block["dir"] = UR
    #     elif block["dir"] == DL:
    #         block["dir"] = DR
    #     #block["borde"] = randrange(31)
    # elif block["rect"].top <= 0:
    #     # choco arriba
    #     if block["dir"] == UL:
    #         block["dir"] = DL
    #     elif block["dir"] == UR:
    #         block["dir"] = DR
    # elif block["rect"].bottom >= HEIGHT:
    #     # choco abajo
    #     if block["dir"] == DR:
    #         block["dir"] = UR
    #     elif block["dir"] == DL:
    #         block["dir"] = UL
    #     #block["radio"] = randint(-1, 25)


# muevo el bloque de acuerdo a su direccion

    if move_left and block["rect"].left > 0:
        block["rect"].left -= SPEED
        if block["rect"].left < 0:
            block["rect"].left = 0
    if move_right and block["rect"].right < WIDTH:
        block["rect"].left += SPEED
        if block["rect"].left < 0:
            block["rect"].left = 0
    if move_up:
        block["rect"].top -= SPEED
    if move_down:
        block["rect"].top += SPEED


    
    for coin in coins.copy():
        if detectar_colision_circulo(block["rect"], coin["rect"]):
            score += 1
            texto = fuente.render(f"Score: {score}", True, WHITE)
            coins.remove(coin) 
            print("Colision!!!!")
            colission_sound.play()
            if len(coins) == 0:
                load_coin_list(coins, INITIAL_QTY_COINS) # Vuelvo a llenar la pantalla de monedas


    # dibujar pantalla

    #screen.fill(BLACK)

    #pygame.draw.rect(
    #       screen, block["color"], block["rect"], block["borde"], block["radio"])
    screen.blit(imagen_fondo, (0, 0))
    screen.blit(block["img"], block["rect"])

    for coin in coins:
        pygame.draw.rect(screen, coin["color"], coin["rect"], border_radius = coin["radio"])

    screen.blit(texto, (WIDTH // 2, 20))
    
    # actualizo la pantalla

    pygame.display.flip()

pygame.quit()   