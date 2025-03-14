from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

chrome_options = Options()
chrome_options.add_argument("--headless")  # Chạy ẩn trình duyệt
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")

# Đường dẫn đến ChromeDriver (sử dụng raw string hoặc dấu gạch chéo ngược kép)
service = Service(r'E:\chromedriver-win64\chromedriver-win64\chromedriver.exe')

# Khởi tạo trình duyệt
driver = webdriver.Chrome(service=service, options=chrome_options)

# URL cần crawl
url = "https://www.scrapingcourse.com/cloudflare-challenge"

# Mở trang web
driver.get(url)

# Đợi một chút để trang web tải xong
time.sleep(5)

# Lấy nội dung HTML sau khi trang đã tải xong
html_content = driver.page_source

# Đóng trình duyệt
driver.quit()

# Sử dụng BeautifulSoup để phân tích HTML
from bs4 import BeautifulSoup

soup = BeautifulSoup(html_content, "html.parser")

# Tìm tất cả các thẻ <img> chứa hình ảnh
pins = soup.find_all("img")

# Lấy thông tin từ các pin
for pin in pins:
    img_url = pin.get("src")  # URL hình ảnh
    alt_text = pin.get("alt")  # Mô tả hình ảnh
    if img_url and alt_text:
        print(f"Hình ảnh: {img_url}")
        print(f"Mô tả: {alt_text}")
        print("---")