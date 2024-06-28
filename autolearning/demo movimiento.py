import pygame
import sys
import math

# Inicializar Pygame
pygame.init()

# Configurar la ventana
WIDTH, HEIGHT = 800, 600
win = pygame.display.set_mode((WIDTH, HEIGHT))

# Configurar el personaje
player_size = 20
player_x = WIDTH // 2
player_y = HEIGHT // 2
player_color = (0, 0, 255)  # Azul
player_speed = 1

angle = 0
jugador = pygame.Rect(player_x, player_y, player_size, player_size)
# Bucle principal del juego
running = True
while running:
    pygame.time.Clock().tick(60)
    win.fill((0, 0, 0))  # Llenar la pantalla de negro

    # Dibujar al personaje
    jugador = pygame.draw.rect(win, player_color, (player_x, player_y, player_size, player_size))

    # Eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Movimiento del personaje


    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x - player_speed > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x + player_speed < WIDTH - player_size:
        player_x += player_speed
    if keys[pygame.K_UP] and player_y - player_speed > 0:
        player_y -= player_speed
    if keys[pygame.K_DOWN] and player_y + player_speed < HEIGHT - player_size:
        player_y += player_speed
    if keys[pygame.K_SPACE]:
        vuelta_x = player_x + 100 * math.cos(angle)
        vuelta_y = player_y + 100 * math.sin(angle)
        player_x = vuelta_x
        player_y = vuelta_y
        angle -= player_speed

    # Actualizar la pantalla
    pygame.display.flip()

pygame.quit()
sys.exit()


############ MOVIMIENTO CIRCULAR############

         #pygame.draw.rect(win, player_color, (vuelta_x - player_size // 2, vuelta_y - player_size // 2, player_size, player_size))
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
