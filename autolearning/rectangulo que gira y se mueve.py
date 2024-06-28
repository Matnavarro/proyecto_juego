import pygame
import sys
import math

# Inicializar Pygame
pygame.init()

# Configuración de la ventana
width, height = 600, 400
center_x, center_y = width // 2, height // 2
window = pygame.display.set_mode((width, height))
pygame.display.set_caption('Rectángulo que rota y se mueve')

# Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Dimensiones del rectángulo
rect_width, rect_height = 100, 50

# Posición inicial del rectángulo
rect_x, rect_y = center_x, center_y

# Ángulo inicial
angle = 0

# Velocidad angular
angular_speed = 0.03

# Velocidad de movimiento del rectángulo
move_speed = 5

# Bucle principal
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Obtener el estado del teclado
    keys = pygame.key.get_pressed()
    
    # Manejo del movimiento del rectángulo con las teclas de flecha
    if keys[pygame.K_LEFT]:
        rect_x -= move_speed
    elif keys[pygame.K_RIGHT]:
        rect_x += move_speed
    elif keys[pygame.K_UP]:
        rect_y -= move_speed
    elif keys[pygame.K_DOWN]:
        rect_y += move_speed
    
    # Manejo de la rotación del rectángulo con la tecla 'R'
    if keys[pygame.K_r]:
        angle += angular_speed
    
    # Calcular las coordenadas del rectángulo en función del ángulo
    x = center_x + 100 * math.cos(angle)
    y = center_y + 100 * math.sin(angle)
    
    # Calcular el rectángulo rotado
    rotated_rect = pygame.Rect(rect_x - rect_width // 2, rect_y - rect_height // 2, rect_width, rect_height)
    
    # Dibujar en la pantalla
    window.fill(BLACK)
    pygame.draw.rect(window, WHITE, rotated_rect)
    
    # Actualizar la pantalla
    pygame.display.flip()
    
    # Control de velocidad del bucle
    pygame.time.Clock().tick(60)

# Salir de Pygame
pygame.quit()
sys.exit()
