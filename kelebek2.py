import matplotlib
import time
x=0.9999999
a=3.9999999
yn=x
sıfır=[]
bir=[]
hepsi=[]
start=time.time()
for i in range(1000000):
    xn=a*yn*float(1-yn)
    yn=xn
    if yn>0.4999724:
        hepsi.append(1)
        bir.append(1)
    else:
        hepsi.append(0)
        sıfır.append(0)
end=time.time()

# [['0000'],['0001'],['0010'],.....]
dortluk = [''.join(map(str,hepsi[i:i+4])) for i in range(0, len(hepsi), 4)]




# decimal to binary ['1111']=15
sayilar=[]
for i in dortluk:
    sayilar.append(int(i,2))







# 0-15 kadar listede toplam sayısı
degerler=[]
for i in range(0,16):
    degerler.append(sayilar.count(i))

#
bitler=['0000','0001','0010','0011','0100','0101','0110','0111','1000','1001','1010','1011','1100','1101','1110','1111']
bir=[]
sıfır=[]
for i in bitler:
    bir.append(i.count('1'))
    sıfır.append(i.count('0'))

bir_bit=[]
sıfır_bit=[]
for i in range(len(degerler)):
    bir_bit.append(bir[i]*degerler[i])
    sıfır_bit.append(sıfır[i]*degerler[i])








print("sıfır :",len(sıfır))
print("bir :",len(bir))
print("sayilar = ",len(sayilar))
print("degerler =", degerler)
print("bir_bit =",bir_bit)
print("sıfır_bit =",sıfır_bit)
bir_toplam=0
sıfır_toplam=0
for i in range(16):
    bir_toplam+=bir_bit[i]
    sıfır_toplam+=sıfır_bit[i]
print("1 : ",bir_toplam)
print("0 : ",sıfır_toplam)


