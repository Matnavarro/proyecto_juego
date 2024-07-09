import pygame
import sys
def punto_en_rectangulo(punto, rect):
    x = punto[0]
    y = punto[1]
    return x >= rect.left and x <= rect.right and y >= rect.top and y <= rect.bottom
# Inicializar Pygame
pygame.init()

# Configuración de pantalla
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Menú de Opciones")

# Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)

# Fuente
font = pygame.font.Font(None, 36)

# Función para dibujar un botón
def draw_button(text, rect, color, hover_color, action=None):
    mouse_pos = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    hovered = punto_en_rectangulo(mouse_pos, rect)
    
    if hovered:
        pygame.draw.rect(screen, hover_color, rect)
        if click[0] == 1 and action:
            pygame.time.delay(200)
            action()
    else:
        pygame.draw.rect(screen, color, rect)
    
    text_surf = font.render(text, True, BLACK)
    screen.blit(text_surf, (rect.x + (rect.width - text_surf.get_width()) // 2, rect.y + (rect.height - text_surf.get_height()) // 2))
    
    return hovered

# Acciones de los botones
def go_to_screen1():
    screen1()

def go_to_screen2():
    screen2()

def go_to_screen3():
    screen3()

def quit_game():
    pygame.quit()
    sys.exit()

# Pantalla principal
def main_menu():
    while True:
        screen.fill(WHITE)
        mouse_over_button = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game()

        if draw_button("Opción 1", pygame.Rect(300, 200, 200, 50), BLUE, YELLOW, go_to_screen1):
            mouse_over_button = True
        if draw_button("Opción 2", pygame.Rect(300, 300, 200, 50), BLUE, YELLOW, go_to_screen2):
            mouse_over_button = True
        if draw_button("Opción 3", pygame.Rect(300, 400, 200, 50), BLUE, YELLOW, go_to_screen3):
            mouse_over_button = True
        if draw_button("Salir", pygame.Rect(300, 500, 200, 50), RED, YELLOW, quit_game):
            mouse_over_button = True

        if mouse_over_button:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

        pygame.display.flip()

# Otras pantallas
def screen1():
    while True:
        screen.fill(WHITE)
        mouse_over_button = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game()

        text_surf = font.render("Screen 1", True, BLACK)
        screen.blit(text_surf, (screen_width // 2 - text_surf.get_width() // 2, screen_height // 2 - text_surf.get_height() // 2))

        if draw_button("Volver", pygame.Rect(300, 500, 200, 50), GREEN, YELLOW, main_menu):
            mouse_over_button = True

        if mouse_over_button:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

        pygame.display.flip()

def screen2():
    while True:
        screen.fill(WHITE)
        mouse_over_button = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game()

        text_surf = font.render("Screen 2", True, BLACK)
        screen.blit(text_surf, (screen_width // 2 - text_surf.get_width() // 2, screen_height // 2 - text_surf.get_height() // 2))

        if draw_button("Volver", pygame.Rect(300, 500, 200, 50), GREEN, YELLOW, main_menu):
            mouse_over_button = True

        if mouse_over_button:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

        pygame.display.flip()

def screen3():
    while True:
        screen.fill(WHITE)
        mouse_over_button = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game()

        text_surf = font.render("Screen 3", True, BLACK)
        screen.blit(text_surf, (screen_width // 2 - text_surf.get_width() // 2, screen_height // 2 - text_surf.get_height() // 2))

        if draw_button("Volver", pygame.Rect(300, 500, 200, 50), GREEN, YELLOW, main_menu):
            mouse_over_button = True

        if mouse_over_button:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

        pygame.display.flip()

# Iniciar la pantalla principal

main_menu()
