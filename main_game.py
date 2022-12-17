"""programme de DAMODARANE JEAN-BAPTISTE
projet : JEU de LABYRINTHE
commencé (officiellement) le 1 juin 2021
"""

import pygame      #module pygame
import time

####################################################
print(" _________________________________________________")
print("|BIENVENU à THE AMAZING MAZE GAME                   |")
print("|________________________________________________|")
time.sleep(1)
print("*****************************************")
print("* Ce jeu a certains règles à respecter: *")
print("*DEPLACEMENTS DU PERSONNAGES :          *")
print("*haut     : flèche du haut              *")
print("*bas      : flèche du bas               *")
print("*droite   : flèche de droite            *")
print("*gauche   : flèche de gauche            *")
print("*****************************************")

time.sleep(1)
print("ALORS COMMENCONS")

#permet d'initialiser pygame
pygame.init()


#permet de créer la fenêtre de jeu

screen = pygame.display.set_mode((1106, 600))    #cette fenêtre est temporaire et nous fait quitter automatiquement


#permet de mettre un icon pour la fenêtre

mon_icone = pygame.image.load('assets/mazeicon.png') #permet de faire venir (load) l'image
pygame.display.set_icon(mon_icone)                   #permet d'appliquer l'image qu'on a fait venir

#donne un nom à la fenêtre

pygame.display.set_caption("THE AMAZING MAZE GAME      (made in INDIA)")


#création de l'image de l'arrière plan
background = pygame.image.load('assets/ph.png')


#création du joueur

mon_joueur = pygame.image.load('assets/car.png')
#position de l'icone par rapports aux axes x et y
joueurX = 100			#axe x
joueurY = 100			#axe y
mouvement1x = 0
mouvement2y = 0


#définition de la fonction permettant de "dessiner" (=blit) l'image du joueur et de le place selon les axes

def joueur_icone(x,y):
	screen.blit(mon_joueur,(x,y))




#création du drapeau d'arrivé
reached = pygame.image.load('assets/flags.png')


#prosition du drapeau
flagX = 980
flagy = 500



#définition de la fonction permettant de dessiner le drapeau du point d'arrivé du joueur
def flag_image(x, y):
	screen.blit(reached,(x,y))


#définiitons des murs
wall = pygame.image.load('assets/minus.png')
def minus(x,y):
	 screen.blit(wall,(x,y))
wall2 = pygame.image.load('assets/minus2.png')
def minus2(x,y):
	 screen.blit(wall2,(x,y))
wall3 = pygame.image.load('assets/minus2.png')
def minus3(x,y):
	 screen.blit(wall3,(x,y))
wall4 = pygame.image.load('assets/minus2.png')
def minus4(x,y):
	 screen.blit(wall4,(x,y))
wall5 = pygame.image.load('assets/minus2.png')
def minus5(x,y):
	 screen.blit(wall5,(x,y))
wall6 = pygame.image.load('assets/minus2.png')
def minus6(x,y):
	 screen.blit(wall6,(x,y))
wall7 = pygame.image.load('assets/minus2.png')
def minus7(x,y):
	 screen.blit(wall7,(x,y))
wall8 = pygame.image.load('assets/minus2.png')
def minus8(x,y):
	 screen.blit(wall8,(x,y))

#définitions des obstacles

#création du drapeau d'arrivé
ufo1 = pygame.image.load('assets/ufo.png')
obs1x = 0
obs1y = 0
def obs1(x,y):
	screen.blit(ufo1,(x,y))
obs2x = 989
obs2y = 15
def obs2(x,y):
	screen.blit(ufo1,(x,y))




#########BOUCLE_INFINIE#############

maintain_screen = True
while (maintain_screen):						   # boucle while qui boucle àl'infini

	screen.blit(background,(0,0))                  #permet de dessiner l'image de l'arrière plan
	for event in pygame.event.get():
		#print(event)
		if event.type == pygame.QUIT:   #permet de quitter
			print("vous avez quitte")
			time.sleep(1)
			print("Revenez vite pour rejouer !!!!")
			maintain_screen = False

	if event.type == pygame.KEYDOWN:                 #quand on reste appuyer sur le les bouttons : KEYDOWN
		if event.key == pygame.K_LEFT:
			mouvement1x = -0.8
		if event.key == pygame.K_RIGHT:
			mouvement1x = +0.8
		if event.key == pygame.K_UP:
			mouvement2y = -0.8
		if event.key == pygame.K_DOWN:
			mouvement2y = +0.8
	if event.type == pygame.KEYUP:                  #quand on lache les bouttons : KEYUP
		if(event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT) or (event.key == pygame.K_UP or event.key == pygame.K_DOWN):
			mouvement1x = 0
			mouvement2y = 0





	##programme principale de la fonction joueur_icone
	joueurX += mouvement1x
	joueurY += mouvement2y
	joueur_icone(joueurX, joueurY)                    #appel de la fonction jouer_icone

	##programme principale de la fonction flag_image
	flag_image(flagX, flagy)						  #appel de la fonction flag_image80

	#programme principal des fonctions minus
	minus(830,15)
	minus2(100,100)
	minus3(250,15)
	minus4(380,100)
	minus5(500,15)
	minus6(650,100)
	minus7(-50,15)
	minus8(-190,100)

	#programme principale des fonctions obstacles
	obs1(obs1x,obs1y)
	obs2(obs2x,obs2y)






	pygame.display.update()#permet de mettre à jour cette couleur jusqu'à l'infini
