import pygame
from sys import exit
pygame.init()

screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Runner Boy Run')
clock = pygame.time.Clock()
test_font = pygame.font.Font('font\pixeltype.ttf', 50)

sky_surface = pygame.image.load('graphics/sky.png').convert()
ground_surface = pygame.image.load('graphics/ground.png').convert()

score_surf = test_font.render('Score: ', False, (64, 64, 64))
score_rect = score_surf.get_rect(center = (350, 50))

snail_surface = pygame.image.load('graphics\snail\snail1.png').convert_alpha()
snail_rect = snail_surface.get_rect(bottomright = (600, 300))

player_surface = pygame.image.load('graphics\player\player_walk_1.png').convert_alpha()
player_rect = player_surface.get_rect(midbottom = (80,300))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            # exit cancels all the code (no errors)
            exit()
#         if event.type == pygame.MOUSEMOTION:
            
     
    screen.blit(sky_surface, (0,0))
    screen.blit(ground_surface, (0, 300))
    
    
    
    pygame.draw.rect(screen, '#c0e8ec', score_rect)
    pygame.draw.rect(screen, '#c0e8ec', score_rect, 15)
    screen.blit(score_surf,(score_rect))
   
    snail_rect.x -= 4
    if snail_rect.right <= 0: snail_rect.x=left = 800    
    screen.blit(snail_surface, snail_rect)
    screen.blit(player_surface, player_rect)
    
    # collision
#      if player_rect.colliderect(snail_rect):
#     mouse_pos = pygame.mouse.get_pos()
#     if player_rect.collidepoint(mouse_pos):
        
        
    
                
    # draw all our elements
    # update everything
    pygame.display.update()
    # Ceiling of the FPS
    clock.tick(60)
    