import pygame
import random
pygame.mixer.init()
#Sounds
music = pygame.mixer.music.load('sounds/African_fun_long.mp3')
wingssound=pygame.mixer.Sound('sounds/wings.wav')
explodesound=pygame.mixer.Sound('sounds/explode.mp3')
pygame.mixer.music.play(-1)
# Game Variables
LUNGIME, LATIME=900, 500 #window sizes
WIN=pygame.display.set_mode((LUNGIME,LATIME)) #creating window
pygame.display.set_caption("Flappy Bird") #title
FPS=70
jump=False
score=0
gens=0
high_score=0

#images
bg_img=pygame.image.load("imgs/background2.jpg")
treeup_img=pygame.image.load("imgs/treeup.png")
birdup_img=pygame.image.load("imgs/birdup.png")
birddown_img=pygame.image.load("imgs/birddown.png")
birdmid_img=pygame.image.load("imgs/birdmid.png")
arrow_img=pygame.image.load("imgs/arrow.png")

#rescaling the images
arrow=pygame.transform.scale(arrow_img,(40,40))
birddown=pygame.transform.scale(birddown_img,(60,60))
birdmid=pygame.transform.scale(birdmid_img,(60,60))
birdup=pygame.transform.scale(birdup_img,(60,60))
birdlist=[birdup, birdmid, birddown]
bg=pygame.transform.scale(bg_img, (LUNGIME, LATIME))

clock = pygame.time.Clock()

#random variables to determinate the pipe height
rand1 = random.randrange(40, 240)
rand2 = random.randrange(40, 240)
rand3 = random.randrange(40, 240)
rand4 = random.randrange(40, 240)
rand5 = random.randrange(40, 240)
rand6 = random.randrange(40, 240)

#the top side of pipes surfaces
treeup_surface1=pygame.transform.scale(treeup_img,(90,rand1))
treeup_surface2=pygame.transform.scale(treeup_img,(90,rand2))
treeup_surface3=pygame.transform.scale(treeup_img,(90,rand3))
treeup_surface4=pygame.transform.scale(treeup_img,(90,rand4))
treeup_surface5=pygame.transform.scale(treeup_img,(90,rand5))
treeup_surface6=pygame.transform.scale(treeup_img,(90,rand6))

#the bottom side of pipes surfaces
treedown_surface1=pygame.transform.scale(treeup_img,(90,415-rand1-130))
treedown_surface1=pygame.transform.flip(treedown_surface1,False,True)

treedown_surface2=pygame.transform.scale(treeup_img,(90,415-rand2-130))
treedown_surface2=pygame.transform.flip(treedown_surface2,False,True)

treedown_surface3=pygame.transform.scale(treeup_img,(90,415-rand3-130))
treedown_surface3=pygame.transform.flip(treedown_surface3,False,True)

treedown_surface4=pygame.transform.scale(treeup_img,(90,415-rand4-130))
treedown_surface4=pygame.transform.flip(treedown_surface4,False,True)

treedown_surface5=pygame.transform.scale(treeup_img,(90,415-rand5-130))
treedown_surface5=pygame.transform.flip(treedown_surface5,False,True)

treedown_surface6=pygame.transform.scale(treeup_img,(90,415-rand6-130))
treedown_surface6=pygame.transform.flip(treedown_surface6,False,True)
