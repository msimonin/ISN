import numpy as np

def nb_cases_libres_voisines(mat,n,p,x,y):
   compteur = 0 
   if (x>0):
     compteur = compteur + mat[x-1,y] 
   if (x<n-1):
     compteur = compteur + mat[x+1,y] 
   if (y>0):
     compteur = compteur + mat[x,y-1] 
   if (y<p-1):
     compteur = compteur + mat[x,y+1]
   return compteur

mat = np.loadtxt("qualite1.txt")
n=9
p=9
impasses = 0
for i in range(n):
  for j in range(p):
    if (nb_cases_libres_voisines(mat,n,p,i,j)==1 and mat[i,j]) :
      impasses = impasses + 1

print impasses
