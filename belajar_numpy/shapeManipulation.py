import numpy as np

a= np.array((   [1,2,3],
                [4,5,6]
                ))
print("mtrix a dengan akurasi: ", a.shape)
print(a)




#flatten array, vector baris
print ("flatten matrxi a:")
print(a.ravel())
print(np.ravel(a))
print("matrix a dengan ukuran: ",a.shape)

#reshape matrix
print("reshape matrix a:")
print(a.reshape(6,1))
print("matrix a dengan ukuran: ",a.shape)

#resize matrix 
print ("resize matrix a: ")
a.resize(3,2)
print(a)
print("Matrix a dengan ukuran : ",a.shape)

#tranpose
print("tranpose matrid a adalah = ")
print(a.transpose())
print(np.transpose(a))
print(a.T)