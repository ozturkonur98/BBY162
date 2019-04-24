__author__ = "ONUR ÖZTÜRK / DATE = 24.04.19/ 21661707"
print(__author__)

#1.	Aşağıdaki değişkene atanmış metnin içerisindeki ilk 20 karakteri ekrana yazdıracak python kodunu yazınız (2P).

print ("\n\t\t Soru 1 ")
metin = "Açık bilim, araştırma çıktılarına ve süreçlerine herkesin serbestçe erişmesi, bunların ortak kullanımı, dağıtımını ve üretimini kolaylaştıran bilim uygulamasıdır."

print(metin)
print("\t\tİlk yirmi karakteri ekrana geliyor...")
ilk20 = metin[:20]
print(ilk20)

print ("\n\t\t Soru 2 ")
#2. Aşağıdaki liste öğesinde yer alan elemanları alt alta ekrana yazdıracak python kodunu yazınız. Kodunuzu bir döngü yardımıyla oluşturunuz (3P).

liste = ["Açık Bilim", "Açık Erişim", "Açık Lisans", "Açık Eğitim", "Açık Veri", "Açık Kültür"]

print(liste)
for i in liste:
    print(i)


print ("\n\t\t Soru 3 ")

#3. Aşağıdaki sözlük öğesinde yer alan kelime alanında klavyeden girilen veri ile bir arama yaptırarak ilgili kelimeye karşılık gelen açıklamayı ve kelimenin kendisini ekrana yazdıracak python kodunu yazınız. Eğer klavyeden girilen kelime sözlükte yoksa uygun bir mesaj ile yeniden arama yapılabilmesi için gereken düzenlemeyi yapınız (5P).

sozluk = {"Elma" : "Ağaçta yetişen bir tür meyve" , "Salatalık" : "Fidan üzerinde büyüyen bir tür sebze" }
kgiris = input("Hangi sözcüğü aramak istiyorsunuz? Elma/Salatalık : ")

if kgiris == "Elma":
    kgiris = kgiris.swapcase()
    print(sozluk["Elma"])
elif kgiris == "Salatalık":
    kgiris == kgiris.swapcase()
    print(sozluk["Salatalık"])
else:
    print("Aradığınız kelime sözlükte bulunamamaktadır. Lütfen Tekrar arama yapınız.")