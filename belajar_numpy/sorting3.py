import numpy as np

#dtipe = [('nama', '510'),('tinggi',int)]
dtipe = [('nama','S10'),('tinggi',int)]
# data =[
#     ('ucup',170),
#     ('otong',150),
#     ('mario',100)
# ]

data = [
	('Ucup',170),
	('Otong', 150),
	('Mario',160)
]

a=np.array(data, dtype = dtipe)
print(a)
print(np.sort(a, order='tinggi'))
print(np.sort(a, order='nama'))

# import numpy as np

# dtipe = [('nama','S10'),('tinggi',int)]
# data = [
# 	('Ucup',170),
# 	('Otong', 150),
# 	('Mario',160)
# ]

# a = np.array(data, dtype = dtipe)
# print(a)