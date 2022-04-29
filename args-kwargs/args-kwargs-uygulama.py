# 1) Kendisine gönderilen 2 sayıdan büyük olanı bulan fonksiyonu yazınız.
# 2) Kendisine gönderilen bir string bilgi içinde her karakter kaçar kez tekrarlanmış bulunuz.
# 3) Kendisine gönderilen list, command, position ve value bilgilerine göre liste üzerinde güncelleme yapınız.
#     --  [1, 2, 3], ("add, remove"), ("beginning | end", "4") => [1, 2, 3, 4]
#     -- list_operation([1, 2, 3], "remove", "end", "4") => [1, 2, 3, 4]
#     -- list_operation([1, 2, 3], "remove", "beginning", "4") => [2, 3]
# 4) Kendisine gönderilen renk isimlerinden içinde "blue" rengi varsa True döndüren fonksiyonu yazınız.


# 1:
import re
from tkinter.tix import Tree
from xmlrpc.client import FastParser


def buyukolanibul(a, b):
    if(a > b):
        print(f'{a} sayisi {b} sayisindan buyuktur.');
    elif(b > a):
        print(f'{b} sayisi {a} sayisindan buyuktur.');
    else:
        print(f'{a} sayisi ile {b} sayisi esittir.');

buyukolanibul(45, 56)

#*********************************************************************

# 2:
def karaktersayisibul(c):
    return {harf: c.count(harf) for harf in c}
print(karaktersayisibul("python"));

#*********************************************************************

# 3:
def liste_guncelle(liste, command, position, value = None):
    if command == "remove" and position == "end":
        return liste.pop();
    elif command == "remove" and position == "beginning":
        return liste.pop(0);
    elif command == "add" and position == "end":
        liste.append(value);
        return liste;
    elif command == "add" and position == "beginning":
        liste.insert(0, value);
        return liste;
sonuc = liste_guncelle([1, 2, 3], "add", "end", 4);
sonuc = liste_guncelle([1, 2, 3], "add", "beginning", 4);
sonuc = liste_guncelle([1, 2, 3], "remove", "beginning");
sonuc = liste_guncelle([1, 2, 3], "remove", "end");

print(sonuc);

#*********************************************************************

# 4:
def renkbul(*args):
    if "blue" in args:
        return True;
    return False;
print(renkbul("red","yellow","pink","black", "blue"));
