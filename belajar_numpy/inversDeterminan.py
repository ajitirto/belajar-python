import numpy as np 
a=np.array([(1,-1),(1,1)])

#print (a)

#invers matrix 
a_invers = np.linalg.inv(a)

# print(a_invers)
# print(np.dot(a,a_invers))

#determinan matrix

det_a = np.linalg.det(a)
det_a_inv = np.linalg.det(a_invers)
print(det_a)
print(det_a_inv)

#