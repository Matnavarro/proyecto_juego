from constantes import *


move_left = False
move_right = False
move_up = False
move_down = False

pygame.init()

clock = pygame.time.Clock()

pygame.display.set_caption("Primer Jueguito")
screen = pygame.display.set_mode(SCREEN_SIZE)
fuente = pygame.font.SysFont(None, 48, False, True)
score = 0
texto = fuente.render(f"Score: {score}", True, WHITE)