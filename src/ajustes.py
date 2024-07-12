from constantes import *
import json

pygame.init()

clock = pygame.time.Clock()

pygame.display.set_caption("Primer Jueguito")
screen = pygame.display.set_mode(SCREEN_SIZE)
fuente = pygame.font.SysFont(None, 48, False, True)

move_left = False
move_right = False
move_up = False
move_down = False

with open("src/images.json", "r") as file:
    imagenes_recursos = json.load(file)

imagen_menu = pygame.image.load(imagenes_recursos["menu_juego"])
imagen_pausa = pygame.image.load(imagenes_recursos["pausa"])
imagen_fondo = pygame.image.load(imagenes_recursos["fondo"])
imagen_ranking = pygame.image.load(imagenes_recursos["ranking"])
imagen_proyectil = pygame.image.load(imagenes_recursos["proyectil"])
imagen_proyectil2 = pygame.image.load(imagenes_recursos["proyectil2"])
imagen_objeto = pygame.image.load(imagenes_recursos["objeto"])
imagen_bomba = pygame.image.load(imagenes_recursos["bomba"])
imagen_vida = pygame.image.load(imagenes_recursos["vida"])
imagen_jugador = pygame.image.load(imagenes_recursos["player"])

imagen_fondo = pygame.transform.scale(imagen_fondo, SCREEN_SIZE)
imagen_menu = pygame.transform.scale(imagen_menu, SCREEN_SIZE)
imagen_pausa = pygame.transform.scale(imagen_pausa, SCREEN_SIZE)
imagen_ranking = pygame.transform.scale(imagen_ranking, SCREEN_SIZE)
imagen_vida = pygame.transform.scale(imagen_vida, (30, 30))

with open("src/sounds.json", "r") as file:
    sonidos_recursos = json.load(file)

sonido_score = pygame.mixer.Sound(sonidos_recursos["score"])
sonido_damage = pygame.mixer.Sound(sonidos_recursos["damage"])
sonido_gameover = pygame.mixer.Sound(sonidos_recursos["game_over"])
sonido_bomba = pygame.mixer.Sound(sonidos_recursos["bomba"])


proyectiles_lr = []
proyectiles_rl = []
proyectiles_tb = []
proyectiles_bt = []



is_running = True
menu = True
bomb_timer = True

pygame.time.set_timer(NEW_PROJECTILE_EVENT, 1000)
pygame.time.set_timer(NEW_BOMB_EVENT, 10000)

