# Öğrenci notları kayıt programı

# 'sinavNotlari.txt' dosyasının içindeki bilgileri parçalayarak öğrencinin notlarına ulaşılır ve ortalaması hesaplanır.
def notHesapla(satir):
    satir = satir[ : -1]
    liste = satir.split(":")

    ogrenciAdi = liste[0]
    notlar = liste[1].split(",")

    not1 = int(notlar[0])
    not2 = int(notlar[1])
    not3 = int(notlar[2])

    ortalama = (not1 + not2 + not3) / 3

    if (ortalama >= 90):
        harf = "AA"

    elif (ortalama >= 85 and ortalama <= 89):
        harf = "BA"

    elif (ortalama >= 80 and ortalama <= 84):
        harf = "BB"

    elif (ortalama >= 75 and ortalama <= 79):
        harf = "CB"

    elif (ortalama >= 70 and ortalama <= 74):
        harf = "CC"

    elif (ortalama >= 65 and ortalama <= 69):
        harf = "DC"

    elif (ortalama >= 60 and ortalama <= 64):
        harf = "DD"

    elif (ortalama >= 50 and ortalama <= 59):
        harf = "FD"

    elif (ortalama <= 49):
        harf = "FF"

    return f"{ogrenciAdi}: {harf}\n"

# 1'e basıldığında bu fonksiyon çalışır, 'sinavNotlari.txt' dosyasının içindeki bilgileri 'notHesapla()' fonksiyonuna yollar.
def ortalamalariOku():
    with open("sinavNotlari.txt", "r", encoding = "utf-8") as dosya:
        for satir in dosya:
            print(notHesapla(satir))

# 2'ye basıldığında bu fonksiyon çalışır, öğrencinin notlarını 'sinavNotlari.txt' dosyasına ekler.
def notGir():
    ad = input("Öğrenci ad: ")
    soyad = input("Öğrenci soyad: ")
    not1 = input("Not1: ")
    not2 = input("Not2: ")
    not3 = input("Not3: ")

    with open("sinavNotlari.txt", "a", encoding = "utf-8") as dosya:
        dosya.write(f"{ad} {soyad}: {not1}, {not2}, {not3}\n")

# 3'e basıldığında bu fonksiyon çalışır, 'notHesapla()' fonksiyonundan gelen değerler 'sonuclar.txt' dosyasına eklenir.
def notlariKaydet():
    with open("sinavNotlari.txt", "r", encoding = "utf-8") as dosya:
        liste = []

        for i in dosya:
            liste.append(notHesapla(i))

        with open("sonuclar.txt", "w", encoding = "utf-8") as dosya2:
            for i in liste:
                dosya2.write(i)

# Menünün oluşturulduğu bölüm
while True:
    islem = input("1.) Notları oku\n2.) Not gir\n3.) Notları kaydet\n4.) Çıkış\n")

    if islem   == "1":
        ortalamalariOku()

    elif islem == "2":
        notGir()

    elif islem == "3":
        notlariKaydet()

    elif islem == "4":
        break

    else:
        print("Yanlış değer girdiniz. Lütfen tekrar deneyiniz.")
