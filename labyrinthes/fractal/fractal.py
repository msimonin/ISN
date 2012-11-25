import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
base = np.loadtxt("base7x7_1.txt")
#
#
#Votre algorithme ici
#
#  
im = plt.imshow(base, interpolation='None', cmap='gist_gray')
plt.show()
