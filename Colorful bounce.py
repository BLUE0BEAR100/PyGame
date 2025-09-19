import pygame 
import random 

#init pygame
pygame.init()

#custom event ids for color change events
SPRITE_COLOR_CHANGE_EVENT = pygame.USEREVENT + 1
BACKGROUND_COLOR_CHANGE_EVENT = pygame.USEREVENT + 2

#Define basic colors using pygame.color
#Background colors
BLUE = pygame.Color('blue')
LIGHTBLUE = pygame.Color('lightblue')
DARKBLUE = pygame.Color('darkblue')

#sprite colors
YELLOW=pygame.Color('yellow')
MAGENTA =pygame.Color('magenta')
ORANGE =pygame.Color('orange')
WHITE = pygame.Color('white')


#Sprite sclass repeasenting the moving obj
class Sprite(pygame.sprite.Sprite):
    def __init__(self,color,height,width):
        super().__init__()
#create sprites surface with dimen and color
        self.image = pygame.Surface([width,height])
        self.image.fill(color)
        #get the sprite rect defining its pos and size
        self.rect=self.image.get_rect()
        #Set init velocity with random direction
        self.velocity = [random.choice([-1,1]),random.choice([-1,1])]

    #meth to update sprite pos
    def update(self):
        #moves the sprite by its velo
        self.rect.move_ip(self.velocity)
        #flag to track if the sprite hits a boundary
        boundary_hit=False
        #cheak for collision with left or right boundaries and reverse direct
        if self.rect.left <= 0 or self.rect.right>=500:
            self.velocity[0]=-self.velocity[0]
            boundary_hit=True
        if self.rect.top<= 0 or self.rect.bottom >=400:
            self.velocity[1]=-self.velocity[1]
            boundary_hit=True

        #if a boundary was hit post events to change colors
        if boundary_hit:
            pygame.event.post(pygame.event.Event(SPRITE_COLOR_CHANGE_EVENT))
            pygame.event.post(pygame.event.Event(BACKGROUND_COLOR_CHANGE_EVENT))
    def change_color(self):
        self.image.fill(random.choice([YELLOW,MAGENTA,ORANGE,WHITE]))

def change_background_color():
    global bg_color
    bg_color=random.choice([BLUE,LIGHTBLUE,DARKBLUE])

#Create a group to hold the sprite
all_sprites_list = pygame.sprite.Group()
#instantiate the sprite
sp1 =Sprite(WHITE,20,30)
#randomly pos the sprite
sp1.rect.x = random.randint(0,480)
sp1.rect.y = random.randint(0,370)
#add the sprite to the group
all_sprites_list.add(sp1)

#create the window
screen = pygame.display.set_mode((500,400))
#set the window tittle
pygame.display.set_caption("Colorful Bounce")
#set the initial background color
bg_color=BLUE
#apply the bg color
screen.fill(bg_color)
#game loop control flag
exit=False
#create a clock obj to control frame rate
clock = pygame.time.Clock()

#main game loop
while not exit:
    #event handling loop
    for event in pygame.event.get():
        #if the windows close button is clicked exit the game
        if event.type == pygame.QUIT:
            exit=True
        #if the sprite color chage is triggered change the sprites color
        elif event.type==SPRITE_COLOR_CHANGE_EVENT:
            sp1.change_color()
        elif event.type==BACKGROUND_COLOR_CHANGE_EVENT:
            change_background_color()

    #update all sprites
    all_sprites_list.update()
    #fill the screen with the curremt bg color
    screen.fill(bg_color)
    #Draw all sprites to the screen
    all_sprites_list.draw(screen)

    #refreash the display
    pygame.display.flip()
    #limit the frame rate to 240 fps
    clock.tick(240)
#unit all pygame modules and close window
pygame.quit()