import pygame, sys
import random
import neat
import os

pygame.init()
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




class Bird:  #Bird Class
    x=45
    y=250
    birdindex=0
    tick_count=0
    counter=0
    vel = 0
    height=y

    def jump(self): #Jump function
        self.vel=-10.5
        self.tick_count=0
        self.height=self.y

def draw_window(): # Update the window
    pygame.display.update()

def AI_display(birds): #On AI part of game, the function prints on which generation we are in this moment, and the birds alive.
    gens_font = pygame.font.Font("imgs/04B_19.TTF", 30)
    gens_surface = gens_font.render("Gen: " + str(gens), False, (0, 0, 0))
    birds_surface=gens_font.render("Alive:" + str(len(birds)), False, (0, 0, 0))
    gens_rect = gens_surface.get_rect(center=(60, 30))
    birds_rect=birds_surface.get_rect(center=(60,80))
    WIN.blit(gens_surface, gens_rect)
    WIN.blit(birds_surface, birds_rect)

def score_display(): #On SP part of game , the function prints the score(how many pipes we passed)

    score_font = pygame.font.Font("imgs/04B_19.TTF", 20)
    score_surface = score_font.render("Score: " + str(score), False, (0, 0, 0))
    score_rect = score_surface.get_rect(center=(LUNGIME / 4 * 5.5 / 3, 50))
    WIN.blit(score_surface, score_rect)

