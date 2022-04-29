def toplam(*args):
    sonuc = 0;
    for i in args:
        sonuc += i;
    return sonuc;

print(toplam(10, 20, 30));
print(toplam(10, 20, 30, 40));


#değişken türünde parametre olduğu için * ekledik.

    # *args:  alacağımız parametre sayısını bilmiyorsak veya parametre sayısı 
    # değişkenlik gösteriyorsa kullanılır. 
    # Böylelikle fonksiyonumuza dinamiklik kazandırmış oluyoruz.
    
