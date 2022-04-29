def selamla(isim):
    return "Merhaba " + isim;

print(selamla("Rabia Aydemir"));

def toplam(a, b):
    return a + b;

sonuc = toplam(40, 20);
print(sonuc);

# yas hesaplayan fonksiyon
def yashesapla(dogumyili):
    return 2022 - dogumyili;
sonuc2 = yashesapla(1956);
print(sonuc2);

# emekliliğe kalan yıl 
def emekliligekacyilkaldi(dogumyili, isim):
    yas = yashesapla(dogumyili);
    emeklilik = 65 - yas;
    return f"Sn. {isim} emekliliginize {emeklilik} kaldi.";

sonuc3 = emekliligekacyilkaldi(1998, "Aydemir");
print(sonuc3);
