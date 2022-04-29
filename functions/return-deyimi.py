from datetime import date
import re


def toplam():
    return f'toplam: {10+20}';

print(toplam());

# yaş hesapla
def simdi():
    import datetime
    return datetime.datetime.now().year;

def yashesapla():
    return simdi() - 1998;

print(yashesapla());

# saat dilimine göre selamlaşma
def vakit():
    import datetime
    return datetime.datetime.now().hour;

print(vakit());

def selamla():
    if(vakit() < 12):
        return "Gunaydin!";
    elif(vakit() > 12 & vakit() <= 18):
        return "Iyi Gunler!";
    else:
        return "Iyı Aksamlar!";
print(selamla());