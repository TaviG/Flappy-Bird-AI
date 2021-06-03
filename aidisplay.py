from variables import *
def AI_display(birds,gens): #On AI part of game, the function prints on which generation we are in this moment, and the birds alive.
    gens_font = pygame.font.Font("imgs/04B_19.TTF", 30)
    gens_surface = gens_font.render("Gen: " + str(gens), False, (0, 0, 0))
    birds_surface=gens_font.render("Alive:" + str(len(birds)), False, (0, 0, 0))
    gens_rect = gens_surface.get_rect(center=(60, 30))
    birds_rect=birds_surface.get_rect(center=(60,80))
    WIN.blit(gens_surface, gens_rect)
    WIN.blit(birds_surface, birds_rect)