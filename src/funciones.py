from constantes import *
from random import *
from ajustes import *
from bloques import *
import sys


def pausa(tecla:pygame.event, imagen:pygame.surface):
    """Congela la partida y muetra una pantalla de pausa

    Args:
        tecla (pygame.event): tecla de pausa
        imagen (pygame.surface): imagen de pausa
    """
    if imagen:
        try:
            screen.blit(imagen, (0,0))
        except TypeError:
            screen.fill(BLACK)

    pausa = True
    while pausa:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                terminar()
            if evento.type == pygame.KEYDOWN:
                if evento.key == tecla:
                    pausa = False
        pygame.display.flip()

def dibujar_vidas(vidas:int, imagen:pygame.surface):
    """Dibuja las vidas en la pantalla.

    Args:
        vidas (int): Cantidad de vidas
        imagen (pygame.surface): imagen de la vida
    """
    x = WIDTH - 50
    y = 20
    for i in range(vidas):
        try:
            screen.blit(imagen, (x - i * 40, y))
        except:
            pygame.draw.rect(screen, RED, (x - i * 40, y, 30, 30))

def damage(jugador:dict, proyectil:dict, lista_proyectil:list, vidas:int, sonido:pygame.mixer, inmunidad:bool)->int:
    """Detecta ssi el jugador colisiono con un proyectil y descuenta una vida

    Args:
        jugador (dict): jugador
        proyectil (dict): proyectil
        lista_proyectil (list): lista de proyectiles
        vidas (int): vidas que tiene el jugador
        sonido (pygame.mixer): sonido de daño
        inmunidad (bool): si es inmune no descuenta vidas

    Returns:
        int: vidas anteriores -1
    """

    if detectar_colision(jugador["rect"], proyectil["rect"]):
        if not inmunidad:
            vidas -=1
            lista_proyectil.remove(proyectil)
            sonido.play()
            return vidas
    
    return vidas

def terminar():
    """ Termina el programa"""

    pygame.quit()
    sys.exit()

