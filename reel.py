import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
import subprocess

# ==== Banner Tasarımı ====
def banner():
    print("\033[34m")  # Mavi renk
    print("*" * 50)
    print("************     VİOSRİO İNSTA TOOL     ************")
    print("*" * 50)
    print("\033[0m")  # Renk sıfırlama

# ==== Modül Kontrol ve Yükleme ====
def check_and_install(package):
    try:
        __import__(package)
    except ImportError:
        print(f"\033[33mModül bulunamadı: {package}. Şimdi yükleniyor...\033[0m")
        os.system(f"pip install {package}")

# ==== Gerekli Modülleri Kontrol Et ====
modules = ['selenium', 'webdriver-manager']
for module in modules:
    check_and_install(module)

# ==== Kullanıcı Seçimi ====
def user_input():
    print("\033[31m")  # Kırmızı renk
    print("1. İNSTALOADER")
    print("2. WEB DRİVER")
    print("3. MOZİLLA FİREFOX")
    print("\033[0m")  # Renk sıfırlama
    choice = input("HANGİ KÜTÜPHANE SEÇİN? : ")
    return choice

# ==== Geckodriver Ayarları ====
def setup_driver():
    geckodriver_path = "./geckodriver"  # Aynı dizinde olmalı
    service = Service(geckodriver_path)
    driver = webdriver.Firefox(service=service)
    return driver

# ==== Instagram Girişi ====
def instagram_login(driver, username, password):
    driver.get("https://www.instagram.com")
    time.sleep(3)
    print("\033[35mInstagram giriş yapılıyor...\033[0m")  # Mor renk
    # Burada selenium ile giriş işlemleri yapılabilir.

# ==== Ana Program ====
if __name__ == "__main__":
    banner()
    choice = user_input()

    if choice == "1":
        print("İnstaloader Seçildi!")
        check_and_install("instaloader")
    elif choice == "2":
        print("Web Driver Seçildi!")
    elif choice == "3":
        print("Mozilla Firefox Seçildi!")
        driver = setup_driver()

        # Kullanıcı bilgilerini alalım
        username = input("Kullanıcı Adı: ")
        password = input("Şifre: ")

        # Instagram giriş yap
        instagram_login(driver, username, password)

        # Reels Link'i alalım
        reels_link = input("Reels URL'sini Girin: ")
        print(f"Reels Bağlantısı: {reels_link}")

        # Kaç adet işlem yapılacak
        count = input("Kaç Adet Olabilir? ")
        print(f"{count} adet işlem başlıyor...")

        # İşlemleri başlat
        print("\033[32mİşlem Başlıyor ❤️\033[0m")  # Yeşil renk
        time.sleep(2)

        # Sürücü kapatılıyor
        driver.quit()
    else:
        print("\033[31mHatalı Seçim! Programdan çıkılıyor...\033[0m")
