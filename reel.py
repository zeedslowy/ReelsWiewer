from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from time import sleep

# Geckodriver yolunu belirtin
gecko_driver_path = 'geckodriver'

# WebDriver ayarları
service = Service(gecko_driver_path)
options = Options()
options.add_argument("--headless")  # Tarayıcıyı başsız modda çalıştırmak için (isteğe bağlı)

# WebDriver'ı başlatın
driver = webdriver.Firefox(service=service, options=options)

# Instagram giriş bilgileri
username = "kullanici_adi"  # Buraya kendi kullanıcı adınızı girin
password = "sifre"          # Buraya kendi şifrenizi girin

# Instagram URL'si
url = 'https://www.instagram.com'

# Instagram'da giriş yapma fonksiyonu
def login_to_instagram(driver, username, password):
    driver.get(url)
    sleep(2)
    # Kullanıcı adı ve parola alanlarını bulma
    username_input = driver.find_element("name", "username")
    password_input = driver.find_element("name", "password")
    # Kullanıcı adı ve parolayı girme
    username_input.send_keys(username)
    password_input.send_keys(password)
    # Giriş yapma
    password_input.send_keys(Keys.RETURN)
    sleep(6)

# Sayfayı belirli aralıklarla yenileme fonksiyonu
def refresh_page(driver, target_url, refresh_interval=5, refresh_count=15):
    driver.get(target_url)
    for _ in range(refresh_count):
        sleep(refresh_interval)
        driver.refresh()
        print(f'Refreshed the page {_+1} times')

# Instagram'a giriş yap
login_to_instagram(driver, username, password)

# Yenilemek istediğiniz Instagram sayfasının URL'sini girin
target_url = 'https://www.instagram.com/reel/C-Vk6RXPXKE/'

# Yenileme işlemini başlat
refresh_page(driver, target_url)

# WebDriver'ı kapatın
driver.quit()