def menu_principal(imagen:pygame.surface = None):
    """Pantalla del menú con el botón para iniciar el juego.

    Args:
        imagen (pygame.surface, optional): imagen de fondo. Defaults to None.
    """

    button_w = 200
    button_h = 50

    if imagen:
        try:
            screen.blit(imagen, (0,0))
        except TypeError:
            screen.fill(BLACK)


    texto_jugar = fuente.render("Jugar", True, BLACK) 
    boton_jugar = create_block((WIDTH // 2) - 100, (HEIGHT // 2) - 25, button_w, button_h, color = MAGENTA)
    pygame.draw.rect(screen, boton_jugar["color"], boton_jugar["rect"])
    texto_rect_jugar = texto_jugar.get_rect()
    texto_rect_jugar = (boton_jugar["rect"].x + ((boton_jugar["rect"].width - texto_rect_jugar.width) // 2), boton_jugar["rect"].y + ((boton_jugar["rect"].height - texto_rect_jugar.height) // 2))
    screen.blit(texto_jugar, texto_rect_jugar)

    texto_highscore = fuente.render("Highscore", True, BLACK) 
    boton_highscore = create_block(boton_jugar["rect"].x, boton_jugar["rect"].y + 100, button_w, button_h, color = RED)
    pygame.draw.rect(screen, boton_highscore["color"], boton_highscore["rect"])
    texto_rect_highscore = texto_jugar.get_rect()
    texto_rect_highscore = (boton_highscore["rect"].x - 20 + ((boton_highscore["rect"].width - texto_rect_highscore.width) // 2), boton_highscore["rect"].y + 5 + ((boton_highscore["rect"].height - texto_rect_highscore.height) // 2))
    screen.blit(texto_highscore, texto_rect_highscore)

    continuar = True
    while continuar:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                terminar()
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if evento.button == 1:
                    if punto_en_rectangulo(evento.pos, boton_jugar["rect"]):
                        continuar = False

                    if punto_en_rectangulo(evento.pos, boton_highscore["rect"]):
                        screen_highscore()
                        menu_principal(imagen)
                        continuar = False
                        
        pygame.display.flip()

def game_over(score:int, highscore:int = 0, imagen:pygame.surface = None, sonido:pygame.mixer = None)->bool:
    """ Muestra la pantalla de Game Over con opciones para reiniciar o volver al inicio.

    Args:
        score (int): puntuacion de la partida
        highscore (int, optional):puntuacion mas alta. Defaults to 0.
        imagen (pygame.surface, optional): imagen del fondo. Defaults to None.
        sonido (pygame.mixer, optional): sonido de game over. Defaults to None.

    Returns:
        bool: True = volver al menu
              False = Reiniciar partida
    """

    if sonido:
        try:
            sonido.play()
        except TypeError:
            sonido = None

    if highscore < score:
        highscore = score
        save_highscore(highscore)

    boton_width = 200
    boton_height = 50
    boton_x = (WIDTH - boton_width) // 2
    boton_y = (HEIGHT - boton_height) // 2 + 100

    while True:

        if imagen:
            screen.blit(imagen, (0,0))
        else:
            screen.fill(BLACK)


        texto_gameover = fuente.render("Game Over", True, RED)
        texto_rect_gameover = texto_gameover.get_rect()
        texto_rect_gameover.center = (WIDTH // 2, HEIGHT // 4)
        screen.blit(texto_gameover, texto_rect_gameover)

        texto_highscore = fuente.render(f"Highscore: {highscore}", True, WHITE)
        texto_rect_highscore = texto_highscore.get_rect()
        texto_rect_highscore.center = (texto_rect_gameover.centerx, texto_rect_gameover.centery + 60)
        screen.blit(texto_highscore, texto_rect_highscore)

        texto_score = fuente.render(f"Score: {score}", True, WHITE)
        texto_rect_score = texto_score.get_rect()
        texto_rect_score.center = (texto_rect_highscore.centerx, texto_rect_highscore.centery + 60)
        screen.blit(texto_score, texto_rect_score)
   
        restart_boton = pygame.draw.rect(screen, GREEN, (boton_x, boton_y, boton_width, boton_height))
        texto_restart = fuente.render("Restart", True, WHITE)
        texto_rect_restart = texto_restart.get_rect()
        texto_rect_restart = (restart_boton.x + ((restart_boton.width - texto_rect_restart.width) // 2), restart_boton.y + ((restart_boton.height - texto_rect_restart.height) // 2))
        screen.blit(texto_restart, texto_rect_restart)
        
        inicio_boton = pygame.draw.rect(screen, BLUE, (boton_x, boton_y + 60, boton_width, boton_height))
        texto_inicio = fuente.render("Inicio", True, WHITE)
        texto_rect_inicio = texto_inicio.get_rect()
        texto_rect_inicio = (inicio_boton.x + ((inicio_boton.width - texto_rect_inicio.width) // 2), inicio_boton.y + ((inicio_boton.height - texto_rect_inicio.height) // 2))
        screen.blit(texto_inicio, texto_rect_inicio)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                terminar()

            if evento.type == pygame.MOUSEBUTTONDOWN:
                if evento.button == 1:
                    if punto_en_rectangulo(evento.pos, restart_boton):
                        return False
                    if punto_en_rectangulo(evento.pos, inicio_boton):
                        return True
                    
        pygame.display.flip()

def create_random_projectile(proyectiles_lr:list, proyectiles_rl:list, proyectiles_tb:list, proyectiles_bt:list, imagen:pygame.surface):
    """Crea proyectiles en posiciones aleatorias

    Args:
        proyectiles_lr (list): proyectiles de left to right
        proyectiles_rl (list): proyectiles de right to left
        proyectiles_tb (list): proyectiles de up to down
        proyectiles_bt (list): proyectiles de down to up
        imagen (pygame.surface): imagen del proyectil
    """

    selector = randint(0,3)
    if selector == 0:
        proyectiles_lr.append(create_projectile(0, randint(0,HEIGHT), imagen, color = RED))
    elif selector == 1:
        proyectiles_rl.append(create_projectile(WIDTH, randint(0,HEIGHT), imagen, color = RED))
    elif selector == 2:
        proyectiles_tb.append(create_projectile(randint(0,WIDTH), 0, imagen, color = RED))
    elif selector == 3:
        proyectiles_bt.append(create_projectile(randint(0,WIDTH), HEIGHT, imagen, color = RED))

def save_highscore(valor:int):
    """Crea un archivo con el score mas alto

    Args:
        valor (int): Valor a guardar
    """
    with open("src/Highscore.txt", "w") as file:
        file.write(f"{valor}")

def read_highscore()->int:
    """Lee desde un archivo el record y lo devuelve

    Returns:
        int: highscore
    """
    try:
        with open("src/Highscore.txt", "r") as file:
            valor = int(file.readline())

    except ValueError:
        valor = 0

    except FileNotFoundError:
        with open("src/Highscore.txt", "w") as file:
            file.write("0")
            valor = 0

    return valor

def screen_highscore():
    highscore = read_highscore()

    while True:

        screen.fill(BLACK)

        texto_highscore = fuente.render(f"Highscore: {highscore}", True, GREEN)
        texto_rect_highscore = texto_highscore.get_rect()
        texto_rect_highscore.center = (WIDTH // 2, HEIGHT // 4)
        screen.blit(texto_highscore, texto_rect_highscore)

        texto_volver = fuente.render(f"Volver", True, WHITE)
        texto_rect_volver = texto_volver.get_rect()
        texto_rect_volver.center = (WIDTH // 2, HEIGHT // 2)
        screen.blit(texto_volver, texto_rect_volver)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                terminar()

            if evento.type == pygame.MOUSEBUTTONDOWN:
                if evento.button == 1:
                    if punto_en_rectangulo(evento.pos, texto_rect_volver):
                        return True
                    
        pygame.display.flip()



