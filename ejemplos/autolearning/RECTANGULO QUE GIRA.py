import pygame
import sys
import math

# Inicializar Pygame
pygame.init()

# Configuración de la ventana
width, height = 600, 400
center_x = width // 2
center_y = height // 2
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
    angle -= angular_speed
    
    # Actualizar la pantalla
    pygame.display.flip()
    
    # Control de velocidad del bucle
    pygame.time.Clock().tick(60)

# Salir de Pygame
pygame.quit()
sys.exit()