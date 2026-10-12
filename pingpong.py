import pygame
import sys

pygame.init()
WIDTH,HEIGHT=800, 400
WHITE=(255,255,255)
BLACK=(0,0,0)
FADEWHITE=(245, 255,255)
screen= pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Ping Pong")
running=True

player1 = pygame.Surface((10,80))
player1.fill(WHITE)
player1_x=20
player1_y=160
player1_speed=5

player2 = pygame.Surface((10,80))
player2.fill(WHITE)
player2_x=770
player2_y=160
player2_speed=5

divider = pygame.Surface((1,400))
divider.fill(FADEWHITE)
divider_x=390
divider_y=0

ball = pygame.Surface((20,20), pygame.SRCALPHA)
ball_x=380
ball_y = 180
speed_ball_x = 2
speed_ball_y = -0.5
pygame.draw.circle(ball, WHITE, (10,10), 10)         

clock = pygame.time.Clock()

while running:
    screen.fill(BLACK)
    key_get = pygame.key.get_pressed()
    for event in pygame.event.get():                  
            if key_get[pygame.K_q]:                 
                running = False  
            if key_get[pygame.K_w]:
                if player1_y > 0:
                    player1_y -= player1_speed
            if key_get[pygame.K_s]:
                if player1_y < 320:
                    player1_y += player1_speed             
            if key_get[pygame.K_i]:
                if player2_y > 0:
                    player2_y -= player2_speed
            if key_get[pygame.K_k]:
                if player2_y < 320:
                    player2_y += player2_speed  
            
    if ball_x == player2_x - 20 and ball_y in range(player2_y- 20, player2_y+80):
        speed_ball_x *= -1
        speed_ball_y *= -1
    if ball_x == player1_x and ball_y in range(player2_y- 20, player2_y+80):
        speed_ball_x =speed_ball_x * -1
        speed_ball_y = speed_ball_y * -1
        
    ball_x += speed_ball_x
    ball_y += speed_ball_y            
                
    screen.blit(player1, (player1_x, player1_y))
    screen.blit(player2, (player2_x, player2_y))
    screen.blit(divider, (divider_x, divider_y))
    screen.blit(ball, (ball_x,ball_y))
    pygame.display.update()
    
    clock.tick(60)
    

sys.exit()
pygame.quit()
