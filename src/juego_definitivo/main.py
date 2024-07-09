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

NEW_PROJECTILE_EVENT = pygame.USEREVENT + 1
NEW_BOMB_EVENT = pygame.USEREVENT + 2
#NEW_LIFE_EVENT = pygame.USEREVENT + 3

pygame.time.set_timer(NEW_PROJECTILE_EVENT, 500)

bomb_timer = True

if bomb_timer:
    pygame.time.set_timer(NEW_BOMB_EVENT, 5000)


imagen_menu = pygame.image.load("./src/assets/images/menu_jgo.jpg")
imagen_menu = pygame.transform.scale(imagen_menu, (WIDTH, HEIGHT))

imagen_fondo = pygame.image.load("./src/assets/images/bgndd.jpg")
imagen_proyectil = pygame.image.load("./src/assets/images/asteroide2.png")
imagen_proyectil2 = pygame.image.load("./src/assets/images/asteroide.png")
imagen_objeto = pygame.image.load("./src/assets/images/verdes.png")
imagen_bomba = pygame.image.load("./src/assets/images/bomba3.png")

imagen_vida = pygame.image.load("./src/assets/images/corazon.png")
imagen_vida = pygame.transform.scale(imagen_vida, (30, 30))

sonido_score = pygame.mixer.Sound("./src/assets/sounds/point.mp3")
sonido_damage = pygame.mixer.Sound("./src/assets/sounds/impacto.mp3")


#magen_jugador = pygame.image.load("./src/assets/bgnd.jpg")
#imagen_objeto =

jugador = create_player()
objeto = create_collectable(imagen_objeto)
bomba = create_collectable(imagen_bomba)
proyectiles_lr = []
proyectiles_rl = []
proyectiles_tb = []
proyectiles_bt = []
proyectil_random = []
vidas = 3
score = 0
#proyectil.append(create_proyectile(0,0))
is_running = True
menu = True

while is_running:
    clock.tick(FPS)
   # presionar_boton((0,50), (0, 50), "hola", 60, 60)
    texto = fuente.render(f"Score: {score}", True, MAGENTA)

    if menu:
        menu_principal(imagen_menu)
        menu = False
    # screen.fill(BLACK)
    imagen_fondo = pygame.transform.scale(imagen_fondo, (WIDTH, HEIGHT))
    screen.blit(imagen_fondo, (0,0))

    for evento in pygame.event.get():
        #manejo_eventos(evento, proyectiles_lr, proyectiles_rl, proyectiles_tb, proyectiles_bt)
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
        # if evento.type == NEW_LIFE_EVENT:
        #     new_coin = create_coin()
        #     new_coin["color"] = RED
        #     coins.append(new_coin)

    move_player(jugador["rect"], move_left, move_right, move_up, move_down)


    for proyectil in proyectiles_lr[:]:
        proyectil["rect"].x += PROJECTILE_SPEED
        #pygame.draw.rect(screen, proyectil["color"], proyectil["rect"], proyectil["borde"], proyectil["radio"])
        screen.blit(proyectil["img"], proyectil["rect"])

        if proyectil["rect"].left > WIDTH: 
            proyectiles_lr.remove(proyectil)

        vidas = damage(jugador, proyectil, proyectiles_lr, vidas, sonido_damage)          


    for proyectil in proyectiles_rl[:]:
        proyectil["rect"].x -= PROJECTILE_SPEED
        #pygame.draw.rect(screen, proyectil["color"], proyectil["rect"], proyectil["borde"], proyectil["radio"])
        screen.blit(proyectil["img"], proyectil["rect"])
        if proyectil["rect"].right < 0:
            proyectiles_rl.remove(proyectil)
        vidas = damage(jugador, proyectil, proyectiles_rl, vidas, sonido_damage)          


    for proyectil in proyectiles_tb[:]:
        proyectil["rect"].y += PROJECTILE_SPEED
        #pygame.draw.rect(screen, proyectil["color"], proyectil["rect"], proyectil["borde"], proyectil["radio"])
        screen.blit(proyectil["img"], proyectil["rect"])
        if proyectil["rect"].top > HEIGHT:
            proyectiles_tb.remove(proyectil)

        vidas = damage(jugador, proyectil, proyectiles_tb, vidas, sonido_damage)          

    for proyectil in proyectiles_bt[:]:
        proyectil["rect"].y -= PROJECTILE_SPEED
        #pygame.draw.rect(screen, proyectil["color"], proyectil["rect"], proyectil["borde"], proyectil["radio"])
        screen.blit(proyectil["img"], proyectil["rect"])
        if proyectil["rect"].bottom < 0:
            proyectiles_bt.remove(proyectil)
            
        vidas = damage(jugador, proyectil, proyectiles_bt, vidas, sonido_damage)          
  

    if detectar_colision(jugador["rect"], objeto["rect"]):
        print("OBJETO")
        objeto = create_collectable(imagen_objeto)
        score +=1
        sonido_score.play()

    if detectar_colision(jugador["rect"], bomba["rect"]):
        print("BOMBA")
        bomba["rect"].x = WIDTH + 200 #create_collectable(imagen_bomba)
        delete_projectiles(proyectiles_lr, proyectiles_rl, proyectiles_tb, proyectiles_bt)
        bomb_timer = True

    screen.blit(objeto["img"], objeto["rect"])
    screen.blit(bomba["img"], bomba["rect"])
    #pygame.draw.rect(screen, objeto["color"], objeto["rect"], objeto["borde"], objeto["radio"])
    #screen.blit(jugador["img"], jugador["rect"])
    pygame.draw.rect(screen, jugador["color"], jugador["rect"], jugador["borde"], jugador["radio"])
    screen.blit(texto,(0,0))
    
    if vidas > 0:
        dibujar_vidas(vidas, imagen_vida)
    else:
        game_over(score)
        delete_projectiles(proyectiles_lr, proyectiles_rl, proyectiles_tb, proyectiles_bt)
        menu = True
        vidas = 3

        
    #if not impacto:
    #    screen.blit(imagen_objeto,(0,30))
    pygame.display.flip()

pygame.quit() 