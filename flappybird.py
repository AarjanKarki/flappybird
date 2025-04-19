import pygame, os
import time
import random
import sys
pygame.init()
clock=pygame.time.Clock()
fps=60
WIDTH=864
HEIGHT=936
screen=pygame.display.set_mode((WIDTH,HEIGHT))
#define game variables
ground_scroll = 0
scroll_speed = 4
flying = True
pipe_gap = 150
game_over = False
pipe_frequency = 1500 #milliseconds
last_pipe = pygame.time.get_ticks() - pipe_frequency
score = 0
pass_pipe = False
floor_x=0
font_=pygame.font.SysFont('Comic Sans',50)




#loading and images
bg=pygame.image.load(os.path.join('flappyball','flappybirdbg.png'))
floor=pygame.image.load(os.path.join('flappyball','floor.png'))
pipe=pygame.image.load(os.path.join('flappyball','pipe.png'))

#checking if the pipe is facing up or down
pipeup=1

#showing text output on the screen
def drawtext(text,font,textcolor,x,y):
    mainfont=font.render(text,True,textcolor)
    screen.blit(mainfont,(x,y))



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
        self.vel+=0.5
        if self.vel>10:
            self.vel=10
        if self.rect.bottom<HEIGHT-50:
            self.rect.y+=int(self.vel)
        
        if game_over==False:
            #checking for jump
            if pygame.mouse.get_pressed()[0]==1 and self.clicked==False:
                self.clicked=True
                self.vel=-10
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
            #rotating the bird
            self.image=pygame.transform.rotate(self.images[self.index],self.vel*-2)
        else:
            self.image=pygame.transform.rotate(self.images[self.index],self.vel*-90)
            

        
        
        



class Pipes(pygame.sprite.Sprite):
    def __init__(self,x,y,pipeup):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load('C:/Users/amark/pygame2module/flappyball/pipe.png')
        self.rect=self.image.get_rect()
        if pipeup==1:
            self.image=pygame.transform.flip(self.image,False,True)
            self.rect.bottomleft=[x,y-pipe_gap//2]
        if pipeup==-1:
            self.rect.topleft=[x,y+pipe_gap//2]
        print('pipes constructor executed')
        #elif pipeup==-1:
    def update(self):
        self.rect.x-=scroll_speed
        if self.rect.right<0:
            self.kill()

#creating a bird group
birdgroup=pygame.sprite.Group()
pipegroup=pygame.sprite.Group()

flappy=Bird(100,HEIGHT//2)
birdgroup.add(flappy)
#creating a bird group

class Button():
    def __init__(self,image,x,y):
        self.image=image
        self.x=x
        self.y=y
        self.rect=self.image.get_rect(center=(self.x,self.y))
    
    #def updatebutton(self):


        

    def checkforinput(self,position):
        #position=pygame.mouse.get_pos()
        action=False
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top,self.rect.bottom):
            action=True
        screen.blit(self.image,self.rect)
        return(action)
    
button_surface=pygame.image.load(os.path.join('flappyball','restart.png'))
button=Button(button_surface,WIDTH//2,HEIGHT//2)

        
def reset_game():
    pipegroup.empty()
    flappy.rect.x=100
    flappy.rect.y=HEIGHT//2
    score=0
    return(score)
    







running=True
while running:
    #drawing and scrolling the ground
    clock.tick(fps)
    screen.blit(bg,(0,0))
    pipegroup.draw(screen)
    birdgroup.draw(screen)
    birdgroup.update()
    
    #scrolling the ground
    screen.blit(floor,(ground_scroll,768))
    #checking the score
    if len(pipegroup)>0:
        if birdgroup.sprites()[0].rect.left>pipegroup.sprites()[0].rect.left and\
        birdgroup.sprites()[0].rect.right<pipegroup.sprites()[0].rect.right and\
        pass_pipe==False:
            pass_pipe=True
        if pass_pipe==True:
            if birdgroup.sprites()[0].rect.left>pipegroup.sprites()[0].rect.right:
                score+=1
                pass_pipe=False

    for event in pygame.event.get():
        if event.type==pygame.MOUSEBUTTONDOWN and flying == False and game_over==False:
            flying=True
        if event.type==pygame.QUIT:
            running=False
        if event.type==pygame.MOUSEBUTTONDOWN and game_over==True:
            button.checkforinput(pygame.mouse.get_pos())
    #checking if the bird has hit the ground
    if flappy.rect.bottom>HEIGHT:
        game_over=True
        flying=False   
    if flying==True and game_over==False:
        #generating new pipes
        timenow=pygame.time.get_ticks()
        if timenow-last_pipe>pipe_frequency:
            pipeheight=random.randint(-100,100)
            bottompipe=Pipes(WIDTH,HEIGHT//2+pipeheight,-1)
            toppipe=Pipes(WIDTH,HEIGHT//2+pipeheight,1)
            pipegroup.add(bottompipe)
            pipegroup.add(toppipe)
            last_pipe=timenow
        
    
        
        ground_scroll-=scroll_speed
        if ground_scroll>+40:
            ground_scroll=0
        pipegroup.update()

    
    #checking for the collisoion
    if pygame.sprite.groupcollide(birdgroup,pipegroup,False,False) or flappy.rect.top<0:
        game_over=True
    #checking if the game is over if its hitting the ground or not flying
    if flappy.rect.bottom>HEIGHT:
        game_over=True
        flying=False
    drawtext(str(score),font_,'white',50,50)
    if game_over==True:
        if button.checkforinput(pygame.mouse.get_pos()):
            game_over=False
            score=reset_game()

        
    pygame.display.update()





