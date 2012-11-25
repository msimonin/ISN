import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random
from collections import deque
"""
###### parametres de l'algorithmes #####
n        : nombres de lignes du labyrinthe voulu
p        : nombres de colonnes du labyrinthe voulu 
depart   : premier mur a casser (coordonnees x,y)
""" 
n = 10
p = 10 
murs_a_casser = 60 

labyrinthe = np.zeros((n,p),int)

fig = plt.figure()
"""
Debut de l'algorithme
"""
murs_deja_casses = 0
images = []
while(murs_deja_casses != murs_a_casser):
  x = random.randint(0,n-1)
  y = random.randint(0,p-1)
  if (labyrinthe[x,y] == 0):
    labyrinthe[x,y] = 1
    murs_deja_casses = murs_deja_casses + 1
    im = plt.imshow(np.copy(labyrinthe), interpolation='None', cmap='gist_gray')
    images.append([im])




###affichage
ani = animation.ArtistAnimation(fig, images, interval=1, blit=True,repeat_delay=1000)
np.savetxt("premierAlgorithme.txt",labyrinthe,fmt="%d")
ani.save('premierAlgorithme.mp4')
plt.show()
