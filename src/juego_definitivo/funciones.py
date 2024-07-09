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
        imagen (_type_, optional): Imagen. Defaults to None.

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


def create_player(rect_w:int=30, rect_h:int=30, imagen = None)->dict:
    """Configura un personaje posicionado en el centro

    Args:
        rect_w (int, optional): Ancho del rect. Defaults to 50.
        rect_h (int, optional): Alto del rect. Defaults to 50.
        imagen (_type_, optional): Imagen. Defaults to None.

    Returns:
        dict: Diccionario con el rectangulo y la imagen
    """

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
    width = 30
    height = 30
    # if imagen:
    #     imagen = pygame.transform.scale(imagen, (width, height))

    radio = width // 2
    margen = 15
    margen_x = WIDTH * margen // 100
    margen_y =  HEIGHT * margen // 100
    pos_x = randint(margen_x, WIDTH - margen_x)
    pos_y = randint(margen_y, HEIGHT - margen_y)

    return create_block(pos_x, pos_y, width, height, BLUE, radio = radio, imagen = imagen)

def create_projectile(pos_x, pos_y, imagen = None, color = MAGENTA):
    width = 20
    height = 20

    return create_block(pos_x, pos_y, width, height, color, imagen = imagen)

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
    x = punto[0]
    y = punto[1]
    return x >= rect.left and x <= rect.right and y >= rect.top and y <= rect.bottom

def wait_user(tecla) :
    continuar = True
    while continuar :
        for evento in pygame.event.get() :
            if evento.type == pygame.KEYDOWN:
                if evento.key == tecla:
                    continuar = False

def dibujar_vidas(vidas, imagen):
    x = WIDTH - 50
    y = 20
    for i in range(vidas):
        screen.blit(imagen, (x - i * 40, y))

def damage(jugador, proyectil, lista_proyectil, vidas, sonido):
    if detectar_colision(jugador["rect"], proyectil["rect"]):
        vidas -=1
        lista_proyectil.remove(proyectil)
        sonido.play()
        return vidas
    
    return vidas

def terminar():
    pygame.quit()
    sys.exit()

def delete_projectiles(proyectiles_lr, proyectiles_rl, proyectiles_tb, proyectiles_bt):
    for proyectil in proyectiles_lr[:]:
        proyectiles_lr.remove(proyectil)
    for proyectil in proyectiles_rl[:]:
        proyectiles_rl.remove(proyectil)
    for proyectil in proyectiles_tb[:]:
        proyectiles_tb.remove(proyectil)
    for proyectil in proyectiles_bt[:]:
        proyectiles_bt.remove(proyectil)

    move_left = False
    move_right = False
    move_up = False
    move_down = False

