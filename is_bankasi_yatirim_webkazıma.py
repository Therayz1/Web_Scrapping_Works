import requests
from bs4 import BeautifulSoup
import time
import re

class Hisse:
    def __init__(self):
        self.dongu = True
        
        
    def program(self):
        secim = self.menu()
        
        if secim == "1":
            print("Güncel Fiyatlar Alınıyor...\n")
            time.sleep(3)
            self.guncelfiyat()
            
        if secim == "2":
            print("Künye Bilgileri Alınıyor...\n")
            time.sleep(3)
            self.kunye()
            
        if secim == "3":
            print("Cari Değerler Alınıyor...\n")
            time.sleep(3)
            self.carideger()
            
        if secim == "4":
            print("Getiri Bilgileri Alınıyor...\n")
            time.sleep(3)
            self.getiriler()
            
        if secim == "5":
            print("Endeks Ağırlık Oranları Alınıyor...\n")
            time.sleep(3)
            self.endeksagirligidahil()
        
        if secim == "6":
            print("Otomasyondan Çıkılıyor. Teşekkürler...\n")
            time.sleep(3)
            self.cikis()
    
    def menu(self):
        def kontrol(secim):
            if not re.search("[1-6]",secim):
                raise Exception("Lütfen 1 ve 6 arasında geçerli Bir seçim yapınız...")
            elif len(secim) != 1:
                raise Exception("Lütfen 1 ve 6 arasında geçerli Bir seçim yapınız...")
        while True:
            try:
                secim = input("Merhabalar EraylaData Otomasyon sistemine Hoşgeldiniz...\n\nLütfen yapmak istediğiniz işlemi seçiniz...\n\n[1]-Güncel Fiyat\n[2]-Şirket Künyesi\n[3]-Cari Değerler\n[4]-Getiri Rakamları\n[5]-Şirketin Dahil Olduğu Endeksler\n[6]-Çıkış\n\n")
                kontrol(secim)
            except Exception as Hata:
                print(Hata)
                time.sleep(3)
            else:
                break
        return secim
                
    def guncelfiyat(self):
        while True:
            try:
                sirket = input("Lütfen Şirket Adı Giriniz: ").upper()
                url = "https://www.isyatirim.com.tr/tr-tr/analiz/hisse/Sayfalar/default.aspx"
                
                parser = BeautifulSoup(requests.get(url).content,"html.parser")
                
                fiyat = parser.find("a",{"href":"/tr-tr/analiz/hisse/Sayfalar/sirket-karti.aspx?hisse={}".format(sirket.upper())}).parent.parent.find_all("td") # Bu kısımda parsera gelen html kodları arasında bir eleme yapacağız.
                bilgi1 = fiyat[1].string
                bilgi2 = fiyat[2].span.string
                bilgi3 = fiyat[3].string
                bilgi4 = fiyat[4].string
                bilgi5 = fiyat[5].string
                
                print(f"Son Fiyat:{bilgi1}\nDeğişim(%):{bilgi2.lstrip()}\rDeğişim(TL):{bilgi3}\nHacim(TL):{bilgi4}\nHacim(Adet):{bilgi5}")
                break
            except AttributeError:
                print("Hatalı Bir Şirket Adı Girdiniz")
                time.sleep(3)
        time.sleep(3)
        self.menudon()
                
    def kunye(self):
         while True:
            try:
                sirket = input("Lütfen Şirket Adı Giriniz: ").upper()
                url = "https://www.isyatirim.com.tr/tr-tr/analiz/hisse/Sayfalar/sirket-karti.aspx?hisse={}".format(sirket)
                
                parser = BeautifulSoup(requests.get(url).content,"html.parser")
                
                kunye = parser.find("div",{"id":"ctl00_ctl58_g_6618a196_7edb_4964_a018_a88cc6875488"}.find_all("tr"))
                for i in kunye:                    
                    bilgi1 = i.th.string
                    bilgi2 = i.td.string
                    print(f"{bilgi1}:{bilgi2}") 
                break
                
                
            except AttributeError:
                print("Hatalı Bir Şirket Adı Girdiniz")
                time.sleep(3)
        
        
    
    def carideger(self):
        while True:
            try:
                sirket = input("Lütfen Şirket Adı Giriniz: ").upper()
                url = "https://www.isyatirim.com.tr/tr-tr/analiz/hisse/Sayfalar/sirket-karti.aspx?hisse={}".format(sirket)
                
                parser = BeautifulSoup(requests.get(url).content,"html.parser")
                
                carideger = parser.find("div",{"id":"ctl00_ctl58_g_76ae4504_9743_4791_98df_dce2ca95cc0d"}.find_all("tr"))
                for i in carideger:                    
                    bilgi1 = i.th.string
                    bilgi2 = i.td.string
                    print(f"{bilgi1}:{bilgi2}\n") 
                break
                
                
            except AttributeError:
                print("Hatalı Bir Şirket Adı Girdiniz")
                time.sleep(3)
        time.sleep(3)
        self.menudon()
    
    def getiriler(self):
        while True:
            try:
                sirket = input("Lütfen Şirket Adı Giriniz: ").upper()
                url = "https://www.isyatirim.com.tr/tr-tr/analiz/hisse/Sayfalar/sirket-karti.aspx?hisse={}".format(sirket)
                
                parser = BeautifulSoup(requests.get(url).content,"html.parser")
                
                getiriler = parser.find("div",{"id":"ctl00_ctl58_g_aa8fd74f_f3b0_41b2_9767_ea6f3a837982"}.find("table").find("tbody").find_all("tr"))
                for i in getiriler:
                    bilgi = i.find_all("td")
                    print(f"Birim:{bilgi[0].string} Günlük(%):{bilgi[1].string} Haftalık(%):{bilgi[2].string} Aylık(%):{bilgi[3].string} Yıl İçi Getiri:{bilgi[4].string}")                    
                break
            except AttributeError:
                print("Hatalı Bir Şirket Adı Girdiniz")
                time.sleep(3)
        time.sleep(3)
        self.menudon()
    
    def endeksagirligidahil(self):
        while True:
            try:
                sirket = input("Lütfen Şirket Adı Giriniz: ").upper()
                url = "https://www.isyatirim.com.tr/tr-tr/analiz/hisse/Sayfalar/sirket-karti.aspx?hisse={}".format(sirket)
                
                parser = BeautifulSoup(requests.get(url).content,"html.parser")
                
                dahiliendeks = parser.find("div",{"id":"ctl00_ctl58_g_655a851d_3b9f_45b0_a2d4_b287d18715c9"}.find("table").find("tbody").find("tr").find_all("td"))
                dahiliendeks2 = parser.find("div",{"id":"ctl00_ctl58_g_655a851d_3b9f_45b0_a2d4_b287d18715c9"}.find("table").find("thead").find("tr").find_all("th"))
                for i in range(0,3):
                    print(f"{dahiliendeks2[i].string}:{dahiliendeks[i].string}")
                break
            except AttributeError:
                print("Hatalı Bir Şirket Adı Girdiniz")
                time.sleep(3)
        time.sleep(3)
        self.menudon()
    
    def cikis(self):
        self.dongu = False
        exit()
    
    def menudon(self):
        while True:
            x = input("Ana menüye dönmek için 7'ye , çıkmak için Lütfen 6'ya Baısnız...")
            if x == "7":
                print("Ana menüye Dönülüyor")
                time.sleep(3)
                self.program()
                break
            elif x == "6":
                self.cikis()
                break
            else:
                print("Lütfen Geçerli Bir seçim Yapınız")
                
sistem = Hisse()
while sistem.dongu:
    sistem.program()
