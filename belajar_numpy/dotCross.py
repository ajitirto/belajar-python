import numpy as np 
a = np.array([1,3])
b=np.array([2,1])

#pekalian dot
c= np.dot(a,b)
# print(c)

a2= np.array([1,2,0])
b2= np.array([2,1,0])

#perkalian cross
c2=np.cross(a2,b2)
# print(c2)
c3=np.cross(b2,a2)
print(c3)