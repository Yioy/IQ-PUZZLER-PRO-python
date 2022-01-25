
#Règle du jeu : https://www.smartgames.eu/uk/one-player-games/iq-puzzler-pro
#Auteur : Sébastien DOUTRELUINGNE, Yi Wen JIANG, Osée Brayan TCHAPPI



#bibliotèques


from Graphisme import InterfaceGraphique
import numpy as np

#création d'une grille vide
grid = np.zeros((5, 11), dtype=np.uint8)
InterfaceGraphique(grid)



