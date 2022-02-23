__author__ = "All rights reserved by < ONUR ÖZTÜRK >"
print(__author__)
print ("\tGenel kültür sınavına hoş geldiniz... Sınav 5 sorudan ve 3 şıktan oluşmaktadır. Sorulara cevap vererek bir sonraki soruya geçebilirsiniz... Başarılar :)")
# Öğrenci Bilgiler

İsim = input("İsminizi giriniz... : ")
Soyisim = input("Soy isminizi giriniz... : ")
OgrenciNo = input("Numaranızı giriniz... : ")
print()
print("Öğrencinin adı : {}\nÖğrencinin Soyadı : {}\nÖğrencinin Numarası : {}".format(İsim, Soyisim, OgrenciNo))
print()
print ("SINAV BAŞLIYOR...")
print()
# TEST SINAVI SORULAR
sQ = [ 'Fatih Sultan Mehmet’in babası kimdir?',
            'Magna Carta hangi ülkenin kralıyla yapılmış bir sözleşmedir?',
            'Hangisi periyodik tabloda bulunan bir element değildir?',
            'Hangisi bir doğal sayıdır?',
            'Galatasaray hangi yıl UEFA kupasını almıştır?' ]
# ŞIKLAR
A_şıkkı = ['Yıldırım Beyazıt', 'Fransa', 'Oksijen', '0', '2000']
B_şıkkı = ['II. Murat', 'İspanya', 'Su', '2,5', '2001']
C_şıkkı = ['I. Mehmet', 'İngiltere', 'Azot', '-4', '2002']
# DOĞRU CEVAP LİSTESİ
cevaplar = ['B', 'C', 'B', 'A', 'A']
# PUANLAMA
spuan = 0
# For döngüsü
for x in range(len(sQ)):
    print(f'SORU{str(x+1)}' + "\t:\t" + sQ[x])
    print(f'A) {A_şıkkı[x]}')
    print(f'B) {B_şıkkı[x]}')
    print(f'C) {C_şıkkı[x]}')
    cevap = input("Yanıtınızı giriniz : ")
    if cevaplar[x] == cevap.upper():
        print()
        print("-"*20)
        print("Cevabınız DOĞRU...!")
        print("-"*20)
        print()
        spuan +=1
    else:
        print()
        print("-"*20)
        print("Cevabınız YANLIŞ...!")
        print("-"*20)
        print()
# SINAV SONUÇ EKRANI
print("\t\tSınav sona ermiştir... Aldığınız PUAN : ", int((spuan/len(sQ))*100))
print()
input ("\t\tÇıkmak için herhangi bir tuşa basınız...\t")