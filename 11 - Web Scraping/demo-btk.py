from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
from csv import writer  


url = "https://www.btkakademi.gov.tr/portal/catalog?categoryId=353"

# 'requests.get' yerine tarayıcıyı (Driver) başlatıyoruz
driver = webdriver.Chrome()
driver.get(url)

try:
    # Kritik Adım: Sayfanın ve o ID'nin yüklenmesini bekliyoruz (Max 10 sn)
    print("Sayfa yükleniyor, lütfen bekleyin...")
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "gbt_catalog-main-right-course"))
    )

    # Sayfa kaynağını 'response.text' yerine 'driver.page_source' ile alıyoruz
    html_icerigi = driver.page_source
    html = BeautifulSoup(html_icerigi, "html.parser")

    kurslar = html.find(id="gbt_catalog-main-right-course").find_all(class_="ant-ribbon-wrapper")

    with open("kurslar.csv","w",encoding="utf-8",newline="") as file:
        csv_writer = writer(file)
        csv_writer.writerow(["link","image","title","like","ogrenci"])

        for kurs in kurslar:
            anchor = kurs.a
            link = anchor.get("href")
            image = anchor.img.get("src")
            title = anchor.find(class_="font-medium text-base").string

            sayilar = anchor.next_sibling.next_sibling.get_text(separator="-").split("-")
            like = sayilar[0]
            ogrenci = sayilar[1]    

            csv_writer.writerow([link,image,title,like,ogrenci])
        

except Exception as e:
    print(f"Bir hata oluştu: {e}")

finally:
    driver.quit()