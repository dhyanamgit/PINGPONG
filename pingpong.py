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
score_1 = 0
score_2=0
font = pygame.font.SysFont('None', 40)

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

def display_text(text, x,y):
    display = font.render(text, True, WHITE)
    screen.blit(display,(x,y))

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
            
        
    if ball_y < 0 or ball_y > 380:
        speed_ball_y *= -1   
        
    if ball_x + 20 >= player2_x and player2_y-20 <= ball_y <= player2_y + 80:
        speed_ball_x *= -1
    if ball_x <= player1_x + 10 and player1_y - 20 <= ball_y <= player1_y +80:
        speed_ball_x *= -1
                
    ball_x += speed_ball_x
    ball_y += speed_ball_y            
                
    screen.blit(player1, (player1_x, player1_y))
    screen.blit(player2, (player2_x, player2_y))
    screen.blit(divider, (divider_x, divider_y))
    screen.blit(ball, (ball_x,ball_y))
    
    
    if ball_x > 800:
        score_1 += 1
        ball_x = 380
        ball_y = 180
    
    if ball_x < 0:
        score_2 += 1
        ball_x = 380
        ball_y = 180
            
    display_text(str(score_1), 50, 10)
    display_text(str(score_2), 750, 10)
    pygame.display.update()
    
    clock.tick(60)
        
sys.exit()
pygame.quit()
