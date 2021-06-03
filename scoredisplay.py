from variables import *
def score_display(score): #On SP part of game , the function prints the score(how many pipes we passed)

    score_font = pygame.font.Font("imgs/04B_19.TTF", 20)
    score_surface = score_font.render("Score: " + str(score), False, (0, 0, 0))
    score_rect = score_surface.get_rect(center=(LUNGIME / 4 * 5.5 / 3, 50))
    WIN.blit(score_surface, score_rect)