from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

# GECKO DRIVER YOLU
gecko_driver_path = 'geckodriver'

# WEBDRIVER AYARI
service = Service(gecko_driver_path)
options = Options()
options.add_argument("--headless")  # Tarayıcıyı başsız modda çalıştırır

# WEBDRIVER BAŞLAT
driver = webdriver.Firefox(service=service, options=options)

# İnstagram giriş bilgileri
username = 'mehmetsenturk750'
password = 'mehmet1'

# İnstagram URL
url = 'https://www.instagram.com'

# İnstagram'a giriş fonksiyonu
def login_to_instagram(driver, username, password):
    driver.get(url)
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "username"))
    )

    # Kullanıcı adı ve şifre alanlarını bul
    username_input = driver.find_element(By.NAME, "username")
    password_input = driver.find_element(By.NAME, "password")

    # Kullanıcı adı ve şifreyi gir
    username_input.send_keys(username)
    password_input.send_keys(password)

    # Giriş yap
    password_input.send_keys(Keys.RETURN)
    sleep(6)  # Oturum açmanın tamamlanmasını bekler

# Sayfayı belirli aralıklarla yenileme
def refresh_page(driver, target_url, refresh_interval=5, refresh_count=15):
    driver.get(target_url)
    for i in range(refresh_count):
        sleep(refresh_interval)
        driver.refresh()
        print(f'Sayfa {i+1} defa yenilendi')

# Giriş yap
try:
    login_to_instagram(driver, username, password)
    print("Giriş başarılı!")
except Exception as e:
    print(f"Giriş sırasında bir hata oluştu: {e}")
    driver.quit()
    exit()

# Yenilenecek hedef URL (örnek reels içeriği)
target_url = 'https://www.instagram.com/reel/Cqb2zmGonJm/'

# Yenileme işlemini başlat
try:
    refresh_page(driver, target_url)
except Exception as e:
    print(f"Yenileme sırasında bir hata oluştu: {e}")

# WebDriver'ı kapat
driver.quit()
