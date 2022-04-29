def selamla(isim = "Sn. Aydemir", mesaj = "Iyi Calismalar"):
    print(f"{mesaj} {isim}");
    
selamla()

def toplam(a, b):
    return a + b;

def cikarma(a, b):
    return a - b;

def islem(a, b, fn):
    return fn(a, b);

def islme(a, b, fn = toplam): # 2. Yol
    return fn(a, b);

sonuc = islem(5, 3, toplam);
print(sonuc);

cevap = islme(8, 9);
print(cevap); 