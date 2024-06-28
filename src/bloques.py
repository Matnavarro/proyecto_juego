import pygame
from random import *
from settings import *


def create_block(left=0, top=0, width=50, height=50, color=(255, 255, 255), dir=3, borde=0, radio=-1):
    return {"rect": pygame.Rect(left, top, width, height), "color": color, "dir": dir, "borde": borde, "radio": radio}

def create_player():
    rect_w = 50
    rect_h = 50
    posicion_random_x = randint(0, WIDTH - rect_w)
    posicion_random_y = randint(0, HEIGHT - rect_h)
    direccion_random = direcciones[randrange(len(direcciones))] # Direcciones es una tupla, con randrange elijo un indice al azar
                                                                # Randrange excluye el ultimo número [1,n)
    return create_block(posicion_random_x, posicion_random_y, rect_w, rect_h, dir = direccion_random, color = randint(0, WIDTH - rect_w), radio= rect_h // 2)

def create_coin():
    coin_width = 30
    coin_height = 30
    return create_block(randint(0, WIDTH - coin_width), randint(0, HEIGHT - coin_height), coin_width, coin_height, YELLOW, 0, 0, coin_height // 2)

def load_coin_list(lista:list, cantidad):
    for _ in range(cantidad):
        lista.append(create_coin())