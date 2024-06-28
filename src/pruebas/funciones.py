import pygame

def analizar_elementos()->bool:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False