__author__ = "All rights reserved by < ONUR ÖZTÜRK >"
print(__author__)

print ("Genel küjltür sınavına hoş geldiniz... Sınav 5 sorudan oluşmaktadır. Sorulara E veya H ile cevap vererek bir sonraki soruya geçebilirsiniz... Başarılar :)")

# SORULAR

soru1 = "Günümüzde nüfusu en fazla olan İslam ülkesi Endonezyadır. [E/H]: "
soru2 = "İlk defa dünya haritasını Piri Reis çizmiştir. [E/H]: "
soru3 = "Avustralya adasının en tanınmış hayvanı penguendir. [E/H]: "
soru4 = "Futbol toplam 11 ile oynanır. [E/H]: "
soru5 = "Bursa ilimizin araba ve şehir kod numarası 14 kodudur. [E/H]: "

"""
# CEVAPLAR
cevap1 = "Endonezya"
cevap2 = "Piri Reis"
cevap3 = "Kanguru"
cevap4 = "22 Kişi"
cevap5 = "06"
"""

# [E/H] TUŞLAMASI

EVET = "E"
KEVET = EVET.lower()
HAYIR = "H"
KHAYIR = HAYIR.lower()

# PUANLAMA
puan = 0

İsim = input("İsminizi giriniz... : ")
Soyisim = input("Soy isminizi giriniz... : ")
OgrenciNo = input("Numaranızı giriniz... : ")
print("Öğfencinin adı : {}\nÖğrencinin Soyadı : {}\nÖğrencinin Numarası : {}".format(İsim, Soyisim, OgrenciNo))
print ("SINAV BAŞLIYOR...")
print()

Q1 = input (soru1) # 1.SORU CEVABI ENDONEZYA
if Q1 == EVET or Q1 == KEVET:
    print ("Cevabınız DOĞRU...!")
    print()
    puan += 1
else:
    print("Cevabınız YANLIŞ...!")
    print()

Q2 = input(soru2) # 2.SORU CEVABI PİRİ REİS
if Q2 == EVET or Q2 == KEVET:
    print("Cevabınız DOĞRU...!")
    print()
    puan += 1
else:
    print("Cevabınız YANLIŞ...!")
    print()

Q3 = input(soru3) # 3.SORU CEVABI KANGURU
if Q3 == HAYIR or Q3 == KHAYIR:
    print("Cevabınız DOĞRU...!")
    print()
    puan += 1
else:
    print("Cevabınız YANLIŞ...!")
    print()

Q4 = input(soru4) # 4.SORU CEVABI 22
if Q4 == HAYIR or Q4 == KHAYIR:
    print("Cevabınız DOĞRU...!")
    print()
    puan += 1
else:
    print("Cevabınız YANLIŞ...!")
    print()

Q5 = input(soru5) # 5.SORU CEVABI 16
if Q5 == HAYIR or Q5 == KHAYIR:
    print("Cevabınız DOĞRU...!")
    print()
    puan += 1
else:
    print("Cevabınız YANLIŞ...!")
    print()

print("     Sınav sona ermiştir... Aldığınız PUAN : ", str(puan*20))
input ("Çıkmak için herhangi bir tuşa basınız...")
