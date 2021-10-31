def bubleSort(val):
    
    for passnum in range(len(val)-1,0,-1):
        for i in range(passnum):
            if val[i]>val[i+1]:
                temp = val[i]
                val[i] = val[i+1]
                val[i+1] = temp
'''Bubble sort mungkin metode sorting a paling populer yang digunakan dan sederhana. Proses pengurutan dilakukan dengan membandingkan masing-masing nilai dalam suatu list secara berpasangan, kemudian tukar nilai jika diperlukan, dan mengulanginya sampai akhir list secara berurutan, sehingga tidak ada lagi nilai yang dapat ditukar.'''
def selectionSort(val):
    for isi in range(len(val)-1,0,-1):
        max=0
        for lokasi in range(1,isi+1):
            if val[lokasi]>val[max]:
                max = lokasi
        temp = val[isi]
        val[isi] = val[max]
        val[max]= temp
'''Prinsip dari algoritma selection sort adalah memilih elemen dengan nilai paling rendah dan menukar elemen tersebut dengan elemen ke-i. Nilai dari i dimulai dari 1 ke n, dimana n adalah jumlah total elemen dikurangi 1.'''


def insertSort(val):
    for index in range(1,len(val)):
        valueaktif = val[index]
        posisi = index
        while posisi>0 and val[posisi-1]>valueaktif:
            val[posisi]=val[posisi-1]
            posisi=posisi-1
        val[posisi]=valueaktif

'''Prinsip algoritma insertion sort pada dasarnya membagi data yang akan diurutkan menjadi dua bagian, satu bagian yang belum diurutkan dan yang satunya lagi sudah diurutkan. Elemen pertama diambil dari bagian list yang belum diurutkan dan kemudian diletakkan sesuai posisinya pada bagian lain dari list yang telah diurutkan. Langkah ini dilakukan secara berulang hingga tidak ada lagi elemen yang tersisa pada bagian list yang belum diurutkan.'''
angka=[6,4,7,2,1,23,43,54]
# bubleSort(angka)
#selectionSort(angka)
print("belum di urutkan",angka)
insertSort(angka)
print("sudah diurutkan",angka)
