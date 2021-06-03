from variables import *
from draw import *
import sys
def game_over(score):
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