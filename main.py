import pygame
import time
import random
pygame.init()
BACKGROUNDCOLOR = (32, 178, 170)
dis_width = 900
dis_height  = 600
snake_color = (224, 255, 255)
msg_color = (75, 0, 130)
food_color = (255, 255, 0)
score_color = (75, 0, 130)

dis=pygame.display.set_mode((dis_width, dis_height))

pygame.display.set_caption('Snake game by Nastushka')
clock = pygame.time.Clock()
 
block = 30
snake_speed = 10

x1_change = 0       
y1_change = 0
 
font_style = pygame.font.SysFont("TimesNewRoman", 25)
score_font = pygame.font.SysFont("TimesNewRoman", 25)

def Your_score(score):
    value = score_font.render("Your Score: " + str(score), True, score_color)
    dis.blit(value, [0, 0])

def our_snake(block, snake_list):
    header = snake_list[-1]
    pygame.draw.circle(dis, (220, 20, 60), [header[0] , header[1]], block/2)
    for x in snake_list[0:-1]:
        pygame.draw.circle(dis, snake_color, [x[0] , x[1]], block/2)

def message(msg,color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width/4, dis_height/2.5])

def message_1(msg,color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width/4, dis_height/3])

def gameLoop():
    game_over = False
    game_close = False
 
    x1 = random.randrange(block/2, dis_width - block/2 + 1, block)
    y1 = random.randrange(block/2, dis_height - block/2 + 1, block)
 
    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1
 
    foodx = random.randrange(block/2, dis_width - block/2 + 1, block)
    foody = random.randrange(block/2, dis_height - block/2 + 1, block)

    while not game_over:

        while game_close == True:
                dis.fill(BACKGROUNDCOLOR)
                message_1("You Lost! But don't be sad, that's okay.", msg_color)
                message("Press Q-Quit or C-Play Again", msg_color)
                
                pygame.display.update()
 
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_q:
                            game_over = True
                            game_close = False
                        if event.key == pygame.K_c:
                            gameLoop()

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                game_over=True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = block
                    x1_change = 0

        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True
 
        x1 += x1_change
        y1 += y1_change
        dis.fill(BACKGROUNDCOLOR)
            
        pygame.draw.circle(dis, food_color, [foodx, foody], block/3)

        snake_Head = [x1, y1]

        for x in snake_List[0:-1]:
            if x == snake_Head:
                game_close = True

        snake_List.append(snake_Head)

        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        our_snake(block, snake_List)
        Your_score(Length_of_snake - 1)

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = random.randrange(block/2, dis_width - block/2 + 1, block)
            foody = random.randrange(block/2, dis_height - block/2 + 1, block)
            Length_of_snake += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()

gameLoop()