__author__ = "All rights reserved by < ONUR ÖZTÜRK >\n"
print(__author__)
print("Adam Asmaca Oyununa Hoşgeldiniz.\n Kelimeler içerisinde sizin tahmin etmenizi istenilen bitki türleridir.\n Her bir kelime grubu için size 5 can hakkı tanınmaktadır. Başarılar...\n")
isim = input("Lütfen isminizi giriniz. : ")
print (isim, "<< İyi oyunlar... >>\n")

import random

kelimelist = random.choice(["kekik", "kiraz", "marul", "dereotu", "kabak", "nohut",                               "patlıcan", "kızılcık", "bergamot", "hanımeli"])

kelimeuzunluk = len(kelimelist)
print("Bu el {} harfli kelime geldi :)).\n".format(kelimeuzunluk))
oyuncucan = 5
bitkiler = []
tahminler = []
Cizgi = "|_|"
for kelime in kelimelist:
    bitkiler.append(Cizgi)
print(bitkiler)
while oyuncucan > 0:
    i = 0
    harfgiriş = input("\nBir harf giriniz...: ").lower()
    if harfgiriş in kelimelist:
        for kontrol in kelimelist:
            if kelimelist[i] == harfgiriş:
                bitkiler[i] = harfgiriş
            i += 1
        print("")
        print(bitkiler)
        print("\n\t Tahmin DOĞRU! ")
    else:
        oyuncucan -= 1
        print("")
        print(bitkiler)
        print("\n\t Yanlış Cevaap!")
        print("\n\t Kalan can = %s" %oyuncucan)
    if oyuncucan == 0:
        print("\nGAME OVER! Cevap: %s olacaktı.." %kelimelist)
        break
    if Cizgi not in bitkiler:
        print("\nTebrik ederiz.\t Oyunu Başarıyla Tamamladınız!")
        break