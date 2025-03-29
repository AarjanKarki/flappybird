import pygame, os
import time
import random
clock=pygame.time.Clock()
WIDTH=864
HEIGHT=936
screen=pygame.display.set_mode((WIDTH,HEIGHT))

#define game variables
ground_scroll = 0
scroll_speed = 0.5
flying = True
game_over = False
pipe_gap = 150
pipe_frequency = 1500 #milliseconds
last_pipe = pygame.time.get_ticks() - pipe_frequency
score = 0
pass_pipe = False
floor_x=0


#creating a bird group
birdgroup=pygame.sprite.Group()
pipegroup=pygame.sprite.Group()

#loading and images
bg=pygame.image.load(os.path.join('flappyball','flappybirdbg.png'))
floor=pygame.image.load(os.path.join('flappyball','floor.png'))
pipe=pygame.image.load(os.path.join('flappyball','pipe.png'))

#checking if the pipe is facing up or down
pipeup=1

class Bird(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.images=[]
        self.index=0
        self.counter=0
        for num in range(1,4):
            image=pygame.image.load(f'C:/Users/amark/pygame2module/flappyball/bird{num}.png')
            self.images.append(image)
        self.image=self.images[self.index]
        self.rect=self.image.get_rect()
        self.rect.center=[x,y]
        self.vel=0
        self.clicked=False
    def update(self):
        #applying gravity
        self.vel+=0.01
        if self.vel>2:
            self.vel=2
        if self.rect.bottom<HEIGHT-50:
            self.rect.y+=int(self.vel)
        
        if game_over==False:
            #checking for jump
            if pygame.mouse.get_pressed()[0]==1 and self.clicked==False:
                self.clicked=True
                self.vel-=7.5
            if pygame.mouse.get_pressed()[0]==0:
                self.clicked=False
        #adding animation
            self.counter+=1
            flap_cooldown=5
            if self.counter>flap_cooldown:
                self.counter=0
                self.index+=1
                if self.index>=len(self.images):
                    self.index=0
                self.image=self.images[self.index]

            

        
        
        



class Pipes(pygame.sprite.Sprite):
    def __init__(self,x,y,pipeup):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load('C:/Users/amark/pygame2module/flappyball/pipe.png')
        self.rect=self.image.get_rect()
        if pipeup==1:
            self.image=pygame.transform.flip(self.image,False,True)
            self.rect.bottomleft=[x,y-pipe_gap//2]
        elif pipeup==-1:
            self.rect.topleft=[x,y+pipe_gap//2]
            
        #elif pipeup==-1:
    def update(self):
        self.rect.x-=scroll_speed
        if self.rect.right<0:
            self.kill()


flappy=Bird(100,HEIGHT//2)
birdgroup.add(flappy)


        







running=True
while running:
    #drawing and scrolling the ground
    screen.blit(bg,(0,0))
    birdgroup.draw(screen)
    pipegroup.draw(screen)
    birdgroup.update()
    pipegroup.update()
    screen.blit(floor,(floor_x,767))
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
    if flying==True and game_over==False:
        #generating new pipes
        timenow=pygame.time.get_ticks()
        if timenow-last_pipe>pipe_frequency:
            pipeheight=random.randint(0,100)
            bottompipe=Pipes(WIDTH,HEIGHT//2+pipeheight,1)
            pipegroup.add(bottompipe)
            last_pipe=timenow

            
    pipegroup.update()
    floor_x-=scroll_speed
    if floor_x<-30:
        floor_x=0



    pygame.display.update()





