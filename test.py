import requests
from bs4 import BeautifulSoup

# URL cần crawl (ví dụ: tìm kiếm từ khóa "travel")
url = "https://truyenqqto.com/"

# Giả lập header để tránh bị chặn
headers = {
    "authority": "www.google.com",
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "accept-language": "en-US,en;q=0.9",
    "cache-control": "max-age=0",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36",
    "Access-Control-Allow-Credentials": "true",
    "Access-Control-Allow-Origin": "https://yody.vn",
    "Cache-Control": "no-cache, no-store, max-age=0, must-revalidate",
    "Content-Encoding": "gzip",
    "Content-Type": "application/json",
    "Date": "Sun, 02 Mar 2025 03:39:44 GMT",
    "Expires": "0",
    "Pragma": "no-cache",
    "Strict-Transport-Security": "max-age=15724800; includeSubDomains",
    "Vary": "Origin",
    "Vary": "Access-Control-Request-Method",
    "Vary": "Access-Control-Request-Headers",
    "Vary": "Origin",
    "Via": "kong/3.3.1",
    "X-Content-Type-Options": "nosniff",
    "X-Frame-Options": "DENY",
    "X-Kong-Proxy-Latency": "0",
    "X-Kong-Upstream-Latency": "14",
    "X-Xss-Protection": "1; mode=block",
}

# Gửi yêu cầu HTTP
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.content, "html.parser")

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