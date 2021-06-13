import pygame
import time
import random
 
pygame.init()
 
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)
 
ancho = 600
alto = 400
 
dis = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption('Snake por fckfck97')
 
clock = pygame.time.Clock()
 
snake_block = 10

 
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)
 
def Nivel(nivel):
    value = score_font.render("Nivel: " + str(nivel), True, yellow)
    dis.blit(value, [400, 0]) 

def Your_score(score):
    value = score_font.render("Tu Puntuacion: " + str(score), True, yellow)
    dis.blit(value, [0, 0])
 
 
 
def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])
 
 
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [ancho / 6, alto / 3])
 
 
def gameLoop():
    game_over = False
    game_close = False
 	
    x1 = ancho / 2
    y1 = alto / 2
 
    x1_change = 0
    y1_change = 0
 
    snake_List = []
    Length_of_snake = 1
 
    foodx = round(random.randrange(0, ancho - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, alto - snake_block) / 10.0) * 10.0
    
    mostrar_instrucciones = True
 

    while not game_over and mostrar_instrucciones:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True 
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    nivel = "Muy Facil"
                    speed = 5
                    inicio = 1
                    mostrar_instrucciones = False           
                if event.key == pygame.K_2:
                    nivel = "Facil"
                    speed = 15
                    inicio = 2
                    mostrar_instrucciones = False
                if event.key == pygame.K_3:
                    nivel = "Normal"
                    speed = 25
                    inicio = 3
                    mostrar_instrucciones = False
                if event.key == pygame.K_4:
                    nivel = "Dificil"
                    speed = 35
                    inicio = 4
                    mostrar_instrucciones = False
                if event.key == pygame.K_5:
                    game_over = True    

        texto = font_style.render("Snake Creado por fckfck97", True, white)
        dis.blit(texto, [10, 10])
        texto = font_style.render("En que modo quieres jugar muy facil, facil, normal o dificil", True, white)
        dis.blit(texto, [10, 40])
        texto = font_style.render("Presiona 1 para jugar en Modo Muy Facil", True, white)
        dis.blit(texto, [10, 70])
        texto = font_style.render("Presiona 2 para jugar en Modo Facil", True, white)
        dis.blit(texto, [10,100])
        texto = font_style.render("Presiona 3 para jugar en Modo Normal", True, white)
        dis.blit(texto, [10,130])
        texto = font_style.render("Presiona 4 para jugar en Modo Dificil", True, white)
        dis.blit(texto, [10,160])
        texto = font_style.render("Presiona 5 o la X para salir del juego", True, white)
        dis.blit(texto, [10,190])

        clock.tick(20)
        pygame.display.flip()

    while not game_over:
 
        while game_close == True:
            dis.fill(blue)
            texto = font_style.render("Perdiste, Presiona c para continuar o Presiona q para Salir", True, white)
            texto_rect = texto.get_rect()
            texto_x = dis.get_width() / 2 - texto_rect.width / 2
            texto_y = dis.get_height() / 2 - texto_rect.height / 2
            dis.blit(texto, [texto_x, texto_y])
            Your_score(Length_of_snake - 1)
            Nivel(nivel)
            pygame.display.update()
 
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False

                    if event.key == pygame.K_c:
                        dis.fill(black)
                        gameLoop()
 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0
 
        if x1 >= ancho or x1 < 0 or y1 >= alto or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        dis.fill(blue)
        pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]
 
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True
 
        our_snake(snake_block, snake_List)
        Your_score(Length_of_snake - 1)
        Nivel(nivel)

        pygame.display.update()
 
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, ancho - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, alto - snake_block) / 10.0) * 10.0
            Length_of_snake += 1
        
        if Length_of_snake == 11 and nivel == "Muy Facil":
            nivel = "Facil"
            speed = 15
        if Length_of_snake == 21 and nivel == "Facil" or Length_of_snake == 11 and nivel == "Facil" and inicio == 2:
            nivel = "Normal"
            speed = 25
        if Length_of_snake == 31 and nivel == "Normal" or Length_of_snake == 11 and nivel == "Normal" and inicio == 3:
            nivel = "Dificil"
            speed = 35
        if Length_of_snake == 41 and nivel == "Dificil" or Length_of_snake == 11 and nivel == "Dificil" and inicio == 4:
            nivel = "Muy Dificil"
            speed = 45
        
        clock.tick(speed)
 
    pygame.quit()
    quit()
 
 
gameLoop()