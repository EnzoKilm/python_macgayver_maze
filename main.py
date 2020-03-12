#############################
#       Maze MacGyver       #
#     par Enzo Beauchamp    #
#      Version : 1.2.0      #
#############################
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
from pygame.locals import *
from random import randint

class Game:
    # Initialisation de la classe
    def __init__(self):
        # Transformation map texte en matrice
        with open('maps.txt', 'r') as fichier:
            carte = fichier.readlines()
            self.matrice_carte = []
            i = 0
            for ligne in carte:
                self.matrice_carte.append([])
                for case in ligne:
                    if case != "\n":
                        self.matrice_carte[i].append(case)
                i += 1
                
            # Initialisation de pygame
            pygame.init()
            self.ecran = pygame.display.set_mode((len(self.matrice_carte)*40, len(self.matrice_carte[0])*40))
            pygame.display.set_caption('Mac Gyver Maze')
            self.mur = pygame.image.load('images/mur.png').convert()
            self.sol = pygame.image.load('images/sol.png').convert()
            self.perso = pygame.image.load('images/macgyver.png').convert_alpha()
            self.gardien = pygame.image.load('images/gardien.png').convert_alpha()
            self.objet1 = pygame.image.load('images/aiguille.png').convert_alpha()
            self.objet2 = pygame.image.load('images/tube.png').convert_alpha()
            self.objet3 = pygame.image.load('images/ether.png').convert_alpha()
            
            # Ajout des objets sur la carte
            elements_a_placer = ['1', '2', '3']
            sprites_objets = [self.objet1, self.objet2, self.objet3]
            self.elements_a_rassembler = elements_a_placer.copy()
            while elements_a_placer != []:
                y_random = randint(0,len(self.matrice_carte)-1)
                x_random = randint(0,len(self.matrice_carte[y_random])-1)
                if self.matrice_carte[y_random][x_random] == '_':
                    self.matrice_carte[y_random][x_random] = elements_a_placer[0]
                    del elements_a_placer[0]
                    
        self.partie_gagnee = False
        self.partie_en_cours = True
        self.inventaire_joueur = []
        for y in range(0, len(self.matrice_carte)):
            for x in range(0, len(self.matrice_carte[y])):
                case = self.matrice_carte[y][x]
                if case == '#':
                    self.ecran.blit(self.mur, (y*40, x*40))
                else:
                    self.ecran.blit(self.sol, (y*40, x*40))
                    if case == 'D':
                        self.pos_joueur = [y, x]
                        self.ecran.blit(self.perso, (y*40, x*40))
                    elif case == 'A':
                        self.ecran.blit(self.gardien, (y*40, x*40))
                    elif case in self.elements_a_rassembler:
                        self.ecran.blit(sprites_objets[self.elements_a_rassembler.index(case)], (y*40, x*40))

    # Gestion des déplacements
    def mouvement(self, x, y):
        self.matrice_carte[self.pos_joueur[0]][self.pos_joueur[1]] = '_'
        self.ecran.blit(self.sol, (self.pos_joueur[0]*40, self.pos_joueur[1]*40))

        # Si il est bien dans la carte
        if self.pos_joueur[0]+y >= 0 and self.pos_joueur[1]+x >= 0 and self.pos_joueur[0]+y < len(self.matrice_carte) and self.pos_joueur[1]+x < len(self.matrice_carte[0]):
            # On vérifie que le joueur ne soit pas sur un mur
            if self.matrice_carte[self.pos_joueur[0]+y][self.pos_joueur[1]+x] != '#':
                # Si il est sur un objet
                if self.matrice_carte[self.pos_joueur[0]+y][self.pos_joueur[1]+x] in self.elements_a_rassembler:
                    self.inventaire_joueur.append(self.matrice_carte[self.pos_joueur[0]+y][self.pos_joueur[1]+x])
                    ######AFFICHER QU'IL A L'OBJET
                # Ou si il est sur la case d'arrivée
                elif self.matrice_carte[self.pos_joueur[0]+y][self.pos_joueur[1]+x] == 'A':
                    self.partie_en_cours = False
                    if len(self.inventaire_joueur) == len(self.elements_a_rassembler):
                        self.partie_gagnee = True
                    else:
                        self.partie_gagnee = False
                # On le déplace
                self.pos_joueur[0] += y
                self.pos_joueur[1] += x
                
        self.ecran.blit(self.perso, (self.pos_joueur[0]*40, self.pos_joueur[1]*40))
        
    # Lancement du jeu
    def lancement(self):
        while self.partie_en_cours == True:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key in [pygame.K_w, pygame.K_UP]:
                        self.mouvement(-1, 0)
                    elif event.key in [pygame.K_a, pygame.K_LEFT]:
                        self.mouvement(0, -1)
                    elif event.key in [pygame.K_s, pygame.K_DOWN]:
                        self.mouvement(1, 0)
                    elif event.key in [pygame.K_d, pygame.K_RIGHT]:
                        self.mouvement(0, 1)
                    elif event.key == pygame.K_ESCAPE:
                        self.partie_en_cours = False
            pygame.display.flip()
        # On regarde si il a gagné ou non
        if self.partie_gagnee == True:
            print("Bravo, vous avez endormi le garde et réussi à vous échapper!")
        else:
            print("Vous n'avez pas réuni tous les éléments nécessaires pour endormir le garde, il vous a donc assommé!")
        pygame.quit()
        
if __name__ == "__main__":
    partie = Game().lancement()
