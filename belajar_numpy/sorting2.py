import numpy as np 

a=np.floor(np.random.randn(2,2) *10)

print(a)

print("nilai max dari a = ", a.max())
print("posisi max dari a = ", a.argmax())

print("nilai min dari a = ", a.min())
print("posisi min dari a = ", a.argmin())

print("mengurutkan nialai a = ")
print(np.sort(a))

print("mengurutkan posisis a = ")
print(np.argsort(a))
