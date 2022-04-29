# arguments, parametres
def ad_soyad(isim, soyad):
    return isim+ " " + soyad;

sonuc = ad_soyad("Rabia", "Aydemir");
print(sonuc);


#--------------------------------------------------------------------------------------
#fonksiyonu tanımlarken kullandığımız değişkenler PARAMETRE'dir.
# def ad_soyad(isim, soyad): buradaki isim ve soyad değerleri PARAMETRE'dir.
#--------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------
#sonuc = ad_soyad("Rabia", "Aydemir"); burada ad_soyad fonksiyonuna vermiş olduğumuz 
#değerler ARGÜMAN' dır. Tanımladığımız fonksiyona değer vermek ARGÜMAN'dır.
#--------------------------------------------------------------------------------------
#Fonksiyon çağrılırken gönderilen değerlere Argüman denir.
#Fonksiyon bildiriminde, fonksiyona girdi olarak, kullanılan değişkenlere Parametre denir.