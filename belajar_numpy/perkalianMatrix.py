import numpy as np

a= np.array(([1,2],[3,4]))
b= np.ones([2,2])

print ("matrix a:")
print(a)
print("Matrix b:")
print (b)

#perkalian matrix
print("Perkalin matrix a,b")
c = a.dot(b)
print(c)