import numpy as np 

#membuat vektor
a=np.array([1,2,3,4,5])
b=np.array([1.5,2.5,3.5,4,5])
#membuat vektor dengan range
c= np.arange(1,10,2)

#mebuat linespace
d= np.linspace(1,10,4)
#membuat multidimensi.matrix
e=np.array([(1,2,3),(4,5,6)])

#matrix denan nilai nool

f=np.zeros([5,5])

#menampilkan 1 semua
g= np.ones([5,5])

#matrix indentitas
h = np.identity(5)
i= np.eye(5)
# menampilkan
# print(a)
# print(b)
# print(c)
# print(d)
# print(e+1)
# print(f)
# print(g)
print(h)
print(i)