def menu_principal(imagen):

    button_w = 200
    button_h = 50

    texto_jugar = fuente.render("Jugar", True, WHITE) 
    #texto_jugar = texto_jugar.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.blit(imagen, (0,0))
    button_play = create_block((WIDTH // 2) - 100, (HEIGHT // 2) - 25, button_w, button_h, color = MAGENTA)
    pygame.draw.rect(screen, button_play["color"], button_play["rect"], button_play["borde"], button_play["radio"])
    screen.blit(texto_jugar, button_play["rect"])

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                terminar()
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if evento.button == 1:
                    if punto_en_rectangulo(evento.pos, button_play["rect"]):
                        return

        pygame.display.flip()

def game_over(score, highscore = None, imagen = None):
    
    highscore = 20

    # Dimensiones y posición de los botones
    boton_width = 200
    boton_height = 50
    boton_x = (WIDTH - boton_width) // 2
    boton_y_restart = (HEIGHT - boton_height) // 2 + 100

    # Colores
    boton_color = GREEN
    texto_color = WHITE


    while True:
        screen.fill(BLACK)
        # Texto de "Game Over" en la parte superior
        texto_game_over = fuente.render("Game Over", True, RED)
        text_rect_game_over = texto_game_over.get_rect(center=(WIDTH // 2, HEIGHT // 4))
        screen.blit(texto_game_over, text_rect_game_over)

        # Texto de "Highscore" y "Score" debajo
        texto_highscore = fuente.render(f"Highscore: {highscore}", True, WHITE)
        
        screen.blit(texto_highscore, (10,20))

        texto_score = fuente.render(f"Score: {score}", True, WHITE)
        #text_rect_score = texto_score.get_rect(center=(WIDTH // 2, HEIGHT // 2 +100))
        screen.blit(texto_score, (10,10))

        # Botón Restart
        boton = pygame.draw.rect(screen, boton_color, (boton_x, boton_y_restart, boton_width, boton_height))
        texto_restart = fuente.render("Restart", True, texto_color)
        #text_rect_restart = texto_restart.get_rect(center=(WIDTH // 2, boton_y_restart + boton_height // 2))
        text_rect_restart = texto_restart.get_rect()
        text_rect_restart = (boton.x + ((boton.width - text_rect_restart.width) // 2), boton.y + ((boton.height - text_rect_restart.height) // 2))
        
        #text_rect
        screen.blit(texto_restart, text_rect_restart)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                terminar()

            if evento.type == pygame.MOUSEBUTTONDOWN:
                if evento.button == 1:
                    if punto_en_rectangulo(evento.pos, boton):
                        return

        pygame.display.flip()
    # posicion_texto_highscore = ((WIDTH // 2) - WIDTH*0.25, (HEIGHT // 2) - HEIGHT * 0,95)
    # posicion_texto_gameover = 

    # screen.blit(imagen, (0,0))
    # screen.blit(texto_gameover, posicion_texto_gameover)

    # if highscore < score:
    #     highscore = score

def create_random_projectile(proyectiles_lr, proyectiles_rl, proyectiles_tb, proyectiles_bt, imagen):

    selector = randint(0,3)

    if selector == 0:
        proyectiles_lr.append(create_projectile(0, randint(0,HEIGHT), imagen, color = RED))
    elif selector == 1:
        proyectiles_rl.append(create_projectile(WIDTH, randint(0,HEIGHT), imagen, color = RED))
    elif selector == 2:
        proyectiles_tb.append(create_projectile(randint(0,WIDTH), 0, imagen, color = RED))
    elif selector == 3:
        proyectiles_bt.append(create_projectile(randint(0,WIDTH), HEIGHT, imagen, color = RED))





















# def draw_button(text, rect, color, hover_color, action=None):
#     mouse_pos = pygame.mouse.get_pos()
#     click = pygame.mouse.get_pressed()
#     hovered = punto_en_rectangulo(mouse_pos, rect)
    
#     if hovered:
#         pygame.draw.rect(screen, hover_color, rect)
#         if click[0] == 1 and action:
#             pygame.time.delay(200)
#             action()
#     else:
#         pygame.draw.rect(screen, color, rect)
    
#     text_surf = font.render(text, True, BLACK)
#     screen.blit(text_surf, (rect.x + (rect.width - text_surf.get_width()) // 2, rect.y + (rect.height - text_surf.get_height()) // 2))
# def main_menu():
#     while True:
#         screen.fill(WHITE)
#         mouse_over_button = False

#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 quit_game()

#         if draw_button("Opción 1", pygame.Rect(300, 200, 200, 50), BLUE, YELLOW, game()):
#             mouse_over_button = True
#         if draw_button("Opción 2", pygame.Rect(300, 300, 200, 50), BLUE, YELLOW, scores()):
#             mouse_over_button = True
#         if draw_button("Salir", pygame.Rect(300, 500, 200, 50), RED, YELLOW, salir()):
#             mouse_over_button = True

#         if mouse_over_button:
#             pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
#         else:
#             pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

#         pygame.display.flip()












# def presionar_boton(coordenadas_x: tuple, coordenadas_y: tuple, boton: str, raton_x: int, raton_y) -> str:
    
#     """ 
#     Maneja la lógica al presionar un botón.

#     Argumentos:
#     - coordenadas_x: Tupla con las coordenadas X del botón.
#     - coordenadas_y: Tupla con las coordenadas Y del botón.
#     - boton: Nombre del botón.
#     - raton_x: Coordenada X del ratón.
#     - raton_y: Coordenada Y del ratón.
#      """
    
#     mensaje = ""
#     if coordenadas_x[0] <= raton_x <= coordenadas_x[1] and coordenadas_y[0] <= raton_y <= coordenadas_y[1]:
        
#         sonido_click = pygame.mixer.Sound("./src/assets/sounds/point.mp3")
#         sonido_click.set_volume(0.35)
#         sonido_click.play()

#     return mensaje

##### Hacer que no se pueda mover en diagonal, agrandar tamaño al jugador para agregar dificultad, eventos aleatorios, no poder parar



# def manejo_eventos(evento, proyectiles_lr, proyectiles_rl, proyectiles_tb, proyectiles_bt):
#     if evento.type == pygame.QUIT:
#         is_running = False

#     if evento.type == pygame.KEYDOWN:
#         if evento.key == pygame.K_LEFT:
#             print("izq")
#             move_left = True
#             move_right = False
#             proyectiles_lr.append(create_projectile(0, jugador["rect"].centery, imagen_proyectil))

#         if evento.key == pygame.K_RIGHT:
#             print("der")
#             move_right = True
#             move_left = False
#             proyectiles_rl.append(create_projectile(WIDTH, jugador["rect"].centery, imagen_proyectil))

#         if evento.key == pygame.K_UP:
#             print("arriba")
#             move_up = True
#             move_down = False
#             proyectiles_tb.append(create_projectile(jugador["rect"].centerx, 0, imagen_proyectil))

#         if evento.key == pygame.K_DOWN:
#             print("abajo")
#             move_down = True
#             move_up = False
#             proyectiles_bt.append(create_projectile(jugador["rect"].centerx, HEIGHT, imagen_proyectil))
# def move_projectiles(screen, proyectil, proyectiles_lr, proyectiles_rl, proyectiles_tb, proyectiles_bt):

#     for proyectil in proyectiles_lr[:]:  # Usamos [:] para iterar sobre una copia y poder eliminar mientras iteramos
#         proyectil["rect"].x += PROJECTILE_SPEED
#         pygame.draw.rect(screen, proyectil["color"], proyectil["rect"], proyectil["borde"], proyectil["radio"])
#     # Eliminar proyectiles que salen de la pantalla
#         if proyectil["rect"].right > WIDTH:
#             proyectiles_lr.remove(proyectil)

#     for proyectil in proyectiles_rl[:]:  # Usamos [:] para iterar sobre una copia y poder eliminar mientras iteramos
#         proyectil["rect"].x -= PROJECTILE_SPEED
#         pygame.draw.rect(screen, proyectil["color"], proyectil["rect"], proyectil["borde"], proyectil["radio"])
#         # Eliminar proyectiles que salen de la pantalla
#         if proyectil["rect"].right < 0:
#             proyectiles_rl.remove(proyectil)

#     for proyectil in proyectiles_tb[:]:  # Usamos [:] para iterar sobre una copia y poder eliminar mientras iteramos
#         proyectil["rect"].y += PROJECTILE_SPEED
#         pygame.draw.rect(screen, proyectil["color"], proyectil["rect"], proyectil["borde"], proyectil["radio"])
#         # Eliminar proyectiles que salen de la pantalla
#         if proyectil["rect"].top > HEIGHT:
#             proyectiles_tb.remove(proyectil)

#     for proyectil in proyectiles_bt[:]:  # Usamos [:] para iterar sobre una copia y poder eliminar mientras iteramos
#         proyectil["rect"].y -= PROJECTILE_SPEED
#         pygame.draw.rect(screen, proyectil["color"], proyectil["rect"], proyectil["borde"], proyectil["radio"])
#         # Eliminar proyectiles que salen de la pantalla
#         if proyectil["rect"].bottom < 0:
#             proyectiles_bt.remove(proyectil)