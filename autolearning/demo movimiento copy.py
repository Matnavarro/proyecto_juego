import pygame
import sys
import math
# Inicializar Pygame
pygame.init()

# Configurar la ventana
WIDTH, HEIGHT = 800, 600
win = pygame.display.set_mode((WIDTH, HEIGHT))

# Ángulo inicial
angle = 0

# Velocidad angular
#angular_speed = 0.03

# Configurar el personaje
player_size = 20
center_x =  WIDTH // 2
center_y = HEIGHT // 2
player_color = (0, 0, 255)  # Azul
player_speed = 1

jugador = pygame.Rect(center_x, center_y, player_size, player_size)
jugador_x = center_x
jugador_y = center_y

# jugador_x = jugador_x + 100 * math.cos(angle)
# jugador_y = jugador_y + 100 * math.sin(angle)

# Bucle principal del juego
running = True
while running:
    win.fill((0, 0, 0))  # Llenar la pantalla de negro

    # Dibujar al personaje
    pygame.draw.rect(win, player_color, (center_x, center_y, player_size, player_size))

    # Eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Movimiento del personaje

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and jugador_x - player_speed > 0:
        jugador_x -= player_speed
    if keys[pygame.K_RIGHT] and jugador_x + player_speed < WIDTH - player_size:
        jugador_x += player_speed
    if keys[pygame.K_UP] and jugador_y - player_speed > 0:
        jugador_y -= player_speed
    if keys[pygame.K_DOWN] and jugador_y + player_speed < HEIGHT - player_size:
        jugador_y += player_speed
    if keys[pygame.K_SPACE]:
        pass#j.x = 
    # Actualizar la pantalla
    pygame.display.flip()

pygame.quit()
sys.exit()


############ MOVIMIENTO CIRCULAR############

import pygame
import sys
import math

# Inicializar Pygame
pygame.init()

# Configuración de la ventana
width, height = 600, 400
center_x, center_y = width // 2, height // 2
window = pygame.display.set_mode((width, height))
pygame.display.set_caption('Rectángulo que rota en círculos')

# Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Dimensiones del rectángulo
rect_width, rect_height = 100, 50

# Ángulo inicial
angle = 0

# Velocidad angular
angular_speed = 0.03

# Bucle principal
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Calcular las coordenadas del rectángulo en función del ángulo
    x = center_x + 100 * math.cos(angle)
    y = center_y + 100 * math.sin(angle)
    
    # Calcular el rectángulo rotado
    rotated_rect = pygame.Rect(x - rect_width // 2, y - rect_height // 2, rect_width, rect_height)
    
    # Dibujar en la pantalla
    window.fill(BLACK)
    pygame.draw.rect(window, WHITE, rotated_rect)
    
    # Actualizar el ángulo
    angle += angular_speed
    
    # Actualizar la pantalla
    pygame.display.flip()
    
    # Control de velocidad del bucle
    pygame.time.Clock().tick(60)

# Salir de Pygame
pygame.quit()
sys.exit()
