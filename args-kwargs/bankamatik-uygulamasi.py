# Bankamatik Uygulaması

rabiaHesap = {
    'ad' : "Rabia Aydemir",
    'hesapNo' : "123456789",
    'bakiye' : 5000,
    'ekHesap' : 5500
}

aliHesap = {
    'ad' : 'Ali Sancaktutan',
    'hesapNo' : "987654321",
    'bakiye' : 6000,
    'ekHesap' : 4500
}

def paracek(hesap, miktar):
    print(f"Merhaba Sn {hesap['ad']}");
    
    if hesap['bakiye'] >=miktar:
        hesap['bakiye'] -= miktar;
        print("Paranizi alabilirsiniz.");
    else:
        toplam =hesap['bakiye'] + hesap['ekHesap'];
        if(toplam >= miktar):
            ekhesapkullanimi =  input("Ek hesap kullanılsın mı? (E / H): ");
            if ekhesapkullanimi == 'e' or ekhesapkullanimi == 'E':
                print("Paranizi alabilirsiniz.");
            else:
                print(f"{hesap['hesapNo']} nolu hesabınızda {hesap['bakiye']} TL bulunmaktadır.");
        else:
            print("Bakiye Yetersiz");
def bakiyesorgula(hesap):
    print(f"{hesap['hesapNo']} nolu hesabinizda {hesap['bakiye']} TL bulunmaktadir. Ek hesap limitiniz ise {hesap['ekHesap']} TL bulunmaktadir.");

paracek(aliHesap, 8000);
bakiyesorgula(aliHesap);
print("*********************************");
paracek(rabiaHesap, 15000);
bakiyesorgula(rabiaHesap);

