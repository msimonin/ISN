import numpy as np
import matplotlib.pyplot as plt
import random
"""
###### parametres de l'algorithmes #####
n        : nombres de lignes du labyrinthe voulu
p        : nombres de colonnes du labyrinthe voulu 
""" 
n = 10
p = 10 
murs_a_casser = 60 

labyrinthe = np.zeros((n,p),int)

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

fig = plt.figure()
im = plt.imshow(labyrinthe, interpolation='None', cmap='gist_gray')
np.savetxt("premierAlgorithme.txt",labyrinthe,fmt="%d")
plt.show()