def pause(): #shows us the pause window
    global score, gens
    WIN.blit(bg, (0, 0))
    fontpause=pygame.font.Font('freesansbold.ttf', 80) # font and dimensions
    fontpause2 = pygame.font.Font('freesansbold.ttf', 30) # font and dimensions
    pause=fontpause.render('Pause',True,(255,255,255)) # text
    text=fontpause2.render('Press Q to quit the game , press space to continue',True,(255,255,255)); # text
    text2=fontpause2.render('or M to return to main menu.',True,(255,255,255)); # text
    pauseRect=pause.get_rect()
    textRect=text.get_rect()
    text2Rect=text2.get_rect()
    pauseRect.center=(LUNGIME//2,LATIME//2) #position of rect on window
    textRect.center=(LUNGIME//2,3*LATIME/4) #position of rect on window
    text2Rect.center=(LUNGIME//2,3*LATIME/3.5) #position of rect on window
    pauza=True
    while pauza:
        WIN.blit(pause,pauseRect)
        WIN.blit(text, textRect)
        WIN.blit(text2, text2Rect)
        clock.tick(30)
        draw_window()
        userInput = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type==pygame.QUIT: #if the x of the windows is pressed
                pygame.quit() # end the game
                sys.exit()
            if userInput[pygame.K_q]: # if the q key is pressed
                pygame.quit() # end the game
                sys.exit()
            if userInput[pygame.K_m]: # if the m key is pressed
                config = neat.config.Config(neat.DefaultGenome, neat.DefaultReproduction, neat.DefaultSpeciesSet,
                                            neat.DefaultStagnation, config_path)
                p = neat.Population(config)
                p.add_reporter(neat.StdOutReporter(True))
                stats = neat.StatisticsReporter()
                p.add_reporter(stats)
                score=0
                gens=0
                main_menu(p)
                pauza=False
            if userInput[pygame.K_SPACE]: # if space is pressed
                pauza=False # the game starts

def main_menu(p): #main menu
    arrowRect = pygame.Rect(LUNGIME // 2.6, LATIME // 2.8, 40, 40)
    WIN.blit(bg, (0, 0))
    WIN.blit(arrow, arrowRect)
    fontmenu1 = pygame.font.Font('freesansbold.ttf', 40)
    menu1 = fontmenu1.render('Quit', True, (255, 255, 255),(0,0,0))
    menu1Rect = menu1.get_rect()
    menu1Rect.center = (LUNGIME // 2, LATIME // 2)
    menu2 = fontmenu1.render('Play AI', True, (255, 255, 255), (0, 0, 0))
    menu2Rect = menu2.get_rect()
    menu2Rect.center = (LUNGIME // 2, LATIME // 2.5)
    menu3 = fontmenu1.render('Play SP', True, (255, 255, 255), (0, 0, 0))
    menu3Rect=menu3.get_rect()
    menu3Rect.center=(LUNGIME // 2, LATIME // 3.3)
    UP=2
    loop = True
    while loop:

        WIN.blit(menu1, menu1Rect)
        WIN.blit(menu2, menu2Rect)
        WIN.blit(menu3, menu3Rect)
        clock.tick(FPS)
        draw_window()
        userInput = pygame.key.get_pressed()
        if UP == 2: #if we are on "play sp"
            # draw the arrow
            arrowRect = pygame.Rect(LUNGIME // 2.6, LATIME // 3.8, 40, 40)
            WIN.blit(bg, (0, 0))
            WIN.blit(arrow, arrowRect)
        if UP == 1: #if we are on "play ai "
            # draw the arrow
            arrowRect = pygame.Rect(LUNGIME // 2.6, LATIME // 2.8, 40, 40)
            WIN.blit(bg, (0, 0))
            WIN.blit(arrow, arrowRect)
        if UP == 0: #if we are on "quit"
            # draw the arrow
            arrowRect = pygame.Rect(LUNGIME // 2.6, LATIME // 2.2, 40, 40)
            WIN.blit(bg, (0, 0))
            WIN.blit(arrow, arrowRect)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if userInput[pygame.K_SPACE]:
                if UP == 1:
                    pygame.time.delay(10)
                    winner = p.run(main_AI, 200) # run the ai game
                    loop=False
                if UP == 2:
                    pygame.time.delay(10)
                    main_SP() # run the sp game
                    loop=False
                if UP == 0:
                    pygame.quit() # quit the game
                    sys.exit()
            if userInput[pygame.K_UP]: # if the arrow up key is pressed
                UP=UP+1 # Up increments
                if UP >= 2: # if up is greater than 2
                    UP=2

            if userInput[pygame.K_DOWN]: # if the arrow down key is pressed
                UP=UP-1 # up decrements
                if UP<=0:
                    UP=0


def game_over():
    global high_score
    WIN.blit(bg, (0, 0))
    if score > high_score: # if current score is greater than the high score
        high_score=score
        # fonts and rects of the texts
    font = pygame.font.Font('freesansbold.ttf', 64)
    font2 = pygame.font.Font('freesansbold.ttf', 22)
    text = font.render('Game over!', True, (255,255,255), (0,0,0))
    scoregameover=font2.render('Score: '+str(score),True,(255,255,255),(0,0,0))
    highscoregameover = font2.render('High score: ' + str(high_score), True, (255, 255, 255), (0, 0, 0))
    text2 = font2.render('Press any key to continue.', True, (255, 255, 255), (0, 0, 0))
    scoregameoverRect=scoregameover.get_rect()
    highscoregameoverRect= highscoregameover.get_rect()
    textRect = text.get_rect()
    textRect2 = text2.get_rect()
    scoregameoverRect.center=(LUNGIME/2,LATIME*1.5/4)
    highscoregameoverRect.center=(LUNGIME/2,LATIME*1.8/4)
    textRect.center = (LUNGIME // 2, LATIME // 4)
    textRect2.center = (LUNGIME // 2, LATIME * 3 // 4)
    waiting=True
    while waiting:
        # draw the texts
        WIN.blit(text, textRect)
        WIN.blit(text2, textRect2)
        WIN.blit(scoregameover,scoregameoverRect)
        WIN.blit(highscoregameover, highscoregameoverRect)
        clock.tick(FPS)
        draw_window()
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN: # if any key is pressed
                waiting=False # the game starts again


def swap(r1,r2): # swap 2 variables
    a=r1
    r1=r2
    r2=a
    return r1,r2

def main_SP(): # Single Player game
    b = Bird() # the bird object

    #variables
    global rand1, rand2, rand3, rand4, rand5, rand6, jump, vel, treeup_surface1, treeup_surface2, treeup_surface3, treeup_surface4, treeup_surface5, treeup_surface6
    global treedown_surface1, treedown_surface2, treedown_surface3, treedown_surface4, treedown_surface5, treedown_surface6, birdlist, score
    run = True
    i = 0

    while run:

        WIN.blit(bg, (i, 0))
        WIN.blit(bg, (LUNGIME + i, 0))

        rectbird = pygame.Rect(int(b.x) - 30, int(b.y) - 30, 60, 60)
        WIN.blit(birdlist[b.birdindex], rectbird)
        # counter how fast the bird is flapping the wings.
        b.counter += 1

        if b.counter > 5:
            b.counter = 0
            b.birdindex += 1

        if b.birdindex >= 2:
            b.birdindex = 0

        #the rectangles for the pipes
        rect1 = pygame.Rect(210 + i, 0, 90, rand1)
        rect1down = pygame.Rect(210 + i, rand1 + 130, 90, 415 - rand1 - 130)

        rect2 = pygame.Rect(510 + i, 0, 90, rand2)
        rect2down = pygame.Rect(510 + i, rand2 + 130, 90, 415 - rand2 - 130)

        rect3 = pygame.Rect(810 + i, 0, 90, rand3)
        rect3down = pygame.Rect(810 + i, rand3 + 130, 90, 415 - rand3 - 130)

        rect4 = pygame.Rect(210 + i + LUNGIME, 0, 90, rand4)
        rect4down = pygame.Rect(210 + i + LUNGIME, rand4 + 130, 90, 415 - rand4 - 130)

        rect5 = pygame.Rect(510 + i + LUNGIME, 0, 90, rand5)
        rect5down = pygame.Rect(510 + i + LUNGIME, rand5 + 130, 90, 415 - rand5 - 130)

        rect6 = pygame.Rect(810 + i + LUNGIME, 0, 90, rand6)
        rect6down = pygame.Rect(810 + i + LUNGIME, rand6 + 130, 90, 415 - rand6 - 130)

        #drawing the pipes
        WIN.blit(treeup_surface1, rect1)
        WIN.blit(treedown_surface1, rect1down)

        WIN.blit(treeup_surface2, rect2)
        WIN.blit(treedown_surface2, rect2down)

        WIN.blit(treeup_surface3, rect3)
        WIN.blit(treedown_surface3, rect3down)

        WIN.blit(treeup_surface4, rect4)
        WIN.blit(treedown_surface4, rect4down)

        WIN.blit(treeup_surface5, rect5)
        WIN.blit(treedown_surface5, rect5down)

        WIN.blit(treeup_surface6, rect6)
        WIN.blit(treedown_surface6, rect6down)

        i -= 3 # i is decreasing for the moving effect

        if i == -LUNGIME: # if the first image has passed
            i = 0
            # render the new pipes
            rand1, rand4 = swap(rand1, rand4)
            rand2, rand5 = swap(rand2, rand5)
            rand3, rand6 = swap(rand3, rand6)
            rand4 = random.randrange(40, 240)
            rand5 = random.randrange(40, 240)
            rand6 = random.randrange(40, 240)

            treeup_surface1 = pygame.transform.scale(treeup_img, (90, rand1))
            treeup_surface2 = pygame.transform.scale(treeup_img, (90, rand2))
            treeup_surface3 = pygame.transform.scale(treeup_img, (90, rand3))
            treeup_surface4 = pygame.transform.scale(treeup_img, (90, rand4))
            treeup_surface5 = pygame.transform.scale(treeup_img, (90, rand5))
            treeup_surface6 = pygame.transform.scale(treeup_img, (90, rand6))

            treedown_surface1 = pygame.transform.scale(treeup_img, (90, 415 - rand1 - 130))
            treedown_surface1 = pygame.transform.flip(treedown_surface1, False, True)
            treedown_surface2 = pygame.transform.scale(treeup_img, (90, 415 - rand2 - 130))
            treedown_surface2 = pygame.transform.flip(treedown_surface2, False, True)
            treedown_surface3 = pygame.transform.scale(treeup_img, (90, 415 - rand3 - 130))
            treedown_surface3 = pygame.transform.flip(treedown_surface3, False, True)
            treedown_surface4 = pygame.transform.scale(treeup_img, (90, 415 - rand4 - 130))
            treedown_surface4 = pygame.transform.flip(treedown_surface4, False, True)
            treedown_surface5 = pygame.transform.scale(treeup_img, (90, 415 - rand5 - 130))
            treedown_surface5 = pygame.transform.flip(treedown_surface5, False, True)
            treedown_surface6 = pygame.transform.scale(treeup_img, (90, 415 - rand6 - 130))
            treedown_surface6 = pygame.transform.flip(treedown_surface6, False, True)
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        userInput = pygame.key.get_pressed()
        if userInput[pygame.K_UP] and jump == False: # if the arrow up is pressed
            pygame.mixer.Sound.play(wingssound)
            b.jump() # jump
            jump = True # a boolean variable to not jump continuously
        if userInput[pygame.K_UP] == False: # if the arrow up is not longer pressed
            jump = False

        if userInput[pygame.K_ESCAPE]:# if the escape key is pressed
            pause()

        #the bird movement
        if b.vel > 5:
            b.vel = 5

        b.vel += 1
        b.y += b.vel

        #if a pipe is collided by the bird
        if b.y > LATIME - 85 or b.y < 0 or (b.y > 0 and b.y < rand1 and b.x > 210 + i and b.x < 210 + i + 90) or (
                b.y > rand1 + 130 and b.y < rand1 + 130 + 415 - rand1 - 130 and b.x > 210 + i and b.x < 210 + i + 90) or (
                b.y > 0 and b.y < rand2 and b.x > 510 + i and b.x < 510 + i + 90) or (
                b.y > rand2 + 130 and b.y < rand2 + 130 + 415 - rand2 - 130 and b.x > 510 + i and b.x < 510 + i + 90) or (
                b.y > 0 and b.y < rand3 and b.x > 810 + i and b.x < 810 + i + 90) or (
                b.y > rand3 + 130 and b.y < rand3 + 130 + 415 - rand3 - 130 and b.x > 810 + i and b.x < 810 + i + 90):
            pygame.mixer.Sound.play(explodesound)
            game_over()
            #reset the game
            score = 0
            b.y = 250
            i = 0
            WIN.blit(bg, (i, 0))
            WIN.blit(bg, (LUNGIME + i, 0))
            pygame.time.delay(200)

        #if the pipe is passed
        if (b.y > rand1 and b.y < rand1 + 130 and b.x == 210 + i + 45) or (
                b.y > rand2 and b.y < rand2 + 130 and b.x == 510 + i + 45) or (
                b.y > rand3 and b.y < rand3 + 130 and b.x == 810 + i + 45):
            score += 1

        pygame.time.delay(10)
        score_display()
        draw_window()
    pygame.quit()

def main_AI(genomes, config): #the AI game
    #variables
    nets=[]
    ge=[]
    birds=[]
    tree_index=0
    global rand1, rand2, rand3, rand4, rand5, rand6, jump, vel, treeup_surface1, treeup_surface2, treeup_surface3, treeup_surface4, treeup_surface5, treeup_surface6
    global treedown_surface1, treedown_surface2, treedown_surface3, treedown_surface4, treedown_surface5, treedown_surface6, birdlist, gens
    run = True
    i = 0
    for _, g in genomes:
        net=neat.nn.FeedForwardNetwork.create(g, config) #create the neural network
        nets.append(net)
        birds.append(Bird())
        g.fitness=0 #the bird score
        ge.append(g)

    while run:

        #draw the window
        WIN.blit(bg, (i, 0))
        WIN.blit(bg,(LUNGIME+i,0))

        if len(birds)>0: # if still exists birds
            # get which pipe is next
            tree_index = 0
            if birds[0].x > 210+i+90 and birds[0].x<510+i+90:
                tree_index=1
            if birds[0].x > 510 + i+90 and birds[0].x < 810 + i+90:
                tree_index=2


        else:
            gens += 1
            run=False
            break
        treesup=[rand1, rand2, rand3]
        treesdown=[rand1+130,rand2+130,rand3+130]
        for x,bird in enumerate(birds):
            ge[x].fitness+=0.1
            output=nets[x].activate((bird.y,abs(bird.y-treesup[tree_index]),abs(bird.y-abs(bird.y-treesdown[tree_index])))) # the function that activate the jump

            if output[0]>0.5 and jump==False : # if the output is greater than 0.5

                bird.jump()
                jump=True
            if bird.tick_count>=4:
                jump=False
            bird.tick_count+=1
        for b in birds: #draw the birds
            rectbird=pygame.Rect(int(b.x)-30,int(b.y)-30,60,60)
            WIN.blit(birdlist[b.birdindex],rectbird)
        for b in birds: # count the flapping of every bird's wings
            b.counter+=1
            if b.counter>5:
                b.counter=0
                b.birdindex+=1

            if b.birdindex>=2:
                b.birdindex=0

        #rects for pipes
        rect1=pygame.Rect(210+i,0,90,rand1)
        rect1down=pygame.Rect(210+i, rand1+130, 90, 415-rand1-130)

        rect2=pygame.Rect(510 + i, 0, 90, rand2)
        rect2down=pygame.Rect(510 + i, rand2+130, 90, 415-rand2-130)

        rect3=pygame.Rect(810 + i, 0, 90, rand3)
        rect3down=pygame.Rect(810 + i, rand3+130, 90, 415-rand3-130)

        rect4=pygame.Rect(210 + i + LUNGIME , 0, 90, rand4)
        rect4down=pygame.Rect(210 + i + LUNGIME, rand4+130, 90, 415-rand4-130)

        rect5=pygame.Rect(510 + i + LUNGIME, 0, 90, rand5)
        rect5down=pygame.Rect(510 + i + LUNGIME, rand5+130, 90, 415-rand5-130)

        rect6=pygame.Rect(810 + i + LUNGIME, 0, 90, rand6)
        rect6down=pygame.Rect(810 + i + LUNGIME, rand6+130, 90, 415-rand6-130)

        #draw the pipes

        WIN.blit(treeup_surface1,rect1)
        WIN.blit(treedown_surface1, rect1down)

        WIN.blit(treeup_surface2, rect2)
        WIN.blit(treedown_surface2, rect2down)

        WIN.blit(treeup_surface3, rect3)
        WIN.blit(treedown_surface3, rect3down)

        WIN.blit(treeup_surface4, rect4)
        WIN.blit(treedown_surface4, rect4down)

        WIN.blit(treeup_surface5, rect5)
        WIN.blit(treedown_surface5, rect5down)

        WIN.blit(treeup_surface6, rect6)
        WIN.blit(treedown_surface6, rect6down)


        i-=3



        if i==-LUNGIME: # if the first image is passed
            i=0
            #get the 2nd part of the pipes
            rand1, rand4=swap(rand1,rand4)
            rand2, rand5=swap(rand2,rand5)
            rand3, rand6=swap(rand3,rand6)
            #reinitialize the 2nd part of the pipes
            rand4 = random.randrange(65, 185)
            rand5 = random.randrange(65, 185)
            rand6 = random.randrange(65, 185)

            #calculate the new surfaces
            treeup_surface1 = pygame.transform.scale(treeup_img, (90, rand1))
            treeup_surface2 = pygame.transform.scale(treeup_img, (90, rand2))
            treeup_surface3 = pygame.transform.scale(treeup_img, (90, rand3))
            treeup_surface4 = pygame.transform.scale(treeup_img, (90, rand4))
            treeup_surface5 = pygame.transform.scale(treeup_img, (90, rand5))
            treeup_surface6 = pygame.transform.scale(treeup_img, (90, rand6))

            treedown_surface1 = pygame.transform.scale(treeup_img, (90, 415 - rand1 - 130))
            treedown_surface1 = pygame.transform.flip(treedown_surface1, False, True)
            treedown_surface2 = pygame.transform.scale(treeup_img, (90, 415 - rand2 - 130))
            treedown_surface2 = pygame.transform.flip(treedown_surface2, False, True)
            treedown_surface3 = pygame.transform.scale(treeup_img, (90, 415 - rand3 - 130))
            treedown_surface3 = pygame.transform.flip(treedown_surface3, False, True)
            treedown_surface4 = pygame.transform.scale(treeup_img, (90, 415 - rand4 - 130))
            treedown_surface4 = pygame.transform.flip(treedown_surface4, False, True)
            treedown_surface5 = pygame.transform.scale(treeup_img, (90, 415 - rand5 - 130))
            treedown_surface5 = pygame.transform.flip(treedown_surface5, False, True)
            treedown_surface6 = pygame.transform.scale(treeup_img, (90, 415 - rand6 - 130))
            treedown_surface6 = pygame.transform.flip(treedown_surface6, False, True)
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type==pygame.QUIT: #if the x is pressed
                run=False
                pygame.quit()
        userInput=pygame.key.get_pressed()

        if userInput[pygame.K_ESCAPE]: # if the escape key is pressed
            pause()

        # bird movement

        for b in birds:
            if b.vel>5:
                b.vel=5

            b.vel+=1
            b.y+=b.vel
        for x,b in enumerate(birds):
            #if the bird hits the pipe
            if b.y > LATIME - 85 or b.y < 0 or (b.y > 0 and b.y < rand1 and b.x > 210 + i and b.x < 210 + i + 90) or (
                    b.y > rand1 + 130 and b.y < rand1+130+415 - rand1 - 130 and b.x > 210 + i and b.x < 210 + i + 90) or (
                    b.y > 0 and b.y < rand2 and b.x > 510 + i and b.x < 510 + i + 90) or (
                    b.y > rand2 + 130 and b.y < rand2+130+415 - rand2 - 130 and b.x > 510 + i and b.x < 510 + i + 90) or (
                    b.y > 0 and b.y < rand3 and b.x > 810 + i and b.x < 810 + i + 90) or (
                    b.y > rand3 + 130 and b.y < rand3+130+415 - rand3 - 130 and b.x > 810 + i and b.x < 810 + i + 90):
                ge[x].fitness -= 1 # the score of the bird is decreasing
                #remove the bird
                birds.pop(x)
                nets.pop(x)
                ge.pop(x)

            if (b.y>rand1 and b.y<rand1+130 and b.x==210+i+90 ) or (b.y>rand2 and b.y<rand2+130 and b.x==510+i+90) or (b.y>rand3 and b.y<rand3+130 and b.x==810+i+90):#if the bird pass the pipe
                for g in ge:
                    g.fitness+=5 # the score is increasing with 5

        pygame.time.delay(10)
        AI_display(birds)
        draw_window()

def run(config_path): # the ML configs
    config=neat.config.Config(neat.DefaultGenome,neat.DefaultReproduction,neat.DefaultSpeciesSet,neat.DefaultStagnation,config_path) # get the config from the config path variable
    p=neat.Population(config) # get the population of birds
    p.add_reporter(neat.StdOutReporter(True)) # add the reporter to population
    stats=neat.StatisticsReporter() # get the stats for the algorithm
    p.add_reporter(stats) # include the stats to every bird
    main_menu(p)

if __name__=="__main__": # if this file is the main one
    local_dir=os.path.dirname(__file__)
    config_path=os.path.join(local_dir,"imgs/config-feedforward.txt") # get the config path
    run(config_path)