import pygame, os

screen=pygame.display.set_mode((864,936))

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

#loading and images
bg=pygame.image.load(os.path.join('flappyball','flappybirdbg.png'))
floor=pygame.image.load(os.path.join('flappyball','floor.png'))
pipe=pygame.image.load(os.path.join('flappyball','pipe.png'))
birdup=pygame.image.load(os.path.join('flappyball','birddown.png'))
screen.blit(bg,(0,0))
screen.blit(floor,(0,767))



running=True
while running:
    #drawing and scrolling the ground
    screen.blit(bg,(0,0))
    screen.blit(floor,(0,767))
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
    pygame.display.update()




