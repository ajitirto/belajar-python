import numpy as np
import matplotlib.pyplot as plt

def sinusGenerrator(amplitudo, frekuensi, tAkhir, theta):
    t =np.arange(0,tAkhir,0.1)
    y =amplitudo*np.sin(2*frekuensi*t +np.deg2rad(theta))
    return t,y
t,y =sinusGenerrator(1,1,4,0)

#MEmbuat plot 
plt.plot(t,y)


#setting axis, minimum sama maximum
plt.axis([0,4,-2,2])

#menampilkan 
plt.show()