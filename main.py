##############################
#       Maze MacGayver       #
#     par Enzo Beauchamp     #
#      Version : 1.0.1       #
##############################
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
from random import randint

# Transformation map texte en matrice
with open('maps.txt', 'r') as grille:
    carte = grille.readlines()
    matrice_carte = []
    i = 0
    for ligne in carte:
        matrice_carte.append([])
        for case in ligne:
            if case != "\n":
                matrice_carte[i].append(case)
        i += 1
    # Ajout des objets sur la carte
    elements_a_placer = ['1', '2', '3']
    while elements_a_placer != []:
        y_random = randint(0,len(matrice_carte)-1)
        x_random = randint(0,len(matrice_carte[0])-1)
        if matrice_carte[y_random][x_random] == '_':
            matrice_carte[y_random][x_random] = elements_a_placer[0]
            del elements_a_placer[0]
        

# Affichage de la carte
def print_map():
    print('---------------')
    for ligne in matrice_carte:
        ligne_carte = ''
        for case in ligne:
            ligne_carte += case
        print(ligne_carte)

# Initialisation du jeu
def init():
    global pos_joueur
    y = 0
    for ligne in carte:
        x = 0
        for case in ligne:
            if case == 'D':
                pos_joueur = [y, x]
            x += 1
        y += 1

# Gestion des déplacements
def mouvement(y, x):
    matrice_carte[pos_joueur[0]][pos_joueur[1]] = '_'

    if matrice_carte[pos_joueur[0]+y][pos_joueur[1]+x] != '#':
        if pos_joueur[0]+y >= 0 and pos_joueur[1]+x >= 0:
            pos_joueur[0] += y
            pos_joueur[1] += x

    matrice_carte[pos_joueur[0]][pos_joueur[1]] = 'D'

        
# Lancement du jeu
def lancement():
    init()
    while True:
        print_map()
        deplacement = ''
        while deplacement not in ['z', 'q', 's', 'd']:
            deplacement = input('Déplacement (z,q,s,d) : ')
            if deplacement == 'z':
                mouvement(-1, 0)
            elif deplacement == 'q':
                mouvement(0, -1)
            elif deplacement == 's':
                mouvement(1, 0)
            elif deplacement == 'd':
                mouvement(0, 1)

if __name__ == "__main__":
    lancement()
