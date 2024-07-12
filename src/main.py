from constantes import * 
from funciones import *
from ajustes import *

pygame.init()

vidas = VIDAS
score = 0
highscore = read_highscore()
inmunidad = False
timer_inmunidad = 0
duracion_inmunidad = 1000
inmunidad_cooldown = 2000
ultima_inmunidad = 0

while is_running:
    tiempo_actual = pygame.time.get_ticks()
    clock.tick(FPS)
    texto = fuente.render(f"Score: {score}", True, MAGENTA)

    if menu:
        menu_principal(imagen_menu)
        menu = False
        jugador = create_player(imagen = imagen_jugador)
        objeto = create_collectable(imagen_objeto)
        bomba = create_collectable(imagen_bomba)


    screen.fill(CYAN)
    #screen.blit(imagen_fondo, (0,0))

    for evento in pygame.event.get():

        if evento.type == pygame.QUIT:
            is_running = False

        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT:
                print("izq")
                move_left = True
                move_right = False
                # move_down = False
                # move_up = False
                proyectiles_lr.append(create_projectile(0, jugador["rect"].centery, imagen_proyectil))

            if evento.key == pygame.K_RIGHT:
                print("der")
                move_right = True
                move_left = False
                # move_down = False
                # move_up = False
                proyectiles_rl.append(create_projectile(WIDTH, jugador["rect"].centery, imagen_proyectil))

            if evento.key == pygame.K_UP:
                print("arriba")
                move_up = True
                move_down = False
                # move_left = False
                # move_right = False
                proyectiles_tb.append(create_projectile(jugador["rect"].centerx, 0, imagen_proyectil))

            if evento.key == pygame.K_DOWN:
                print("abajo")
                move_down = True
                move_up = False
                # move_left = False
                # move_right = False
                proyectiles_bt.append(create_projectile(jugador["rect"].centerx, HEIGHT, imagen_proyectil))

            if evento.key == pygame.K_SPACE:
                #inmunidad = True
                if not inmunidad and pygame.time.get_ticks() - ultima_inmunidad > inmunidad_cooldown:
                    inmunidad = True
                    timer_inmunidad = tiempo_actual
                    ultima_inmunidad = tiempo_actual

            if evento.key == pygame.K_p:
                pausa(pygame.K_p, imagen_pausa)
                move_left = False
                move_right = False
                move_up = False
                move_down = False
                print("pausa jeje")

        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_LEFT:
                move_left = False
            if evento.key == pygame.K_RIGHT:
                move_right = False
            if evento.key == pygame.K_UP:
                move_up = False
            if evento.key == pygame.K_DOWN:
                move_down = False

        if evento.type == NEW_PROJECTILE_EVENT:
            create_random_projectile(proyectiles_lr, proyectiles_rl, proyectiles_tb, proyectiles_bt, imagen_proyectil2)
        
        if evento.type == NEW_BOMB_EVENT:
            if bomb_timer:
                bomba = create_collectable(imagen_bomba)
                bomb_timer = False
            print(bomba)

    move_player(jugador["rect"], move_left, move_right, move_up, move_down)

#-------------------------------------------------------------------------------------
    for proyectil in proyectiles_lr[:]:
        move_proyectil_lr(proyectil, proyectiles_lr)
        vidas = damage(jugador, proyectil, proyectiles_lr, vidas, sonido_damage, inmunidad)          

    for proyectil in proyectiles_rl[:]:
        move_proyectil_rl(proyectil, proyectiles_rl)
        vidas = damage(jugador, proyectil, proyectiles_rl, vidas, sonido_damage, inmunidad)          

    for proyectil in proyectiles_tb[:]:
        move_proyectil_tb(proyectil, proyectiles_tb)
        vidas = damage(jugador, proyectil, proyectiles_tb, vidas, sonido_damage, inmunidad)          

    for proyectil in proyectiles_bt[:]:
        move_proyectil_bt(proyectil, proyectiles_bt)   
        vidas = damage(jugador, proyectil, proyectiles_bt, vidas, sonido_damage, inmunidad)
#-------------------------------------------------------------------------------------

    if detectar_colision(jugador["rect"], objeto["rect"]):
        print("OBJETO")
        objeto = create_collectable(imagen_objeto)
        score +=1
        sonido_score.play()

    if detectar_colision(jugador["rect"], bomba["rect"]):
        print("BOMBA")
        sonido_bomba.play()
        bomba["rect"].x = WIDTH + 200
        delete_all_projectiles(proyectiles_lr, proyectiles_rl, proyectiles_tb, proyectiles_bt)
        bomb_timer = True

    screen.blit(objeto["img"], objeto["rect"])
    screen.blit(bomba["img"], bomba["rect"])

    if inmunidad:
        if (tiempo_actual - timer_inmunidad) > duracion_inmunidad:
            inmunidad = False
        pygame.draw.rect(screen, jugador["color"], jugador["rect"])
    else:
        screen.blit(jugador["img"], jugador["rect"])
    screen.blit(texto,(0,0))
    
    if vidas > 0:
        dibujar_vidas(vidas, imagen_vida)
    else:
        menu = game_over(score, highscore, sonido = sonido_gameover)
        delete_all_projectiles(proyectiles_lr, proyectiles_rl, proyectiles_tb, proyectiles_bt)
        highscore = read_highscore()
        #save_highscore(highscore)
        score = 0
        vidas = VIDAS
        move_left = False
        move_right = False
        move_up = False
        move_down = False
        jugador["rect"].center = SCREEN_CENTER


    pygame.display.flip()

terminar()