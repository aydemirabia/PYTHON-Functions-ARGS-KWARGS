# 1- Kendisine gönderilen bir kelimeyi belirtilen kez ekranda gösteren fonksiyonu yazınız.
# 2- Dikdörtgenin alan ve cevresini hesaplayan fonksiyonu yazınız.
# 3- Yazı tura uygulamasını fonksiyon kullanarak yapınız. (Random Modülü)
# 4- Kendisine gönderilen 2 sayı arasındaki tüm asal sayıları bulunuz.
# 5- Kendisine gönderilen bir sayının tam bölenlerini liste şeklinde döndüren fonksiyonu yazınız.

# 1:
def yazdir(txt, adet):
    print(txt * adet);
yazdir('Python Functions\n', 5);

# 2:
def alancevre(a, b):
    alan = a * b;
    cevre = 4 * a * b;
    return f"Alan: {alan}\nCevre: {cevre}"
print(alancevre(5, 6));


# 3:
def yazitura():
    import random
    sayi = random.random();
    
    if sayi > 0.5:
        return "Yazi";
    else:
        return "Tura";
print(yazitura());

# 4:
def asalsayi(a, b):
    for sayi in range(a, b + 1):
        if(sayi > 1):
            for i in range(2, sayi):
                if(sayi % i == 0):
                    break;
            else:
                print("Asal Sayilar:\n"+sayi);
asalsayi(12, 95);

# 5:
def tambolenleribul(sayi):
    tambolenleribul = [];
    for i in range(2, sayi):
        if(sayi % i == 0):
            tambolenleribul.append(i);
    return tambolenleribul;

print(tambolenleribul(15));
print(tambolenleribul(23));
print(tambolenleribul(48));
print(tambolenleribul(71));