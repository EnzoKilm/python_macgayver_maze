##############################
#       Maze MacGayver       #
#     par Enzo Beauchamp     #
#      Version : 1.1.0       #
##############################
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
from random import randint

class Game:
    # Initialisation de la classe
    def __init__(self):
        # Transformation map texte en matrice
        with open('maps.txt', 'r') as grille:
            carte = grille.readlines()
            self.matrice_carte = []
            i = 0
            for ligne in carte:
                self.matrice_carte.append([])
                for case in ligne:
                    if case != "\n":
                        self.matrice_carte[i].append(case)
                i += 1
            # Ajout des objets sur la carte
            elements_a_placer = ['1', '2', '3']
            self.elements_a_rassembler = elements_a_placer.copy()
            while elements_a_placer != []:
                y_random = randint(0,len(self.matrice_carte)-1)
                x_random = randint(0,len(self.matrice_carte[0])-1)
                if self.matrice_carte[y_random][x_random] == '_':
                    self.matrice_carte[y_random][x_random] = elements_a_placer[0]
                    del elements_a_placer[0]
                    
        self.partie_gagnee = False
        self.partie_en_cours = True
        self.inventaire_joueur = []
        y = 0
        for ligne in carte:
            x = 0
            for case in ligne:
                if case == 'D':
                    self.pos_joueur = [y, x]
                x += 1
            y += 1

    # Affichage de la carte
    def affichage_map(self):
        print('───────────────')
        for ligne in self.matrice_carte:
            ligne_carte = ''
            for case in ligne:
                ligne_carte += case
            print(ligne_carte)

    # Gestion des déplacements
    def mouvement(self, y, x):
        self.matrice_carte[self.pos_joueur[0]][self.pos_joueur[1]] = '_'

        # Si il est bien dans la carte
        if self.pos_joueur[0]+y >= 0 and self.pos_joueur[1]+x >= 0 and self.pos_joueur[0]+y < len(self.matrice_carte) and self.pos_joueur[1]+x < len(self.matrice_carte[0]):
            # On vérifie que le joueur ne soit pas sur un mur
            if self.matrice_carte[self.pos_joueur[0]+y][self.pos_joueur[1]+x] != '#':
                # Si il est sur un objet
                if self.matrice_carte[self.pos_joueur[0]+y][self.pos_joueur[1]+x] in self.elements_a_rassembler:
                    self.inventaire_joueur.append(self.matrice_carte[self.pos_joueur[0]+y][self.pos_joueur[1]+x])
                    print(self.inventaire_joueur)
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

        self.matrice_carte[self.pos_joueur[0]][self.pos_joueur[1]] = 'D'
        
    # Lancement du jeu
    def lancement(self):
        while self.partie_en_cours == True:
            self.affichage_map()
            deplacement = ''
            # Tant que l'utilisateur ne saisit pas un déplacement correct
            while deplacement not in ['z', 'q', 's', 'd']:
                deplacement = input('Déplacement (z,q,s,d) : ')
                # On effectue le déplacement souhaité par le joueur
                if deplacement == 'z':
                    self.mouvement(-1, 0)
                elif deplacement == 'q':
                    self.mouvement(0, -1)
                elif deplacement == 's':
                    self.mouvement(1, 0)
                elif deplacement == 'd':
                    self.mouvement(0, 1)
        # On regarde si il a gagné ou non
        if self.partie_gagnee == True:
            print("Bravo, vous avez endormi le garde et réussi à vous échapper!")
        else:
            print("Vous n'avez pas réuni tous les éléments nécessaires pour endormir le garde, il vous a donc assommé!")
            
if __name__ == "__main__":
    partie = Game()
    partie.lancement()
