# Numpy verileri çok daha az yer kaplar ve daha hızlıdır.
# Kompleks işlemlerde öne çıkar.


import numpy as np

# python list
list_py=[0,2,4,6,8,10,12,14,16]                         # List oluşturma

# numpy list
np_array=np.array([0,2,4,6])                           # Tek boyutlu Numpy dizisi oluşturma

#print(type(list_py))                                  # Değişken Tipi -> list
#print(type(np_array))                                 # Değişken Tipi -> numpy.ndarray


py_multi=[[0,2,4],[6,8,10],[12,14,16]]                 # Çok boyutlu dizi oluşturma

                                                       # reshape() metodu ile numpy dizisi şekillendirilir.
np_multi=np_array.reshape(2,2)                         # reshape(2,2) 2x2 tipinde matris oluşturur
#print(np_multi) 


np_arr=np.arange(1,10)                                 # arange(1,10) 1'den 9'a kadar yazdırır
np_arr2=np.arange(10,100,3)                            # arange(10,100,3) 10'dan 97'e kadar 3'er 3'er artar
np_arr3=np.zeros(10)                                   # zeros(10) 10 tane 0 yazdırır
np_arr4=np.ones(10)                                    # ones(10) 10 tane 1 yazdırır
np_arr5=np.linspace(0,100,5)                           # 0 ile 100 arasını 5 eşit parçaya böler. [0 25 50 75 100]

print(np_arr5)








