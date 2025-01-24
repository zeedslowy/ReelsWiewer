import os
import subprocess
from time import sleep

# Renkli yazılar için ANSI kodları
class Colors:
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    RED = '\033[31m'
    RESET = '\033[0m'

# Banner
def banner():
    print(f"{Colors.GREEN}**************************************************")
    print(f"************     VİOSRİO İNSTA TOOL     ************")
    print(f"**************************************************\n")
    print(f"{Colors.YELLOW}1. İNSTALOADER")
    print(f"2. WEB DRİVER")
    print(f"3. MOZİLLA FİREFOX\n")

# Kullanıcıdan seçim almak
def get_user_choice():
    choice = input(f"{Colors.BLUE}HANGİ KÜTÜPHANE SEÇİN? : {Colors.RESET}")
    return choice

# Instaloader kurulumu
def install_instaloader():
    print(f"{Colors.GREEN}Instaloader kurulumu başlatılıyor...{Colors.RESET}")
    os.system("pip install instaloader")
    print(f"{Colors.GREEN}Instaloader başarıyla kuruldu!{Colors.RESET}")

# WebDriver kurulumu
def install_webdriver():
    print(f"{Colors.GREEN}Web Driver kurulumu başlatılıyor...{Colors.RESET}")
    os.system("pip install selenium")
    print(f"{Colors.GREEN}WebDriver başarıyla kuruldu!{Colors.RESET}")

# Mozilla Firefox kurulumu
def install_firefox():
    print(f"{Colors.GREEN}Mozilla Firefox kurulumu başlatılıyor...{Colors.RESET}")
    os.system("apt-get install firefox -y")  # Termux/Ubuntu ortamında
    print(f"{Colors.GREEN}Mozilla Firefox başarıyla kuruldu!{Colors.RESET}")

# WebDriver başlatma fonksiyonu
def setup_driver():
    geckodriver_path = os.path.abspath("geckodriver")
    
    if not os.path.isfile(geckodriver_path):
        print(f"{Colors.RED}Geckodriver bulunamadı. Lütfen geckodriver'ı doğru yere yerleştirdiğinizden emin olun!{Colors.RESET}")
        return
    
    try:
        from selenium import webdriver
        from selenium.webdriver.firefox.service import Service
        service = Service(geckodriver_path)
        driver = webdriver.Firefox(service=service)
        driver.get("https://www.google.com")
        print(f"{Colors.GREEN}Firefox çalışıyor: {driver.title}{Colors.RESET}")
        driver.quit()
    except Exception as e:
        print(f"{Colors.RED}Hata oluştu: {str(e)}{Colors.RESET}")

# Kurulum dosyasını kontrol et ve işlemi başlat
def setup_from_file():
    if os.path.exists("setup.txt"):
        print(f"{Colors.YELLOW}setup.txt dosyası bulundu. Kurulumlar başlatılıyor...{Colors.RESET}")
        with open("setup.txt", "r") as file:
            commands = file.readlines()
            for command in commands:
                print(f"{Colors.YELLOW}Çalıştırılıyor: {command.strip()}{Colors.RESET}")
                os.system(command.strip())
                sleep(1)  # Her komut arasında kısa bir bekleme

# Ana fonksiyon
def main():
    banner()  # Banner göster
    choice = get_user_choice()  # Kullanıcıdan seçim al
    
    if choice == '1':
        install_instaloader()  # Instaloader kurulumu
    elif choice == '2':
        install_webdriver()  # WebDriver kurulumu
        setup_driver()  # WebDriver'ı başlat
    elif choice == '3':
        install_firefox()  # Firefox kurulumu
    else:
        print(f"{Colors.RED}Geçersiz seçim!{Colors.RESET}")
        exit()

# Programı çalıştır
if __name__ == "__main__":
    main()
