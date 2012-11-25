import numpy as np
import matplotlib.pyplot as plt
"""
Nombre de cases du labyrinthe en ligne  et en colonne 
"""
n = 4 
p = 7
"""
Un labyrinthe est initialement rempli de murs
"""
labyrinthe = np.zeros((n,p),int)
"""
On casse un mur
"""
labyrinthe[2,1] = 1
for j in range(p):
"""
On affiche le resultat
"""
fig = plt.figure()
im = plt.imshow(labyrinthe, interpolation='None', cmap='gist_gray')
plt.show()
