import pygame, os
import time
WIDTH=864
HEIGHT=936
screen=pygame.display.set_mode((WIDTH,HEIGHT))

#define game variables
ground_scroll = 0
scroll_speed = 4
flying = False
game_over = False
pipe_gap = 150
pipe_frequency = 1500 #milliseconds
last_pipe = pygame.time.get_ticks() - pipe_frequency
score = 0
pass_pipe = False
floor_x=0

#loading and images
bg=pygame.image.load(os.path.join('flappyball','flappybirdbg.png'))
floor=pygame.image.load(os.path.join('flappyball','floor.png'))
pipe=pygame.image.load(os.path.join('flappyball','pipe.png'))

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
flappy=Bird(100,HEIGHT//2)



        







running=True
while running:
    #drawing and scrolling the ground
    screen.blit(bg,(0,0))
    screen.blit(floor,(floor_x,767))
    floor_x-=0.5
    flappy.draw()
    if floor_x<-30:
        floor_x=0
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
    pygame.display.update()





