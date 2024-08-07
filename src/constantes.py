import pygame

# Configuración de pantalla 
WIDTH = 800
HEIGHT = 600
SCREEN_SIZE = (WIDTH, HEIGHT)
SCREEN_CENTER = (WIDTH // 2, HEIGHT // 2)
FPS = 60

# Colores
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
MAGENTA = (225, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
CUSTOM = (157, 208, 230)

# Velocidades
SPEED = 7
PROJECTILE_SPEED = 5

# Vidas
VIDAS = 20

# Eventos
NEW_PROJECTILE_EVENT = pygame.USEREVENT + 1
NEW_BOMB_EVENT = pygame.USEREVENT + 2