from selenium import webdriver 
import time

driver=webdriver.Chrome('C:/Users/mulus/OneDrive/Masaüstü/Python/Python-100Days/chromedriver.exe')


url="http://github.com"

driver.get(url)                                                     # Driver metodu üzerinden get() fonksiyonu ile sayfa açıldı
time.sleep(2)                                                       # 2 saniye bekleme süresi
driver.maximize_window()                                            # Tam ekran modu


print(driver.title)                                                 # Ziyaret edilen sayfanın başlığı yazdırılır

time.sleep(2)
driver.close()                                                      # Tarayıcı kapatılır                           
