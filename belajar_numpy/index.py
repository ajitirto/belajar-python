import numpy as np

a=np.arange(10)**2

print(a)

#mengambil nilai
print("Element ke 1 dari a adalah", a[0])
print("Element ke 7 dari a adalah", a[6])
print("Element ke akhir dari a adalah", a[-1])

#slicing
print("Elemen dari 1-6 adalah", a[0:5])
print("elemen dari 5 sampai akhir", a[4:])
print("elemen dari 5 sampai deapn", a[:4])

#iterasi
for i in a:
    print("value = ", i)