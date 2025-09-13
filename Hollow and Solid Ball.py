import pygame

pygame.init()
#create the display surface
window = pygame.display.set_mode((400,400))
#fill the screen with white
window.fill((255,255,255))
#difine color
GREEN = (0,255,0)
#draw solid circle
pygame.draw.circle(window,GREEN,(300,300),50)
#Only outline
pygame.draw.circle(window,GREEN,(100,100),50,3)

#draw the surface to screen
pygame.display.update()
#game loop
running = True
while running:
    #event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

#quit pygame
pygame.quit()
