import pygame
import sys
class Grille:

    def __init__(self):
        self.ecran = ecran
        self.lignes = [(( 200,0),(200,600))
        ((400,0),(400,600))
        ((0,200),(600,200))
        ((0,400),(600,400)),]
    def afficher(self):
        for ligne in self.ligne_:
            pygame.draw.line(self.ecran,(0,0,0),ligne[0],ligne[1],2)


class Jeu :

    def __init__(self):
        self.ecran = pygame.display.set_mode((600,600))
        pygame.dipslay.set_caption('Tic Tac Toe')
        self.jeu_encours = True
        self.grille = Grille(self.ecran)

    def fonction_principale(self):
        while self.jeu_encours:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                # ajouter0

            self.ecran.fill((240,240,240))
            self.grille.afficher()
            pygame.display.flip()


if __name__ == ' main':
    pygame.init()
    Jeu().fonction_principale()
    pygame.quit()
