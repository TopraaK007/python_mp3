# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
from random import choice
class Mp3calar():
    def __init__(self,sarki_listesi=[]):
        self.suan_calansarki=""
        self.ses=100
        self.sarki_listesi=sarki_listesi
        self.durum=True

    def sarki_sec(self):
        sayac = 1
        for sarki in self.sarki_listesi:
            print("{}){} ".format(sayac, sarki))
            sayac += 1

        while True:
            try:
                secilen_sarki = int(input("Dinlemek istediğiniz şarkıyı seçiniz:"))
                if secilen_sarki >= 1 and secilen_sarki <= len(self.sarki_listesi):
                    self.suan_calansarki = self.sarki_listesi[secilen_sarki - 1]
                    break
                else:
                    print("1-{} arası sayı giriniz".format(len(self.sarki_listesi)))
            except ValueError:
                print("Lütfen sayı giriniz")
    def ses_arttir(self):
        if self.ses == 100:
            pass
        else:
            self.ses += 10
    def ses_azalt(self):
        if self.ses==0:
            pass
        else:
            self.ses-=10
    def rastgele_sarki(self):
        rndsarki=choice(self.sarki_listesi)
        self.suan_calansarki=rndsarki
    def sarki_ekle(self):
        sanatci=input("Sanatçı/Grup giriniz:")
        sarki=input("Şarkı Giriniz:")

        self.sarki_listesi.append(sanatci+" - "+sarki)


    def sarki_sil(self):
        sayac=1
        for sarki in self.sarki_listesi:
            print("{}){}".format(sayac,sarki))

        while True:
            try:
                silenecek_sarki=int(input("Silinecek şarkıyı seçiniz (1-{})").format(len(self.sarki_listesi)))
                if silenecek_sarki>=1 and silenecek_sarki<=len(self.sarki_listesi):
                    self.sarki_listesi.pop(silenecek_sarki-1)
                else:
                    print("Lütfen 1-{} arası sayı seçiniz".format(len(self.sarki_listesi)))
            except ValueError:
                print("Lütfen sayı giriniz")



    def kapat(self):
        self.durum=False
    def menu_goster(self):
        print( """
Şarkı Listesi : {}
Şuan Çalan Şarkı : {}
Ses Düzeyi : {}

1)Şarkı Seç
2)Ses Arttır
3)Ses Azalt
4)Rastgele Şarkı Seç
5)Şarkı Ekle
6)Şarkı Sil
7)Kapat """.format(self.sarki_listesi,self.suan_calansarki,self.ses))
    def secim(self):
        while True:
            try:
                sec=int(input("Seçiminizi Giriniz:"))
                if sec>=1 and sec<=7:
                    return sec
                else:
                    print("Lütfen 1-7 arası bir seçim yapın")
            except ValueError:
                print("Lütfen sayı giriniz")

    def calistir(self):
        self.menu_goster()
        sec=self.secim()
        if sec==1:
           self.sarki_sec()
        if sec==2:
           self.ses_arttir()
        if sec==3:
           self.ses_azalt()
        if sec==4:
           self.rastgele_sarki()
        if sec==5:
           self.sarki_ekle()
        if sec==6:
            self.sarki_sil()
        if sec==7:
            self.kapat()



mp3calar=Mp3calar()
while mp3calar.durum:
    mp3calar.calistir()
print("Program Sonlandı")