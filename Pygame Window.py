#import necessary libraries
import pygame

#Initialize
pygame.init()

#setup window geometry
screen = pygame.display.set_mode((400,500))

#create a loop to run till the game is quit by the user
done = False

while not done:

    #Clear the event que
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()

    #make changes visible
    pygame.display.flip()