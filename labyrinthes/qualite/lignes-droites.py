import numpy as np

mat = np.loadtxt("qualite3.txt")
n=11
p=21
max_horizontal = 0
courant = 0
for i in range(n):
   for j in range(p):
      if mat[i,j]==1:
        courant = courant + 1
      else:
        if courant>max_horizontal:
          max_horizontal = courant
        courant = 0 

max_vertical = 0 
courant = 0
for j in range(p):
   for i in range(n):
      if mat[i,j]==1:
        courant = courant + 1
      else:
        if courant>max_vertical:
          max_vertical = courant
        courant = 0 


print max_horizontal 
print max_vertical
