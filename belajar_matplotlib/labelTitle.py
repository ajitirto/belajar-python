import matplotlib.pyplot as plt
import numpy as np

#membuatdata
def sinusGenerrator(amplitudo, frekuensi, tAkhir, theta):
    t =np.arange(0,tAkhir,0.1)
    y =amplitudo*np.sin(2*frekuensi*t +np.deg2rad(theta))
    return t,y
amplitudo=1
frekuensi= 1
theta=0
tAkhir = 4

t,y =sinusGenerrator(1,1,4,0)

t,y = sinusGenerrator(amplitudo, frekuensi,tAkhir, theta)

#membuat plot

judul = 'Grafik Sinusosidal\n'
rumus = r'$ \mathcal{Y}  = A.sin(2 \omega t + \theta) $' +'\n'
parameter1 = r'$ A = $' + str(amplitudo) + ' cm, '
parameter2= r'$\omega = $'+ str(frekuensi) + r'$\mathit{Hz}$ '+', '
parameter3 = r'$\theta = $'+ str(theta) +r'$^{o}$'

plt.plot(t,y)
plt.title(judul+rumus+parameter1+parameter2+parameter3)


plt.xlabel("waktu(detik)")
plt.ylabel("Magnitudo(cm)")


#menampilkan plot
plt.show()