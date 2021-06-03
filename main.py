import neat
import os
from bird import *
from swap import *
from aidisplay import *
from scoredisplay import *
from gameover import *
pygame.init()



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
            game_over(score)
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
        score_display(score)
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
        AI_display(birds,gens)
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