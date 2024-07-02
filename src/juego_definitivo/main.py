from constantes import * 
from funciones import *
from ajustes import *

{
# move_left = False
# move_right = False
# move_up = False
# move_down = False

# pygame.init()

# clock = pygame.time.Clock()

# pygame.display.set_caption("Primer Jueguito")
# screen = pygame.display.set_mode(SCREEN_SIZE)
# fuente = pygame.font.SysFont(None, 48, False, True)
# score = 0
# texto = fuente.render(f"Score: {score}", True, WHITE)
}

jugador = create_player()
objeto = create_collectable()
proyectiles_lr = []#create_proyectile(0, HEIGHT // 2)c
proyectiles_rl = []#create_proyectile(0, HEIGHT // 2)c
proyectiles_tb = []#create_proyectile(0, HEIGHT // 2)c
proyectiles_bt = []#create_proyectile(0, HEIGHT // 2)c

imagen_proyectil = pygame.image.load("./src/assets/asteroide2.png")
#magen_jugador = pygame.image.load("./src/assets/bgnd.jpg")
#imagen_objeto = 

#proyectil.append(create_proyectile(0,0))
is_running = True

while is_running:
    clock.tick(FPS)

    screen.fill(BLACK)

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            is_running = False

        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT:
                print("izq")
                move_left = True
                move_right = False
                proyectiles_lr.append(create_projectile(0, jugador["rect"].centery, imagen_proyectil))

            if evento.key == pygame.K_RIGHT:
                print("der")
                move_right = True
                move_left = False
                proyectiles_rl.append(create_projectile(WIDTH, jugador["rect"].centery, imagen_proyectil))

            if evento.key == pygame.K_UP:
                print("arriba")
                move_up = True
                move_down = False
                proyectiles_tb.append(create_projectile(jugador["rect"].centerx, 0, imagen_proyectil))

            if evento.key == pygame.K_DOWN:
                print("abajo")
                move_down = True
                move_up = False
                proyectiles_bt.append(create_projectile(jugador["rect"].centerx, HEIGHT, imagen_proyectil))


        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_LEFT:
                move_left = False
            if evento.key == pygame.K_RIGHT:
                move_right = False
            if evento.key == pygame.K_UP:
                move_up = False
            if evento.key == pygame.K_DOWN:
                move_down = False

    move_player(jugador["rect"], move_left, move_right, move_up, move_down)


    for proyectil in proyectiles_lr[:]:  # Usamos [:] para iterar sobre una copia y poder eliminar mientras iteramos
        proyectil["rect"].x += PROJECTILE_SPEED
        #pygame.draw.rect(screen, proyectil["color"], proyectil["rect"], proyectil["borde"], proyectil["radio"])
        screen.blit(proyectil["img"], proyectil["rect"])

        if proyectil["rect"].left > WIDTH or detectar_colision(jugador["rect"], proyectil["rect"]):
            proyectiles_lr.remove(proyectil)

    for proyectil in proyectiles_rl[:]:
        proyectil["rect"].x -= PROJECTILE_SPEED
        #pygame.draw.rect(screen, proyectil["color"], proyectil["rect"], proyectil["borde"], proyectil["radio"])
        screen.blit(proyectil["img"], proyectil["rect"])
        if proyectil["rect"].right < 0 or detectar_colision(jugador["rect"], proyectil["rect"]):
            proyectiles_rl.remove(proyectil)

    for proyectil in proyectiles_tb[:]:  # Usamos [:] para iterar sobre una copia y poder eliminar mientras iteramos
        proyectil["rect"].y += PROJECTILE_SPEED
        screen.blit(proyectil["img"], proyectil["rect"])
        #pygame.draw.rect(screen, proyectil["color"], proyectil["rect"], proyectil["borde"], proyectil["radio"])
        if proyectil["rect"].top > HEIGHT or detectar_colision(jugador["rect"], proyectil["rect"]):
            proyectiles_tb.remove(proyectil)

    for proyectil in proyectiles_bt[:]:  # Usamos [:] para iterar sobre una copia y poder eliminar mientras iteramos
        proyectil["rect"].y -= PROJECTILE_SPEED
        screen.blit(proyectil["img"], proyectil["rect"])
        #pygame.draw.rect(screen, proyectil["color"], proyectil["rect"], proyectil["borde"], proyectil["radio"])
        if proyectil["rect"].bottom < 0 or detectar_colision(jugador["rect"], proyectil["rect"]):
            proyectiles_bt.remove(proyectil)

    if detectar_colision(jugador["rect"], objeto["rect"]):
        #objeto = None
        print("Colision!!!!")
        objeto = create_collectable()


    screen.blit(objeto["img"], objeto["rect"])
    #pygame.draw.rect(screen, objeto["color"], objeto["rect"], objeto["borde"], objeto["radio"])
    screen.blit(jugador["img"], jugador["rect"])
    #pygame.draw.rect(screen, jugador["color"], jugador["rect"], jugador["borde"], jugador["radio"])







    pygame.display.flip()

pygame.quit() 